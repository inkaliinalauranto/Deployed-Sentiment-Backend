FROM python:3.12
WORKDIR /usr/src/app

# Flask-kehyksen sisäänrakennetut ympäristömuuttujat: 
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_DEBUG=1
ENV FLASK_RUN_PORT=8080

# Kirjastoja gcc:sta lähtien tarvitaan, jotta scikit-learn-kirjasto asentuu
# Linux Alpine -ympäristöön oikein:
# Lähde: https://github.com/scikit-learn/scikit-learn/issues/27644
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8080
COPY . .
CMD ["flask", "run"]