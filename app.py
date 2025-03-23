from flask import Flask
from flask_cors import CORS
from controllers.sentiments import get_sentiment, hello_world

app = Flask(__name__)

CORS(
    app,
    origins=[
        "http://localhost:5500",
        "https://kind-forest-04e83171e.6.azurestaticapps.net:8080",
        "https://deployed-sentiment-analysis-frontend.onrender.com:10000",
    ],
    supports_credentials=True,
)

app.add_url_rule(rule="/", view_func=hello_world)

app.add_url_rule(rule="/api/sentiment", view_func=get_sentiment, methods=["POST"])

# if __name__ == '__main__':
#     app.run(host="0.0.0.0", port="8080", debug=False)
