from flask_mail import Message
from application import mail
from flask import url_for, current_app

def send_reset_email(user):
    token = user.generate_reset_token()
    reset_url = url_for('auth.reset_password', token=token, _external=True)
    msg = Message('Password Reset - MoodCast',
                  recipients=[user.email])
    msg.body = f'''Hi {user.username},

To reset your password, click the following link:

{reset_url}

If you did not request this, simply ignore this email.

Regards,
MoodCast Team
'''
    mail.send(msg)