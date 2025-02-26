from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello World! V3.1 PROD</h1>"


@app.route("/sentiment", methods=["POST"])
def get_sentiment():
    input_data = request.json
    print(input_data)

    # Tehtävänä on sentiment-analyysin tekeminen tähän
    # Otetaan se tähän.
    # Sen voi tuoda colabista Pythonin pickelin avulla. Se on 
    # object serialization -kirjasto. Se on pythonin oma tapa 
    # serialisoida objekti. Eli ei haluta joka kerta tässä kouluttaa.
    # Se voidaan Pipeline tallentaa ja sen voi loadata pickellä, koska
    # scikit learnilla ei ole kätevää tapaa tähän. Pitäisi olla parin 
    # rivin juttu.

    return {"input_data": input_data}

if __name__ == '__main__':
    # Nyt annettava porttimäärittely --> Miksi? --> Sallitaan backendin 
    # käyttäjien tulevan muistakin IP-osoitteista, kuin localhostista
    # Portiksi 8080, koska käytetään Python 3.9-templatea. Rahdin päässä
    # sitä käytetään myös oletuksena siitä, missä backend on. 
    # Palomuuri voi joissain tapauksissa blockata. debug Falseksi 
    # tuotantopuoleen. Mutta debug-mode halutaan localhostin testaamisessa, 
    # joten tässä astuu kuvioon se, miten tämä voidaan vaihtaa envin kautta.
    app.run(host="0.0.0.0", port="8080", debug=False)