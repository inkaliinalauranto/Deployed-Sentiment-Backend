import pickle
from sklearn.pipeline import Pipeline

fitted_text_clf: Pipeline = None

# Avataan serialisoidun koulutetun analyysimallin sisällään pitämä tiedosto:
with open("./data/fitted_text_clf.pkl", "rb") as f:
    # Deserialisoidaan tiedoston sisältö ja tallennetaan koulutusmalli 
    # aiempana alustettuun muuttujaan:
    fitted_text_clf = pickle.load(f)
    f.close()