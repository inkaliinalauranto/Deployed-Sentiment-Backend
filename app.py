from flask import Flask, jsonify
from flask_cors import CORS
from controllers.sentiments import get_fake_sentiment, get_sentiment, hello_world

app = Flask(__name__)

# Sallitaan frontendin locahostin origin ja Renderissä käyttöönotettuun 
# versioon liittyvä origin:
# CORS(app, origins=["*"])

# app.add_url_rule(rule="/", view_func=hello_world)

# app.add_url_rule(rule="/api/fake-sentiment", view_func=get_fake_sentiment)

# app.add_url_rule(rule="/api/sentiment",
#                  view_func=get_sentiment,
#                  methods=["POST"])


@app.route("/")
def hello_world():
    return jsonify({"Message": "Hello world!"})

@app.route("/api/fake-sentiment")
def get_fake_sentiment():
    return jsonify({"result": "positive"})

# if __name__ == '__main__':
#     app.run(host="0.0.0.0", port="8080", debug=False)