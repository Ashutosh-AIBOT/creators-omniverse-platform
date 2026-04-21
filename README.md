# 🚀 CreatorsOmniverse — Full-Stack Creator Platform

![Python](https://img.shields.io/badge/Python-3.10-blue?style=flat-square&logo=python)
![Django](https://img.shields.io/badge/Backend-Django-darkgreen?style=flat-square&logo=django)
![Docker](https://img.shields.io/badge/Deploy-Docker-blue?style=flat-square&logo=docker)
![Nginx](https://img.shields.io/badge/Server-Nginx-green?style=flat-square&logo=nginx)
![HTML](https://img.shields.io/badge/Frontend-HTML_81%25-orange?style=flat-square)
![CI/CD](https://img.shields.io/badge/CI/CD-GitLab_Pipeline-red?style=flat-square&logo=gitlab)
![Status](https://img.shields.io/badge/Stage-Complete-green?style=flat-square)

---

🌐 **Live:** [ashutosh1975-spacelink.hf.space](https://ashutosh1975-spacelink.hf.space/)
👤 **Author:** [Ashutosh](https://github.com/Ashutosh-AIBOT) · [LinkedIn](https://www.linkedin.com/in/ashutosh1975271/)
💼 **Portfolio:** [ashutosh-portfolio-kappa.vercel.app](https://ashutosh-portfolio-kappa.vercel.app/)

---

## 📋 Table of Contents

- [What This Does](#-what-this-does)
- [Platform Features](#-platform-features)
- [App Structure](#-app-structure)
- [Architecture](#-architecture)
- [What I Built](#-what-i-built)
- [Docker Setup](#-docker-setup)
- [CI/CD Pipeline](#-cicd-pipeline)
- [Quick Start](#-quick-start)
- [Tech Stack](#-tech-stack)
- [Project Status](#-project-status)
- [Links](#-links)
- [Author](#-author)

---

## 🧠 What This Does

CreatorsOmniverse is a full-stack Django web platform
built for creators — learners, builders, and makers —
to manage their profiles, study resources, and interact
with an AI companion called Xomni.

1. **Problem** — Creators have no single platform to
   manage their portfolio, organize study resources,
   and get AI assistance — all in one place.
2. **Solution** — A multi-app Django platform with user
   auth, profiles, study tools, AI companion, resource
   collections, fully Dockerized with Nginx and CI/CD.
3. **For** — Full-Stack / Django / Python Developer
   hiring managers looking for real production-grade
   Django application proof.

---

## ✨ Platform Features

| Feature | App | What It Does |
|---------|-----|-------------|
| 🔐 User Authentication | `core` | Register, login, logout, session management |
| 👤 Creator Profiles | `testprofiles` | Public profile pages per user |
| 📚 Study Tools | `study` | Organize and track learning resources |
| 🤖 AI Companion (Xomni) | `xomni` | AI assistant built into the platform |
| 📦 Resource Collections | `collection` | Save and organize creator resources |
| 🌌 Universe Feed | `universe` | Community content discovery feed |
| 💼 Portfolio Display | `portfolio` | Showcase projects and work |
| 🧠 Overthinker Mode | `Overthinker` | Brainstorming and idea capture tool |

---

## 📁 App Structure
```
creators-omniverse-platform/
│
├── core/                   # Base app — auth, settings, base templates
├── portfolio/              # Creator portfolio display
├── study/                  # Study tools and resource tracking
├── xomni/                  # AI companion (Xomni) integration
├── collection/             # Resource collection management
├── universe/               # Community feed
├── Overthinker/            # Idea capture and brainstorming
├── testprofiles/           # User profile pages
├── testaccounts/           # Account management
├── templates/              # All HTML templates
├── static/css/             # Stylesheets
├── nginx/                  # Nginx server configuration
├── CreatorsOmniverse/      # Django project settings
│
├── manage.py
├── requirements.txt
├── Dockerfile
├── Dockerfile-django
├── docker-compose.yml
├── docker-compose.prod.yml
├── supervisor.conf
├── .gitlab-ci.yml          # CI/CD pipeline config
└── README.md
```

---

## 🏗️ Architecture
```
User Browser
      ↓
Nginx (Reverse Proxy)
  → Static file serving
  → Load balancing
  → SSL termination
      ↓
Django Application
  ├── core          → Auth + base config
  ├── portfolio     → Project showcase
  ├── study         → Learning management
  ├── xomni         → AI companion
  ├── collection    → Resource library
  ├── universe      → Community feed
  ├── Overthinker   → Idea capture
  └── testprofiles  → User profiles
      ↓
Database (SQLite → PostgreSQL)
      ↓
Static Files
  → CSS/JS/Images served via Nginx
```

---

## 🔨 What I Built

### 1. Multi-App Django Project
- Modular Django architecture with 8 independent apps
- Each app has its own models, views, URLs, and templates
- Shared base template with consistent navigation
- Django ORM for all database operations
- Custom user model with extended profile fields

### 2. User Authentication System (`core`)
- Full register / login / logout flow
- Session-based authentication
- Password validation and error handling
- Redirect logic after login/logout
- Protected views with `@login_required`

### 3. Creator Profiles (`testprofiles`)
- Public profile page per registered user
- Profile picture, bio, skills display
- Links to portfolio and social accounts
- Profile edit form with validation

### 4. Study Tools (`study`)
- Add, organize, and track study resources
- Category-based resource organization
- Progress tracking per study item
- Notes and bookmark functionality

### 5. AI Companion — Xomni (`xomni`)
- Integrated AI assistant inside the platform
- Context-aware responses for creator tasks
- Connected to LLM API for intelligent replies
- Conversation history per user session

### 6. Resource Collections (`collection`)
- Save external links, videos, articles
- Organize into named collections
- Share collections publicly or keep private
- Search and filter saved resources

### 7. Universe Feed (`universe`)
- Community-style content discovery
- Posts and shares from all platform users
- Like, save, and comment on content
- Personalized feed based on interests

### 8. Portfolio Display (`portfolio`)
- Showcase projects with descriptions and links
- Skills and tech stack display
- Responsive card-based layout
- Public portfolio URL per user

### 9. Docker + Nginx Setup
- `Dockerfile` for development container
- `Dockerfile-django` for production Django container
- `docker-compose.yml` for local development
- `docker-compose.prod.yml` for production deployment
- Nginx configuration for reverse proxy + static files
- Supervisor config for process management

### 10. CI/CD Pipeline (GitLab)
- `.gitlab-ci.yml` automates test + build + deploy
- Pipeline stages: test → build → deploy
- Docker image build on every push
- Automated deployment on merge to main

---

## 🐳 Docker Setup
```bash
# Development
docker-compose up --build

# Production
docker-compose -f docker-compose.prod.yml up --build

# Services started:
# Django app    → http://localhost:8000
# Nginx proxy   → http://localhost:80
```

**Container structure:**
```
docker-compose.yml
  ├── web (Django app)
  ├── nginx (reverse proxy)
  └── db (PostgreSQL)
```

---

## 🔄 CI/CD Pipeline
```
Push to GitLab
      ↓
Stage 1: Test
  → Run Django unit tests
  → Check migrations
  → Lint Python code
      ↓
Stage 2: Build
  → Build Docker image
  → Tag with commit hash
      ↓
Stage 3: Deploy
  → Push image to registry
  → Deploy to server
  → Restart containers
```

---

## ⚡ Quick Start

**Prerequisites:** Python 3.10+, Git

**Option 1 — Without Docker:**
```bash
# 1. Clone the repo
git clone https://github.com/Ashutosh-AIBOT/creators-omniverse-platform.git
cd creators-omniverse-platform

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations
python manage.py migrate

# 5. Create superuser
python manage.py createsuperuser

# 6. Run server
python manage.py runserver

# 7. Open browser
# http://localhost:8000
```

**Option 2 — With Docker:**
```bash
# 1. Clone the repo
git clone https://github.com/Ashutosh-AIBOT/creators-omniverse-platform.git
cd creators-omniverse-platform

# 2. Start all services
docker-compose up --build

# 3. Open browser
# http://localhost:80
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.10 | Core language |
| Django | Full-stack web framework |
| HTML 81% | Frontend templates |
| CSS 10.8% | Styling and layout |
| SQLite / PostgreSQL | Database |
| Nginx | Reverse proxy + static files |
| Docker + Docker Compose | Containerization |
| GitLab CI/CD | Automated pipeline |
| Supervisor | Process management |
| Git | Version control |

---

## 📊 Project Status

| Deliverable | Status |
|-------------|--------|
| User Authentication | ✅ Complete |
| Creator Profiles | ✅ Complete |
| Study Tools | ✅ Complete |
| AI Companion (Xomni) | ✅ Complete |
| Resource Collections | ✅ Complete |
| Universe Community Feed | ✅ Complete |
| Portfolio Display | ✅ Complete |
| Overthinker Tool | ✅ Complete |
| Docker Setup | ✅ Complete |
| Nginx Configuration | ✅ Complete |
| GitLab CI/CD Pipeline | ✅ Complete |
| Production Deployment | ✅ Live |

---

## 🌐 Links

| Resource | URL |
|----------|-----|
| 🚀 Live Platform | [ashutosh1975-spacelink.hf.space](https://ashutosh1975-spacelink.hf.space/) |
| 💼 Portfolio | [ashutosh-portfolio-kappa.vercel.app](https://ashutosh-portfolio-kappa.vercel.app/) |
| 🐙 GitHub | [github.com/Ashutosh-AIBOT](https://github.com/Ashutosh-AIBOT) |
| 🔗 LinkedIn | [linkedin.com/in/ashutosh1975271](https://www.linkedin.com/in/ashutosh1975271/) |

---

## 👤 Author

**Ashutosh**
B.Tech Electronics Engineering · CGPA 7.5 · Batch 2026
[GitHub](https://github.com/Ashutosh-AIBOT) · [LinkedIn](https://www.linkedin.com/in/ashutosh1975271/) · [Portfolio](https://ashutosh-portfolio-kappa.vercel.app/)

---

> *"8 apps. 1 platform. Real Django.*
> *Auth. Profiles. AI. Docker. CI/CD.*
> *Built from scratch. Shipped to production."*
>
> — Ashutosh, building this from zero.
```
