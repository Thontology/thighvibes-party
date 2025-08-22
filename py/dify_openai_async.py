import re
import uuid
import asyncio
from typing import AsyncGenerator, List

from openai.types.chat import (
    ChatCompletion,
    ChatCompletionChunk,
    ChatCompletionMessage,
    ChatCompletionMessageParam,
)
from openai.types.chat.chat_completion import Choice
from openai.types.chat.chat_completion_chunk import Choice as ChunkChoice, ChoiceDelta
from dify_client import AsyncClient, models


class DifyOpenAIAsync:
    def __init__(self, *, api_key: str, base_url: str):
        self._dify = AsyncClient(api_key=api_key, api_base=base_url)

    class Completions:
        def __init__(self, dify: AsyncClient):
            self._dify = dify

        async def create(
            self,
            *,
            messages: List[ChatCompletionMessageParam],
            model: str = "dify",
            stream: bool = False,
            **_,
        ):
            query = messages[-1]["content"] or ""
            inputs = {m["role"]: m["content"] for m in messages[:-1] if m["role"] != "user"}

            conversion_id = None
            for m in messages:
                if m["role"] == "assistant":
                    if match := re.search(r"<conversion id:(.*?)>", m["content"] or ""):
                        conversion_id = match.group(1).strip()
                        break

            req = models.ChatRequest(
                query=query,
                inputs=inputs,
                user="super-agent-party",
                response_mode=models.ResponseMode.STREAMING if stream else models.ResponseMode.BLOCKING,
                conversation_id=conversion_id or None,
            )

            if not stream:
                dify_resp = await self._dify.achat_messages(req, timeout=60)
                cid = dify_resp.conversation_id or ""
                content = dify_resp.answer or ""
                if not conversion_id and cid:
                    content = f"<conversion id:{cid}>\n{content}"
                return ChatCompletion(
                    id="super-agent-party",
                    object="chat.completion",
                    created=int(asyncio.get_event_loop().time()),
                    model=model,
                    choices=[
                        Choice(
                            index=0,
                            message=ChatCompletionMessage(role="assistant", content=content),
                            finish_reason="stop",
                        )
                    ],
                )

            async def _stream():
                cid = None
                first = True
                async for chunk in await self._dify.achat_messages(req, timeout=60):
                    # 只有 MessageStreamResponse 才有 answer
                    delta = getattr(chunk, "answer", "") or ""
                    if first and delta:
                        cid = getattr(chunk, "conversation_id", None)
                        if cid and not conversion_id:
                            delta = f"<conversion id:{cid}>\n{delta}"
                        first = False

                    yield ChatCompletionChunk(
                        id="super-agent-party",
                        object="chat.completion.chunk",
                        created=int(asyncio.get_event_loop().time()),
                        model=model,
                        choices=[
                            ChunkChoice(
                                index=0,
                                delta=ChoiceDelta(role="assistant", content=delta),
                                finish_reason=None,
                            )
                        ],
                    )

                # 结束帧
                yield ChatCompletionChunk(
                    id="super-agent-party",
                    object="chat.completion.chunk",
                    created=int(asyncio.get_event_loop().time()),
                    model=model,
                    choices=[ChunkChoice(index=0, delta=ChoiceDelta(), finish_reason="stop")],
                )

            return _stream()

    @property
    def chat(self):
        return type("Chat", (), {"completions": self.Completions(self._dify)})()