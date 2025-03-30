from flask import jsonify, request
from nlp import fitted_text_clf
from tools.require_user import require_user


def hello_world():
    return jsonify({"Message": "Hello world! Muokattu2"})


def get_sentiment():
    try:
        require_user(request)

        input_data = request.json
        text = input_data.get("text")

        if not text:
            return jsonify({"error": "Invalid request body"}), 400

        result = fitted_text_clf.predict([text])[0]

        return jsonify({"result": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
