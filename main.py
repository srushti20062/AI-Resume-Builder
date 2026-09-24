from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="AI Resume Builder")


@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>AI Resume Builder</title>
    </head>
    <body>
        <h1>AI Resume Builder</h1>
        <p>Your application is working!</p>
    </body>
    </html>
    """


@app.get("/health")
def health():
    return {"status": "AI Resume Builder is running"}
