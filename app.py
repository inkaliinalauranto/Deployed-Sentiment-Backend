from flask import Flask, jsonify#, request, jsonify
# from nlp import fitted_text_clf

app = Flask(__name__)

@app.route("/")
def hello_world():
    return jsonify({"Message": "Hello world!"})


# @app.route("/sentiment", methods=["POST"])
# def get_sentiment():
#     try:
#         input_data = request.json
#         text = input_data.get("text")
        
#         if not text:
#             return jsonify({"error": "Invalid request body"}), 400
        
#         result = fitted_text_clf.predict([text])[0]

#         return jsonify({"result": result})
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8080", debug=False)