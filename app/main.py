
import json
import time

from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse

from app.services.stream_service import generate_stream
from app.token_counter import count_tokens

from app.services.memory_service import (
    create_conversation_id,
    load_conversation,
    save_conversation
)

app = FastAPI()


@app.post("/chat/stream")
async def chat_stream(request: dict):

    prompt = request.get("prompt")
    conversation_id = request.get("conversation_id")

    if not conversation_id:
        conversation_id = create_conversation_id()

    messages = load_conversation(conversation_id)

    # Validate prompt
    if not isinstance(prompt, str) or not prompt.strip():
        raise HTTPException(
            status_code=400,
            detail="Prompt is required"
        )

    def event_generator():

        start_time = time.perf_counter()
        first_token_time = None

        prompt_tokens = count_tokens(prompt)
        full_response = ""

        try:
            for chunk in generate_stream(prompt, messages):

                if not isinstance(chunk, str):
                    chunk = str(chunk)

                full_response += chunk

                if first_token_time is None:
                    first_token_time = time.perf_counter()

                data = json.dumps({
                    "content": chunk
                })

                yield f"data: {data}\n\n"

        except Exception:
            error_data = json.dumps({
                "error": "LLM generation failed"
            })

            yield f"data: {error_data}\n\n"
            yield "data: [DONE]\n\n"
            return

        end_time = time.perf_counter()

        total_time = end_time - start_time

        ttft = (
            first_token_time - start_time
            if first_token_time is not None
            else 0.0
        )

        response_tokens = count_tokens(full_response)

        usage = {
            "prompt_tokens": prompt_tokens,
            "response_tokens": response_tokens,
            "total_tokens": prompt_tokens + response_tokens,
            "time_to_first_token": round(ttft, 4),
            "total_response_time": round(total_time, 4)
        }

        yield f"data: {json.dumps({'usage': usage})}\n\n"

        # Save conversation history
        messages.append({
            "role": "user",
            "content": prompt
        })

        messages.append({
            "role": "assistant",
            "content": full_response
        })

        save_conversation(conversation_id, messages)

        yield "data: [DONE]\n\n"
    def event_generator_with_id():
        yield f"data: {json.dumps({'conversation_id': conversation_id})}\n\n"
        yield from event_generator()


    return StreamingResponse(
        event_generator_with_id(),
        media_type="text/event-stream"
    )
