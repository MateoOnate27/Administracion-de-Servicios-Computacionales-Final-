# train.py
import pickle
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import os

def train():
    print("Cargando datos...")
    iris = load_iris()
    X, y = iris.data, iris.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    print("Entrenando modelo...")
    model = RandomForestClassifier(n_estimators=10)
    model.fit(X_train, y_train)

    # Creamos la carpeta donde se guardará el modelo si no existe
    os.makedirs('/mnt/model', exist_ok=True)
    
    print("Guardando modelo en /mnt/model/model.pkl...")
    with open('/mnt/model/model.pkl', 'wb') as f:
        pickle.dump(model, f)
    
    print("¡Entrenamiento completado exitosamente!")

if __name__ == "__main__":
    train()
