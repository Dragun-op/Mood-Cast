import os
import requests
from flask_login import current_user
from application import db
from application.models import UserTriggerCategory

TRIGGER_CATEGORIES = [
    "Anxiety", "Depression", "Loneliness", "Burnout", "Mood swings", "Intrusive thoughts",
    "Family conflict", "Friendship issues", "Romantic relationship problems", "Social isolation", "Rejection", "Peer pressure",
    "Job stress", "Career uncertainty", "Work-life imbalance", "Deadline pressure", "Lack of motivation",
    "Exam stress", "Poor grades", "Lack of concentration", "Academic burnout",
    "Low self-esteem", "Body image issues", "Identity crisis", "Fear of failure",
    "Debt", "Financial insecurity", "Lack of independence",
    "Sleep deprivation", "Unhealthy eating", "Overstimulation", "Lack of routine",
    "Chronic illness", "Fatigue", "Pain", "Medication side effects",
    "Feeling lost", "Lack of purpose", "Existential thoughts", "Major life changes"
]

ADVICE_MAP = {
    "Anxiety": "Practice deep breathing and grounding techniques. Consider a short walk or break.",
    "Depression": "Try to engage in a small activity you usually enjoy. Reaching out to someone helps.",
    "Loneliness": "Connect with a friend or online support group. You're not alone in this.",
    "Burnout": "Take a full break—mentally and physically. Set strict boundaries with work.",
    "Mood swings": "Track your patterns. Consider journaling or speaking to a therapist.",
    "Intrusive thoughts": "Acknowledge them without judgment. Practice mindfulness or consult a professional.",
    "Family conflict": "Open calm communication often helps. Give space if needed.",
    "Friendship issues": "Talk honestly or write a letter. Real friendships survive clarity.",
    "Romantic relationship problems": "Mutual respect and honest dialogue matter. Don’t ignore red flags.",
    "Social isolation": "Start small—just a message or smile. Community groups or online spaces help.",
    "Rejection": "You’re not defined by someone’s opinion. Reflect and move on kindly.",
    "Peer pressure": "Be true to your values. Real friends don’t push boundaries.",
    "Job stress": "Prioritize tasks. Break your work into smaller, achievable goals.",
    "Career uncertainty": "You’re allowed to explore. Learn and adapt at your pace.",
    "Work-life imbalance": "Define clear 'off' hours. Protect your personal time.",
    "Deadline pressure": "Use the Pomodoro technique. Don’t aim for perfection—aim for progress.",
    "Lack of motivation": "Start with 2-minute tasks. Action creates momentum.",
    "Exam stress": "Prepare in chunks. Reward yourself and rest often.",
    "Poor grades": "One result doesn’t define you. Seek help, reflect, and grow.",
    "Lack of concentration": "Try ambient music, or block distractions. Sleep matters more than you think.",
    "Academic burnout": "Take an intentional break. You need recovery to perform again.",
    "Low self-esteem": "List things you’re proud of. Even small ones. They matter.",
    "Body image issues": "You are more than how you look. Curate your social media mindfully.",
    "Identity crisis": "It’s okay to not have it all figured out. Explore without judgment.",
    "Fear of failure": "Every failure is feedback. Keep moving.",
    "Debt": "Break it into manageable parts. Seek financial literacy or a free counselor.",
    "Financial insecurity": "Budget with basics first. It’s okay to ask for help.",
    "Lack of independence": "Focus on small wins. Plan steps toward autonomy.",
    "Sleep deprivation": "Prioritize a routine. Reduce screens and stimulants at night.",
    "Unhealthy eating": "Start with hydration. Prepare simple, nourishing meals.",
    "Overstimulation": "Log off. Find a quiet, comforting space.",
    "Lack of routine": "Build anchor habits like meals, walk, or journaling.",
    "Chronic illness": "Pace yourself and celebrate progress. Ask for help when needed.",
    "Fatigue": "Your body isn’t weak—it’s signaling you. Prioritize sleep and nutrition.",
    "Pain": "Use a warm compress or rest. Gentle stretching helps.",
    "Medication side effects": "Speak to your doctor. Adjustments can make a difference.",
    "Feeling lost": "You’re not broken—just evolving. Journal your thoughts.",
    "Lack of purpose": "Volunteer or create. Purpose often emerges through action.",
    "Existential thoughts": "Big questions are human. Consider philosophical journaling or therapy.",
    "Major life changes": "Transitions are tough. Ground yourself with familiar routines.",
    "Uncategorized": "Take care of yourself. Reflect, breathe, and seek support."
}

def get_trigger_categories_with_advice(notes):
    from flask import current_app
    HF_API_KEY = current_app.config["HF_API_KEY"]

    headers = {
        "Authorization": f"Bearer {HF_API_KEY}"
    }

    payload = {
        "inputs": notes,
        "parameters": {
            "candidate_labels": TRIGGER_CATEGORIES,
            "multi_label": True
        }
    }

    response = requests.post(
        "https://api-inference.huggingface.co/models/facebook/bart-large-mnli",
        headers=headers,
        json=payload
    )
    result = response.json()

    top_categories = [
        (label, score)
        for label, score in zip(result["labels"], result["scores"])
        if score > 0.4
    ][:3]

    for label, score in top_categories:
        increment_user_trigger_count(current_user.id, label)

    return [
        {"category": label, "score": round(score, 2), "advice": ADVICE_MAP.get(label, "Take care of yourself.")}
        for label, score in top_categories
    ]


def increment_user_trigger_count(user_id, category):
    utc = UserTriggerCategory.query.filter_by(user_id=user_id, category=category).first()
    if utc:
        utc.count += 1
    else:
        utc = UserTriggerCategory(user_id=user_id, category=category)
        db.session.add(utc)
    db.session.commit()


def get_emotion_scores(text):
    from flask import current_app
    HF_API_KEY = current_app.config["HF_API_KEY"]

    headers = {
        "Authorization": f"Bearer {HF_API_KEY}"
    }

    response = requests.post(
        "https://api-inference.huggingface.co/models/j-hartmann/emotion-english-distilroberta-base",
        headers=headers,
        json={"inputs": text}
    )

    result = response.json()
    return sorted(result[0], key=lambda x: x["score"], reverse=True)