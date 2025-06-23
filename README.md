# 🧠 MoodCast – Predictive Mood Calendar & Mental Health Tracker

**MoodCast** is a web app that helps students, developers, and everyday users track their moods, discover emotional patterns, and receive personalized suggestions to improve mental wellbeing. With a privacy-first design and AI-ready structure, MoodCast empowers users to take early action before stress and burnout escalate.

---

## 🚀 Features

- 📝 Daily mood logging with notes, tags, and emotion emojis
- 📅 Mood heatmap calendar to visualize emotional trends
- 🧠 AI-ready logic to identify mood triggers and recurring patterns
- 🎯 Personalized suggestions based on user feedback
- 🧾 Weekly summaries for emotional reflection
- 👥 Trusted-sharing mode for friends/family 
- 🚨 Crisis detection system to prompt professional help when needed

---

## 🛠 Tech Stack

| Layer         | Technology Used                |
|---------------|-------------------------------|
| Backend       | Flask (Python)                |
| Database      | PostgreSQL + SQLAlchemy       |
| Authentication| Flask-Login                   |
| Frontend      | HTML, CSS, Jinja2             |
| Optional AI   | scikit-learn / transformers   |
| Deployment    | Render / Railway               |

---

## 📁 Folder Structure

```bash
MoodCast/
├── application/
│   ├── __init__.py
│   ├── models.py
│   ├── auth/
│   │   └── routes.py
│   ├── mood/
│   │   └── routes.py
│   ├── static/
│   │   ├── css/
│   │   │   ├── custom.css
│   │   │   └── sb-admin-2.min.css
│   │   ├── js/
│   │   │   ├── heatmap.js
│   │   │   └── sb-admin-2.min.js
│   │   ├── img/
│   │   ├── icon/
│   │   └── vendor/              
│   └── templates/
│       ├── base.html
│       ├── landing.html
│       ├── auth/
│       │   ├── login.html
│       │   ├── register.html
│       │   └── forgot_password.html
│       ├── mood/
│       │   ├── log_mood.html
│       │   ├── heatmap.html
│       │   ├── dashboard.html
│       │   └── insights.html
│       ├── errors/
│       │   ├── 404.html
│       │   └── 500.html
│       └── partials/
│           ├── _sidebar.html
│           ├── _topbar.html
│           └── _footer.html
├── run.py
├── config.py
├── .flaskenv
├── .env
├── requirements.txt
├── README.md
```


## 🧰 Setup Instructions

1️⃣ Clone the Repository
   ```bash
   git clone https://github.com/yourusername/moodcast.git
   cd moodcast

2️⃣ Create Virtual Environment

    On Windows:
    python -m venv venv
    venv\Scripts\activate

    On Linux/macOS:
    python3 -m venv venv
    source venv/bin/activate

3️⃣ Install Dependencies

    pip install -r requirements.txt

4️⃣ Set Environment Variables
    
    Create a .env file in the root:
    SECRET_KEY=your_secret_key
    DATABASE_URL=postgresql://username:password@localhost:5432/moodcast

    Also create .flaskenv:
    FLASK_APP=run.py
    FLASK_ENV=development

5️⃣ Start PostgreSQL & Create the Database
    
    Ensure PostgreSQL is running, then:
    psql -U yourusername
    CREATE DATABASE moodcast;

6️⃣ Initialize the Database in Flask

        flask shell
    >>> from app import create_app, db
    >>> app = create_app()
    >>> with app.app_context(): db.create_all()

7️⃣ Run the Application

    flask run

!!!!!