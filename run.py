from application import create_app, db
from application import create_app
from sqlalchemy import text


app = create_app()

if __name__ == '__main__':
    app.run(debug=True, port=5001)