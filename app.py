from flask import Flask
from flask_cors import CORS
from controllers.sentiments import get_sentiment, hello_world

app = Flask(__name__)

# Sallitaan frontendin locahostin origin ja Renderissä käyttöönotettuun 
# versioon liittyvä origin:
CORS(app)

app.add_url_rule(rule="/sentiment", view_func=hello_world)

app.add_url_rule(rule="/",
                 view_func=get_sentiment,
                 methods=["POST"])

# if __name__ == '__main__':
#     app.run(host="0.0.0.0", port="8080", debug=False)