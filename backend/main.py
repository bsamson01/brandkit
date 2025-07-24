import os
import uuid
from typing import List, Optional, Dict, Any

from fastapi import FastAPI, BackgroundTasks, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import openai

# Load environment variables from .env file at project root
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY not found in environment. Please create a .env file with OPENAI_API_KEY=<your_key>.")

openai.api_key = OPENAI_API_KEY

app = FastAPI(title="BrandKit Builder Backend", version="0.1.0")

# Allow local dev front-end to access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify allowed origins explicitly
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory task store (single-user, MVP)
Tasks: Dict[str, Dict[str, Any]] = {}

##############################
# Pydantic models
##############################

class BusinessInput(BaseModel):
    business_name: str = Field(..., example="Acme Corp")
    industry: str = Field(..., example="E-commerce")
    tagline: Optional[str] = Field(None, example="We deliver everything")

class TaskResponse(BaseModel):
    task_id: str
    status: str

class TaglineSelection(BaseModel):
    tagline: str

class ColorPaletteSelection(BaseModel):
    palette: List[str]

##############################
# Helper functions
##############################

def _upsert_task(task_id: str, status: str, result: Optional[Any] = None):
    Tasks[task_id] = {"status": status, "result": result}


def _generate_taglines(business_name: str, industry: str, task_id: str):
    """Background task for generating taglines via OpenAI GPT-4"""
    try:
        prompt = (
            f"Generate 5 creative marketing taglines for a {industry} business called '{business_name}'. "
            "Return the taglines as a JSON array of strings, no additional text."
        )
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",  # use cheaper 4o or change as needed
            messages=[{"role": "user", "content": prompt}],
            temperature=0.8,
        )
        # Extract JSON array from response
        content = response.choices[0].message.content.strip()
        # Basic safety: attempt eval; in production use json.loads after validation
        taglines: List[str] = []
        try:
            import json
            taglines = json.loads(content)
            if not isinstance(taglines, list):
                raise ValueError
        except Exception:
            # Fallback: split by newline
            taglines = [line.strip("- ").strip() for line in content.split("\n") if line.strip()]

        _upsert_task(task_id, "completed", taglines)
    except Exception as e:
        _upsert_task(task_id, "failed", str(e))


def _generate_logo_placeholder(business_name: str, tagline: str, palette: List[str], task_id: str):
    """Placeholder logo generation returning dummy image URLs"""
    try:
        # For MVP, return placeholder images from https://placehold.co/
        logos = [
            f"https://placehold.co/600x400?text={business_name.replace(' ', '+')}+Logo+{i+1}" for i in range(3)
        ]
        _upsert_task(task_id, "completed", logos)
    except Exception as e:
        _upsert_task(task_id, "failed", str(e))

##############################
# API endpoints
##############################

@app.post("/api/taglines", response_model=TaskResponse, summary="Request tagline suggestions")
async def request_taglines(data: BusinessInput, background_tasks: BackgroundTasks):
    if data.tagline:
        # User already provided tagline, no need to generate
        task_id = str(uuid.uuid4())
        _upsert_task(task_id, "completed", [data.tagline])
        return TaskResponse(task_id=task_id, status="completed")

    task_id = str(uuid.uuid4())
    _upsert_task(task_id, "processing")
    background_tasks.add_task(_generate_taglines, data.business_name, data.industry, task_id)
    return TaskResponse(task_id=task_id, status="processing")


@app.get("/api/tasks/{task_id}", summary="Get task status or result")
async def get_task(task_id: str):
    if task_id not in Tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    return Tasks[task_id]


@app.post("/api/logos", response_model=TaskResponse, summary="Generate logos (placeholder)")
async def request_logos(
    business: BusinessInput,
    tagline_selection: TaglineSelection,
    palette_selection: ColorPaletteSelection,
    background_tasks: BackgroundTasks,
):
    task_id = str(uuid.uuid4())
    _upsert_task(task_id, "processing")
    background_tasks.add_task(
        _generate_logo_placeholder,
        business.business_name,
        tagline_selection.tagline,
        palette_selection.palette,
        task_id,
    )
    return TaskResponse(task_id=task_id, status="processing")


@app.get("/api/color-palettes", summary="Return predefined color palettes")
async def get_color_palettes():
    palettes = [
        ["#003f5c", "#58508d", "#bc5090", "#ff6361", "#ffa600"],
        ["#264653", "#2a9d8f", "#e9c46a", "#f4a261", "#e76f51"],
        ["#0d1b2a", "#1b263b", "#415a77", "#778da9", "#e0e1dd"],
        ["#ffbe0b", "#fb5607", "#ff006e", "#8338ec", "#3a86ff"],
        ["#2c3e50", "#2980b9", "#27ae60", "#f39c12", "#c0392b"],
    ]
    return {"palettes": palettes}