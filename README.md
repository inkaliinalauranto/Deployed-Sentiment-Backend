# Deployed-Sentiment-Backend

Backend sisältää web-ohjelmointirajapintafunktioita, joiden kautta backendin tietokantaan on mahdollista toteuttaa CRUD-operaatioita. 

Päätason endpoint on https://sentiment-backend-private-git-deployed-sentiment-analysis.2.rahtiapp.fi.

Web-API-pyynnön URL muodostetaan lisäämällä päätason endpointin perään pyynnön resurssi-/endpoint-pääte.

Rajapintapyynnöt toteutetaan alla olevan taulukon mukaisesti:


| Toiminto (CRUD)                            | HTTP-metodi | Endpointin pääte     | JSON body                               | Token vaaditaan Authorization headeriin  |
|:-------------------------------------------|:------------|:---------------------|:----------------------------------------|:-----------------------------------------|
| Käyttäjän luominen (C)                     | POST        | /api/register        | username- ja password-avaimet arvoineen | Ei                                       |
| Käyttäjän omien tietojen hakeminen (R)     | GET         | /api/account         | Ei                                      | Kyllä                                    |
| Käyttäjän oman salasanan päivittäminen (U) | PATCH       | /api/change-password | password-avain arvoineen                | Kyllä                                    |
| Käyttäjän itsensä poistaminen (D)          | DELETE      | /api/remove          | Ei                                      | Kyllä                                    |
| Sisäänkirjautuminen                        | POST        | /api/login           | username- ja password-avaimet arvoineen | Ei                                       |
| Tunneanalyysin toteuttaminen syötteelle    | POST        | /api/sentiment       | text-avain arvoineen                    | Kyllä                                    |



Rajapintaa hyödyntää sille tehty frontend, joka on otettu käyttöön sekä [Renderissä](https://deployed-sentiment-analysis-frontend.onrender.com/) että [Azuressa](https://kind-forest-04e83171e.6.azurestaticapps.net/).

## Esimerkit

POST-web-API-tunneanalyysifunktion toiminta rajapintatyökalun kautta:
![Esimerkkikuva POST-funktion toiminnasta](./images/api_demo.png)

POST-web-API-tunneanalyysiresurssin hyödyntäminen Azuren kautta käyttöönotetussa frontendissa:
![Esimerkkikuva backendia hyödyntävän käyttöönotetun frontendin alkunäkymästä](./images/deployed_frontend_start.png)

![Esimerkkikuva backendia hyödyntävän käyttöönotetun frontendin loppunäkymästä](./images/deployed_frontend_end.png)
