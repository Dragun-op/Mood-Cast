from application import create_app, db
from application import create_app
from sqlalchemy import text


app = create_app()

@app.route('/init-db')
def init_db():
    with app.app_context():
        db.create_all()
    return "✅ Database initialized!"

if __name__ == '__main__':
    app.run( port=5001)