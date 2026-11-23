@'
# Week 5 - LLM Application

## Project Overview
A FastAPI-based LLM application demonstrating streaming responses,
conversation memory, token counting, and safe error handling.

## Features
- FastAPI chat streaming endpoint
- Server-Sent Events (SSE)
- Conversation ID generation
- Conversation history stored in JSON files
- Token usage counting
- Safe streaming error handling
- Mock LLM response for testing

## Project Structure
- app/main.py - FastAPI application
- app/services/stream_service.py - Streaming logic
- app/services/memory_service.py - Conversation memory
- app/services/mock_llm.py - Mock LLM responses
- app/token_counter.py - Token counting
- data/conversations/ - Local conversation storage

## Run the Application

Activate the virtual environment:

```powershell
.\venv\Scripts\Activate.ps1

