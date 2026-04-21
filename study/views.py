from django.shortcuts import render
from django.http import Http404


# -------------------------------------------------
# SINGLE SOURCE OF TRUTH: Sections and topics
# -------------------------------------------------
SECTIONS = {
    "python": {
        "title": "Python",
        "topics": [
            ("Python DSA", "python-dsa"),
            ("Python OOPS", "python-oops"),
            ("Data Science", "data-science"),
            ("Data Analytics", "data-analytics"),
            ("ML Engineering", "machine-learning"),
            ("Deep Learning", "deep-learning"),
            ("Generative AI", "generative-ai"),
            ("MLOps", "mlops"),
            ("Web Development", "web-dev"),
            ("App Development", "app-dev"),
            ("Game Development", "game-dev"),
        ],
    },
    "java": {
        "title": "Java",
        "topics": [
            ("Java Basics", "java-basics"),
            ("Java OOPS", "java-oops"),
            ("Java DSA", "java-dsa"),
            ("Spring Boot", "spring-boot"),
            ("Microservices", "microservices"),
            ("Java Web Dev", "java-web-dev"),
        ],
    },
    "cpp": {
        "title": "C++",
        "topics": [
            ("C++ Basics", "cpp-basics"),
            ("C++ OOPS", "cpp-oops"),
            ("STL", "stl"),
            ("DSA", "dsa"),
            ("Competitive Programming", "competitive-programming"),
            ("System Design", "system-design"),
        ],
    },
    "data-science": {
        "title": "Data Science",
        "topics": [
            ("Machine Learning", "machine-learning"),
            ("Deep Learning", "deep-learning"),
            ("NLP", "nlp"),
            ("Computer Vision", "computer-vision"),
            ("LLMs", "llms"),
            ("AI Agents", "ai-agents"),
            ("Prompt Engineering", "prompt-engineering"),
        ],
    },
    "web-dev": {
        "title": "Web Development",
        "topics": [
            ("Frontend Basics", "frontend-basics"),
            ("Backend Development", "backend-dev"),
            ("APIs & REST", "apis-rest"),
            ("Authentication", "authentication"),
        ],
    },
    "devops": {
        "title": "DevOps",
        "topics": [
            ("Docker", "docker"),
            ("Kubernetes", "kubernetes"),
            ("Jenkins", "jenkins"),
            ("CI/CD Pipelines", "ci-cd"),
            ("Terraform", "terraform"),
            ("Monitoring & Logging", "monitoring-logging"),
            ("Cloud Fundamentals", "cloud-fundamentals"),
        ],
    },
    "database": {
        "title": "Databases",
        "topics": [
            ("SQL", "sql"),
            ("MySQL", "mysql"),
            ("PostgreSQL", "postgresql"),
            ("MongoDB", "mongodb"),
            ("Redis", "redis"),
            ("Data Modeling", "data-modeling"),
        ],
    },
    "new-important": {
        "title": "Other & Important",
        "topics": [
            ("Python OOPS", "python-oops"),
            ("Java OOPS", "java-oops"),
            ("C++ OOPS", "cpp-oops"),
            ("MLOps", "mlops"),
            ("System Design", "system-design"),
            ("Open Source Contribution", "open-source"),
        ],
    },
}

# -------------------------------------------------
# GENERAL STUDY DASHBOARD VIEW (multi-language)
# URL: /study/ or /study/<lang>/
# -------------------------------------------------
def study_language(request, lang="python", topic=None):
    if lang not in SECTIONS:
        raise Http404("Section not found")

    section = SECTIONS[lang]
    selected_topic = None
    selected_topic_title = None
    topic_template = None

    if topic:
        for name, slug in section["topics"]:
            if slug == topic:
                selected_topic = slug
                selected_topic_title = name
                topic_template = f"study/{slug}.html"
                break
        if not selected_topic:
            raise Http404("Topic not found")

    context = {
        "sections": SECTIONS,
        "selected_key": lang,
        "selected_section": section,
        "selected_topic": selected_topic,
        "selected_topic_title": selected_topic_title,
        "topic_template": topic_template,
    }

    return render(request, "study/study_dashboard.html", context)


