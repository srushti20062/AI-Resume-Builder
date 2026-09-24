from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI(title="AI Resume Builder")

templates = Jinja2Templates(directory="templates")


# Job-specific keywords
JOB_KEYWORDS = {

    "Software Developer": [
        "python",
        "java",
        "c++",
        "javascript",
        "sql",
        "git",
        "data structures",
        "algorithms",
        "api"
    ],

    "Data Analyst": [
        "python",
        "sql",
        "excel",
        "power bi",
        "tableau",
        "statistics",
        "pandas",
        "numpy",
        "data analysis"
    ],

    "Web Developer": [
        "html",
        "css",
        "javascript",
        "react",
        "node",
        "sql",
        "git",
        "api"
    ],

    "AI/ML Engineer": [
        "python",
        "machine learning",
        "deep learning",
        "tensorflow",
        "pytorch",
        "numpy",
        "pandas",
        "scikit-learn",
        "artificial intelligence"
    ],

    "Student / Fresher": [
        "python",
        "communication",
        "problem solving",
        "sql",
        "html",
        "css",
        "javascript",
        "git"
    ]
}


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

    # Combine resume information
    resume_text = (
        education + " " +
        skills + " " +
        projects + " " +
        experience
    ).lower()


    # -----------------------------
    # AI-STYLE SUMMARY GENERATION
    # -----------------------------

    if role:

        summary = (
            f"Motivated and enthusiastic {role} with a strong foundation "
            f"in {skills}. Experienced in academic and practical projects "
            f"including {projects}. Demonstrates a strong interest in "
            f"problem solving, continuous learning, and applying technical "
            f"knowledge to real-world challenges."
        )

    else:

        summary = (
            f"Motivated student with knowledge in {skills}. "
            f"Experienced in academic projects including {projects}. "
            f"Eager to apply technical knowledge to real-world problems "
            f"and develop professional skills."
        )


    # -----------------------------
    # ATS KEYWORD ANALYSIS
    # -----------------------------

    required_keywords = JOB_KEYWORDS.get(role, [])

    matched_keywords = []
    missing_keywords = []


    for keyword in required_keywords:

        if keyword.lower() in resume_text:

            matched_keywords.append(keyword)

        else:

            missing_keywords.append(keyword)


    # Calculate ATS score

    if required_keywords:

        score = int(
            (len(matched_keywords) /
             len(required_keywords)) * 100
        )

    else:

        score = 0


    # -----------------------------
    # IMPROVEMENT FEEDBACK
    # -----------------------------

    suggestions = []


    if len(skills.strip()) < 20:

        suggestions.append(
            "Add more relevant technical skills."
        )


    if len(projects.strip()) < 30:

        suggestions.append(
            "Add detailed project descriptions and technologies used."
        )


    if len(experience.strip()) < 15:

        suggestions.append(
            "Add internship, training, volunteering, or practical experience."
        )


    if not matched_keywords:

        suggestions.append(
            "Add job-specific keywords from the suggested skills section."
        )


    if score >= 80:

        score_message = (
            "Your resume contains most important keywords "
            "for the selected role."
        )

    elif score >= 50:

        score_message = (
            "Your resume has a moderate keyword match. "
            "Adding relevant skills can improve ATS compatibility."
        )

    else:

        score_message = (
            "Your resume has a low keyword match. "
            "Consider adding relevant skills and project keywords."
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

        "summary": summary,

        "ats_score": score,

        "matched_keywords": matched_keywords,

        "missing_keywords": missing_keywords,

        "suggestions": suggestions,

        "score_message": score_message
    }


@app.get("/health")
async def health():

    return {
        "status": "AI Resume Builder is running"
    }
