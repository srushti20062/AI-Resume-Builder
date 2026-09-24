from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI(title="AI Resume Builder")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


@app.post("/generate-resume")
async def generate_resume(data: dict):

    name = data.get("name", "")
    email = data.get("email", "")
    phone = data.get("phone", "")
    role = data.get("role", "")
    education = data.get("education", "")
    skills = data.get("skills", "")
    projects = data.get("projects", "")
    experience = data.get("experience", "")

    # AI-style professional summary
    if role:
        summary = (
            f"Motivated and enthusiastic {role} with a strong foundation "
            f"in {skills}. Experienced in developing projects such as "
            f"{projects}. Passionate about applying technical knowledge "
            f"to solve real-world problems and continuously improving "
            f"professional skills."
        )
    else:
        summary = (
            f"Motivated student with knowledge in {skills}. "
            f"Experienced in academic projects including {projects}. "
            f"Eager to apply technical knowledge to real-world problems."
        )

    return {
        "name": name,
        "email": email,
        "phone": phone,
        "role": role,
        "education": education,
        "skills": skills,
        "projects": projects,
        "experience": experience,
        "summary": summary
    }


@app.get("/health")
async def health():
    return {
        "status": "AI Resume Builder is running"
    }
