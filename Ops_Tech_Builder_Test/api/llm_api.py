from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import Optional
import os
import openai
import google.generativeai as genai

app = FastAPI()

class SummarizeRequest(BaseModel):
    text: str
    provider: Optional[str] = "openai" 
@app.get("/list_models")
async def list_models(provider: Optional[str] = "gemini"):
    provider = provider.lower()

    if provider == "openai":
        try:
            openai.api_key = os.getenv("OPENAI_API_KEY")
            models = openai.Model.list()
            return {
                "provider": "openai",
                "models": [
                    {"id": m.id, "object": m.object}
                    for m in models["data"]
                ]
            }
        except Exception as e:
            return {"error": str(e)}

    elif provider == "gemini":
        try:
            genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
            models = genai.list_models()
            return {
                "provider": "gemini",
                "models": [
                    {
                        "name": m.name,
                        "display_name": m.display_name,
                        "supported_generation_methods": m.supported_generation_methods,
                    }
                    for m in models
                ]
            }
        except Exception as e:
            return {"error": str(e)}

    else:
        return {"error": "Unknown provider. Use 'openai' or 'gemini'."}
@app.post("/summarize")
async def summarize(req: SummarizeRequest):
    text = req.text
    provider = req.provider.lower() if req.provider else "openai"
    summary = ""

    if provider == "openai":
        api_key = os.getenv("OPENAI_API_KEY")
        if api_key:
            openai.api_key = api_key
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "system", "content": "Summarize the following text."},
                          {"role": "user", "content": text}],
                max_tokens=100
            )
            summary = response.choices[0].message["content"].strip()
        else:
            # Mocked response
            summary = f"[MOCKED OPENAI] Summary of: {text[:30]}..."
    elif provider == "claude":
        # Mocked Claude response (since Anthropic API is not public for all)
        summary = f"[MOCKED CLAUDE] Summary of: {text[:30]}..."
    elif provider == "gemini":
        gemini_api_key = os.getenv("GEMINI_API_KEY")
        if gemini_api_key:
            try:
                import google.generativeai as genai
                genai.configure(api_key=gemini_api_key)
                model = genai.GenerativeModel("models/gemini-1.0-pro-latest")
                response = model.generate_content(f"Summarize the following text:\n{text}")
                summary = response.text.strip()
            except Exception as e:
                summary = f"[GEMINI ERROR] {str(e)}"
        else:
            summary = f"[MOCKED GEMINI] Summary of: {text[:30]}..."
    else:
        return {"error": "Unknown provider. Use 'openai', 'claude', or 'gemini'."}

    return {"summary": summary} 