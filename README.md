# 🧠 MoodCast – Predictive Mood Calendar & Mental Health Tracker

**MoodCast** is a web app that helps students, developers, and everyday users track their moods, discover emotional patterns, and receive personalized suggestions to improve mental wellbeing. With a privacy-first design and integrated AI analysis, MoodCast empowers users to reflect, grow, and take early action before stress and burnout escalate.

---

## 🚀 Features

- 📝 Log your daily mood with notes, intensity, tags, and emotion types
- 📅 GitHub-style mood heatmap to visualize patterns over time
- 🧠 AI-powered trigger detection using zero-shot classification
- 🎯 Personalized advice tailored to your emotional context
- 📊 Dashboard with recent analyses and common trigger categories
- 👥 Trusted-sharing mode with secure token-based access
- 📜 Mood history with search, filter, and sorting options
- ⚠️ Emotion score detection to identify critical moods (coming soon)

---

## 🛠 Tech Stack

| Layer         | Technology Used                                  |
|---------------|--------------------------------------------------|
| Backend       | Flask (Python), Flask-SQLAlchemy, Flask-Login    |
| Database      | PostgreSQL                                       |
| NLP/AI        | Hugging Face Transformers (`bart-large-mnli`)    |
| Frontend      | Jinja2, HTML/CSS, Bootstrap (SB Admin 2), JS     |
| Visualization | Apache ECharts                                   |
| Deployment    | Render / Railway                                 |

---

## 📁 Folder Structure

```bash
📁 MoodCast/
├── application/
│   ├── __init__.py
│   ├── models.py
│   ├── auth/
│   │   ├── forms.py
│   │   └── routes.py
│   ├── mood/
│   │   ├── forms.py
│   │   ├── nlp_advice.py
│   │   └── routes.py
├── static/
│   ├── css/
│   │   ├── custom.css
│   │   └── sb-admin-2.min.css
│   ├── icon/
│   │   ├── favicon.ico
│   │   └── favicon.png
│   ├── js/
│   │   ├── heatmap.js
│   │   └── sb-admin-2.min.js
│   └── vendor/
│       ├── bootstrap/
│       ├── chart.js/
│       ├── datatables/
│       ├── fontawesome-free/
│       ├── jquery/
│       └── jquery-easing/
├── templates/
│   ├── base.html
│   ├── landing.html
│   ├── auth/
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── forgot_password.html
│   │   └── reset_password.html
│   ├── mood/
│   │   ├── dashboard.html
│   │   ├── heatmap.html
│   │   ├── history.html
│   │   ├── log_mood.html
│   │   ├── shared_view.html
│   │   └── triggers.html
│   ├── errors/
│   │   ├── 404.html
│   │   └── 500.html
│   └── partials/
│       ├── _sidebar.html
│       ├── _topbar.html
│       └── _footer.html
├── .env
├── .flaskenv
├── .gitignore
├── config.py
├── requirements.txt
├── README.md
├── run.py
└── venv/  

---

## 🧰 Setup Instructions

    1️⃣ Clone the Repository

        git clone https://github.com/yourusername/moodcast.git
        cd moodcast

    2️⃣ Create a Virtual Environment

        # Windows
        python -m venv venv
        venv\Scripts\activate

        # macOS/Linux
        python3 -m venv venv
        source venv/bin/activate

    3️⃣ Install Required Packages

        pip install -r requirements.txt
    
    4️⃣ Setup Environment Variables

        Create a .env file in the root directory:
        SECRET_KEY=your_secret_key
        DATABASE_URL=postgresql://username:password@localhost:5432/moodcast

        Also create .flaskenv:
        FLASK_APP=run.py
        FLASK_ENV=development

    5️⃣ Start PostgreSQL and Create the Database

        # Login to PostgreSQL
        psql -U yourusername

        # Inside psql
        CREATE DATABASE moodcast;
    
    6️⃣ Initialize the Database

        flask shell
        >>> from application import create_app, db
        >>> app = create_app()
        >>> with app.app_context():
        ...     db.create_all()

    7️⃣ Run the Application
        
        flask run

---

## 📌 Future Enhancements

    ⏱ Weekly mood summary reports with visualizations

    🧠 Fine-tuned transformer models for better emotion detection

    🧩 User feedback loop for improving advice suggestions

    📱 Mobile-responsive layout improvements

    🧪 Admin analytics dashboard

---