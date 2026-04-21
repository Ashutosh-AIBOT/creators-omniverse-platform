from django.shortcuts import render
from django.http import Http404

SECTIONS = {
    
    # ================= CODING LANGUAGES =================
    "coding_languages": {
        "title": "Coding Languages",
        "topics": [
            ("Python", "python"),
            ("R", "r"),
            ("Java", "java"),
            ("C++", "cpp"),
            ("C#", "note"),
            ("JavaScript", "note"),
            ("Ruby", "note"),
            ("Swift", "note"),
            ("Kotlin", "note"),
            ("PHP", "note"),
            ("Objective-C", "note"),
            ("Scala", "note"),
            ("Dart", "note"),
            ("Go (Golang)", "note"),
            ("Perl", "note"),
            ("Rust", "note"),
            ("TypeScript", "note"),
        ],
    },

    # ================= DATABASES =================
    "databases": {
        "title": "Databases",
        "topics": [
            ("MySQL", "mysql"),
            ("PostgreSQL", "postgresql"),
            ("MongoDB", "mongodb"),
            ("Redis", "note"),
            ("Oracle DB", "note"),
            ("SQLite", "note"),
            ("Cassandra", "note"),
            ("Firebase", "note"),
            ("Elasticsearch", "note"),
        ],
    },

    # ================= DATA SCIENCE =================
    "data_science": {
        "title": "Data Science",
        "topics": [
            ("Python Libraries ", "python-libraries"),
            ("Extra libraries", "extra-libraries"),
            ("Data Visualization", "data-visualization"),
            ("Exploratory Data Analysis (EDA)", "eda"),
            ("Statistical Analysis", "statistical-analysis"),
            ("Data Wrangling & Cleaning", "data-wrangling"),
            ("Data Science Overview", "data-science"),
            ("Data Analytics", "data-analytics"),
            ("Data Engineering", "data-engineering"),
            ("Machine Learning", "machine-learning"),
            ("Deep Learning", "deep-learning"),
            ("Natural Language Processing (NLP)", "nlp"),
            ("Computer Vision", "computer-vision"),
            ("Generative AI", "generative-ai"),
            ("LLMs", "llms"),
            ("AI Agents", "ai-agents"),
            ("Big Data", "big-data"),
        ],
    },

    # ================= WEB DEVELOPMENT =================
    "web_development": {
        "title": "Web Development",
        "topics": [
            ("Python Web Development", "python-web-dev"),
            ("Java Web Development", "java-web-dev"),
            ("JavaScript & Frontend", "note"),
            ("React", "note"),
            ("Angular", "note"),
            ("Vue.js", "note"),
            ("Node.js", "note"),
            ("Ruby on Rails", "note"),
            ("PHP Web Development", "note"),
            ("ASP.NET", "note"),
        ],
    },

    # ================= APP DEVELOPMENT =================
    "app_development": {
        "title": "App Development",
        "topics": [
            ("Python App Development", "python-app-dev"),
            ("Java Android Development", "note"),
            ("Kotlin Android Development", "note"),
            ("Swift iOS Development", "note"),
            ("React Native", "note"),
            ("Flutter (Dart)", "note"),
            ("Xamarin (C#)", "note"),
            ("Cordova / PhoneGap", "note"),
            ("Ionic Framework", "note"),
            ("NativeScript", "note"),
        ],
    },

    # ================= DEVOPS & CLOUD =================
    "devops_cloud": {
        "title": "DevOps & Cloud",
        "topics": [
            ("MLOps", "mlops"),
            ("github", "github"),
            ("GitLab", "note"),
            ("Docker", "docker"),
            ("Kubernetes", "kubernetes"),
            ("CI/CD Pipelines", "ci-cd"),
            ("AWS", "aws"),
            ("Azure", "note"),
            ("Google Cloud Platform", "note"),
            ("Cloud Fundamentals", "note"),
            ("Monitoring & Logging", "note"),
            
        ],
    },



    # ================= CYBER SECURITY & WHITE HAT =================
    "cyber_security": {
        "title": "Cyber Security ",
        "topics": [
            ("Cyber Security Basics", "note"),
            ("Ethical Hacking", "note"),
            ("Capture The Flag (CTF)", "note"),
            ("Network Security", "note"),
            ("Penetration Testing", "note"),
            ("Cryptography", "note"),
            ("Malware Analysis", "note"),
            ("Security Tools", "note"),
            ("Security Certifications", "note"),
        ],
    },

    # ================= CRYPTO & BLOCKCHAIN =================
    "crypto_blockchain": {
        "title": "Blockchain",
        "topics": [
            ("Blockchain Basics", "note"),
            ("Cryptocurrency", "note"),
            ("Smart Contracts", "note"),
            ("Decentralized Finance (DeFi)", "note"),
            ("NFTs", "note"),
            ("Crypto Trading", "note"),
            ("Crypto Wallets", "note"),
        ],
    },
    
    
    # ================= CREATIVE & GAMING =================
    "creative_gaming": {
        "title": " Gaming",
        "topics": [
            ("Game Development", "note"),
            ("Unity", "note"),
            ("Unreal Engine", "note"),
            ("Video Editing", "note"),
            ("Photo Editing", "note"),
            ("Motion Graphics", "note"),
            ("Content Creation", "note"),
            ("Gaming Community", "note"),
            ("Gaming Tournaments", "note"),
        ],
    },

    # ================= SOFTWARE DESIGN & OOP =================
    "software_design_oop": {
        "title": "Software Design & OOP",
        "topics": [
            ("Object-Oriented Programming (OOP)", "oop"),
            ("System Design", "system-design"),
            ("Design Patterns", "design-patterns"),
            ("SOLID Principles", "note"),
            ("Microservices Architecture", "note"),
            ("Clean Code", "note"),
            ("Refactoring", "note"),
        ],
    },


    # ================= OPERATING SYSTEMS =================
    "operating_systems": {
        "title": "Operating Systems",
        "topics": [
            ("OS Basics", "os-basics"),
            ("Linux Basics", "linux"),
            ("Windows OS", "note"),
            ("Unix", "note"),
            ("MacOS", "note"),
            ("System Calls", "note"),
            ("Cloud Networking", "note"),
            ("Process Management", "note"),
        ],
    },

    # ================= NETWORKING =================
    "networking": {
        "title": "Networking",
        "topics": [
            ("Network Security", "note"),
            ("Networking Fundamentals", "networking-fundamentals"),
            ("Shell Scripting", "note"),
            ("Computer Networks", "computer-networks"),
            ("TCP/IP", "note"),
            ("HTTP/HTTPS", "note"),
            ("Network Security", "note"),
            ("Firewalls", "note"),
            ("VPNs", "note"),
        ],
    },
    
    # ================= OPEN SOURCE =================
    "open_source": {
        "title": "Open Source",
        "topics": [
            ("Python Open Source", "python-open-source"),
            ("Java Open Source", "java-open-source"),
            ("C++ Open Source", "cpp-open-source"),
            ("Data Science Open Source", "data-science-open-source"),
            ("AI Open Source", "ai-open-source"),
            ("DevOps Open Source", "devops-open-source"),
            ("Web Development Open Source", "web-dev-open-source"),
            ("JavaScript Open Source", "note"),
            ("Open Source Contribution", "note"),
            ("Open Source Projects", "note"),
            ("Open Source Communities", "note"),
            ("Open Source Licensing", "note"),
        ],
    },

    # ================= GITHUB LINKS =================
    "github_links": {
        "title": "GitHub Links",
        "topics": [
            ("Python GitHub Repos", "python-github-repos"),
            ("Java GitHub Repos", "note"),
            ("C++ GitHub Repos", "note"),
            ("Data Science GitHub Repos", "data-science-github-repos"),
            ("AI GitHub Repos", "ai-github-repos"),
            ("DevOps GitHub Repos", "devops-github-repos"),
            ("Web Development GitHub Repos", "note"),
            ("JavaScript GitHub Repos", "note"),
            ("GitHub Trending", "note"),
            ("GitHub Actions", "note"),
            ("GitHub Discussions", "note"),
            ("GitHub Issues", "note"),
            ("GitHub Best Practices", "note"),
        ],
    },

    # ================= JOBS =================
    "jobs": {
        "title": "Jobs",
        "topics": [
            ("Python Jobs", "python-jobs"),
            ("Java Jobs", "java-jobs"),
            ("C++ Jobs", "note"),
            ("JavaScript Jobs", "note"),
            ("Data Science Jobs", "data-science-jobs"),
            ("AI Jobs", "ai-jobs"),
            ("DevOps Jobs", "note"),
            ("Web Development Jobs", "web-dev-jobs"),
            ("Remote Jobs", "remote-jobs"),
            ("Internships", "internships"),
            ("Freelance Jobs", "freelance-jobs"),
            ("Open Source Jobs", "open-source-jobs"),
        ],
    },
    
    # ================= ANALYTICS =================
    "Analytics": {
        "title": "Analytics",
        "topics": [
            ("Web Analytics", "web-analytics"),
            ("Business Analytics", "business-analytics"),
            ("Customer Analytics", "customer-analytics"),
            ("Marketing Analytics", "marketing-analytics"),
            ("Financial Analytics", "financial-analytics"),
        ],
    },

    

    # ================= SOCIAL MEDIA =================
    "social_media": {
        "title": "Social Media",
        "topics": [
            ("YouTube", "youtube"),
            ("Instagram", "instagram"),
            ("Twitter", "twitter"),
            ("LinkedIn", "linkedin"),
            ("Facebook", "note"),
            ("Twitch", "note"),
            ("Pinterest", "note"),
            ("Snapchat", "note"),
            ("Affiliate Marketing", "note"),
            ("Sponsored Content", "note"),
            ("Merchandising", "note"),
            ("Crowdfunding", "note"),
            ("Ad Revenue", "note"),
        ],
    },

    # ================= BUSINESS =================
    "business": {
        "title": "Business",
        "topics": [
            ("Service Based Business", "service-based-business"),
            ("Product Based Business", "product-based-business"),
            ("Startups", "startups"),
            ("E-commerce", "e-commerce"),
            ("SaaS (Software as a Service)", "note"),
            ("B2B Business Models", "note"),
            ("B2C Business Models", "note"),
            ("Business Strategy", "note"),
            ("Business Marketing", "note"),
            ("Entrepreneurship", "note"),
        ],
    },
    

    # ================= MORE EARNING WAYS =================
    "more_earning_ways": {
        "title": "More Earning Ways",
        "topics": [
            ("Freelancing", "note"),
            ("Consulting", "note"),
            ("Online Courses", "note"),
            ("Coaching & Mentorship", "note"),
            ("Blogging & Content Creation", "note"),
            ("Stock Market & Trading", "note"),
            ("Cryptocurrency Investing", "note"),
            ("Real Estate Investing", "note"),
            ("Dropshipping", "note"),
            ("Print on Demand", "note"),
            ("Membership Sites", "note"),
            ("Podcasting", "note"),
            ("Mobile App Monetization", "note"),
            ("YouTube Monetization", "youtube-monetization"),
            ("Affiliate Marketing", "note"),
        ],
    },
    
        
    # ================= AI & TOOLS =================
    "ai_tools": {
        "title": "AI Tools",
        "topics": [
            ("AI Basics Tools", "ai-basics"),
            ("APIs", "apis"),
            ("Generative AI", "note"),
            ("LLMs", "note"),
            ("AI Agents", "note"),
            ("Coding AI Tools", "note"),
            ("Design AI Tools", "note"),
            ("Video AI Tools", "note"),
            ("Productivity AI Tools", "note"),
            ("Automation Tools", "note"),
        ],
    },
    
    # ================= MORE IMPORTANT =================
    "more_imp": {
        "title": "More Important",
        "topics": [
            ("Time Management", "time-management"),
            ("Productivity Hacks", "productivity-hacks"),
            ("Work-Life Balance", "work-life-balance"),
            ("Continuous Learning", "continuous-learning"),
        ],
    },


    
    # ================= GET STARTED =================
    "get_started": {
        "title": "Just Click & Get Started",
        "topics": [
            ("How to Start Coding & Programming", "start-coding"),
            ("How to Find a Job", "find-job"),
            ("How to Start Social Media", "start-social-media"),
            ("How to Start a Business", "note"),
            ("How to Create Small Resources", "note"),
            ("More Getting Started Guides", "note"),
        ],
    },
    

    
}



def collection_language(request, lang="coding_languages", topic=None):
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
                topic_template = f"collection/{slug}.html"
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

    return render(request, "collection/study_dashboard.html", context)
