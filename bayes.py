# Importar la libreria

from sklearn.naive_bayes import GaussianNB


# Entrenamiento del algoritmo

modelo_nb = GaussianNB()

modelo_nb.fit(x_entrenamiento, y_entrenamiento)


# Predicciones de algoritmos para el conjunto de datos de prueba

prediccion = modelo_nb.predict(x_prueba)
