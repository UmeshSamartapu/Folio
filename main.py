from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
from datetime import datetime

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

# Profile data - customized with your information
PROFILE_DATA = {
    "name": "Umesh Samartapu",
    "title": "AI/ML & Full Stack Developer",
    "contact": {
        "phone": "+91 9063228334",
        "email": "umeshsamartapu@gmail.com",
        "linkedin": "https://linkedin.com/in/umeshsamartapu",
        "github": "https://github.com/UmeshSamartapu"
    },
    "about": """
        Aspiring Full Stack Developer with hands-on experience in building scalable web applications 
        using the MERN stack and deploying AI-powered projects. Currently pursuing B.Tech in Computer 
        Science Engineering with specialization in AI/ML and Full Stack Development.
    """,
    "education": [
        {
            "degree": "B.Tech in Computer Science Engineering",
            "institute": "Avanthi Institute of Engineering and Technology, Gunthapally",
            "score": "CGPA: 8.14",
            "year": "2022-2026"
        },
        {
            "degree": "Intermediate (MPC)",
            "institute": "TSRJC, Sarvail, Choutuppal",
            "score": "91.8%",
            "year": "2020-2022"
        },
        {
            "degree": "SSC",
            "institute": "S.T.Thomas High School, Dilsukhnagar, Hyderabad",
            "score": "10.0 GPA",
            "year": "2020"
        }
    ],
    "skills": {
        "Programming": ["Python", "JavaScript", "Java", "C", "Go (Basic)"],
        "Frameworks/Stacks": ["MERN Stack", "Django", "FastAPI", "React.js", "Node.js"],
        "AI/ML": ["PyTorch", "TensorFlow", "scikit-learn", "OpenCV", "Pandas", "NumPy"],
        "Databases": ["MongoDB", "SQL"],
        "Tools & Platforms": ["Docker", "Git", "Kubernetes", "CI/CD", "VS Code"]
    },
    "projects": [
        {
            "title": "AI-Powered DeepFake Detection System",
            "description": "Built and deployed a real-time deepfake detection web app using CNNs and facial movement analysis with >90% detection accuracy.",
            "tags": ["Python", "Django", "PyTorch", "OpenCV"]
        },
        {
            "title": "E-Commerce Web Application",
            "description": "Designed and deployed a scalable shopping platform with authentication, cart, and admin dashboard using MERN stack.",
            "tags": ["React", "Node.js", "MongoDB", "Stripe"]
        },
        {
            "title": "Smart City Traffic Pattern Forecasting",
            "description": "Developed time series forecasting model to predict traffic patterns across four junctions for smart city planning.",
            "tags": ["Python", "Machine Learning", "Time Series"]
        },
        {
            "title": "Agriculture Crop and Weed Detection",
            "description": "Built YOLOv5-based object detection system to identify crops and weeds separately for targeted pesticide spraying.",
            "tags": ["Python", "YOLOv5", "Computer Vision"]
        }
    ],
    "internships": [
        {
            "role": "Full-Stack Web Development Intern",
            "company": "Codtech IT Solutions",
            "duration": "May 2025 - Present"
        },
        {
            "role": "AI Markup Language Intern",
            "company": "Codtech IT Solutions",
            "duration": "Apr 2025 - Present"
        },
        {
            "role": "Data Science & Machine Learning Intern",
            "company": "Upskill Campus / UniConverge Technologies",
            "duration": "Mar-Apr 2025"
        },
        {
            "role": "Generative AI Intern",
            "company": "Prodigy InfoTech",
            "duration": "Apr-May 2025"
        }
    ],
    "achievements": [
        "1st Place, Hackathon – Tech Fest 2024, Avanthi Institute",
        "Runner-Up, Code Unnati Innovative Marathon 2025",
        "Code Unnati Program, SAP India: AI/ML and Industry 4.0 training"
    ],
    "languages": [
        "English (Fluent)",
        "Telugu (Native)",
        "Hindi (Basic)"
    ],
    "now": datetime.now()
}

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "profile": PROFILE_DATA})

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)