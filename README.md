# 🧠 MoodCast – Predictive Mood Calendar & Mental Health Tracker

**MoodCast** is a web app that helps students, developers, and everyday users track their moods, discover emotional patterns, and receive personalized suggestions to improve mental wellbeing. With a privacy-first design and AI-ready structure, MoodCast empowers users to take early action before stress and burnout escalate.

---

## 🚀 Features

- 📝 Daily mood logging with notes, tags, and emotion emojis
- 📅 Mood heatmap calendar to visualize emotional trends
- 🧠 AI-ready logic to identify mood triggers and recurring patterns
- 🎯 Personalized suggestions based on user feedback
- 🧾 Weekly summaries for emotional reflection
- 👥 Trusted-sharing mode for friends/family (optional)
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
| Deployment    | Render / Railway (recommended) |

---

## 📁 Folder Structure

MoodCast/
├── run.py
├── config.py
├── .env
├── .flaskenv
├── requirements.txt
├── README.md
├── app/
│ ├── init.py
│ ├── models.py
│ ├── auth/
│ │ └── routes.py
│ ├── mood/
│ │ └── routes.py
│ ├── templates/
│ │ ├── auth/
│ │ │ └── login.html
│ │ └── mood/
│ │ └── calendar.html
│ └── static/
│ └── (css/js/icons)

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