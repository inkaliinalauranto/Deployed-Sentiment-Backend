from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from controllers.sentiments import get_sentiment, hello_world
from controllers.users import get_users, register, login, get_logged_in_user, remove_logged_in_user, \
    change_password_for_logged_in_user
from models import Base
from init_db import engine

# Ladataan ympäristömuuttujat:
load_dotenv()

# Luodaan tietokantataulut, jos niitä ei vielä ole:
Base.metadata.create_all(bind=engine)

# Alustetaan Flask-luokan instanssi:
app = Flask(__name__)

# Määritellään, miltä verkkotunnuksilta backendin API-resursseihin on pääsy:
CORS(
    app,
    origins=[
        "http://localhost:5173",
        "http://localhost:5500",
        "https://kind-forest-04e83171e.6.azurestaticapps.net",
        "https://deployed-sentiment-analysis-frontend.onrender.com",
    ],
)

app.add_url_rule(rule="/", view_func=hello_world)
app.add_url_rule(rule="/api/sentiment", view_func=get_sentiment, methods=["POST"])

app.add_url_rule(rule="/api/users", view_func=get_users)
app.add_url_rule(rule="/api/account", view_func=get_logged_in_user)

app.add_url_rule(rule="/api/register", view_func=register, methods=["POST"])
app.add_url_rule(rule="/api/login", view_func=login, methods=["POST"])
app.add_url_rule(rule="/api/change-password", view_func=change_password_for_logged_in_user, methods=["PATCH"])
app.add_url_rule(rule="/api/remove", view_func=remove_logged_in_user, methods=["DELETE"])

# if __name__ == '__main__':
#     app.run(host="0.0.0.0", port="8080", debug=False)
