import scipy.stats as stats
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = pd.read_csv(r"Experimento_a.csv")
data2 = pd.read_csv(r"Experimento_b.csv")

print("""Hola, buen día ¿Cual de las siguientes quiere ver?
      1: significancia entre medias.
      2: Correlaciones de Pearson y Spearman de los datos.
      3: Diagrama de dispersion con regresion lineal
      4. Cancelar y salir""")


while(True):
    opcion=input("Ingrese el numero de la opcion de su preferencia")


    if opcion == "1":
        #INCISO A
        mean1=data["V1"].mean()
        print("La media es Exp_A es",mean1)
        mean2=data2["V1"].mean()
        print("La media es Exp_A es",mean2)

    #realice dos pruebas t de muestra con varianzas iguales
        pruebaT=stats.ttest_ind (data["V1"], data2["V1"],)
        print(pruebaT)

    if opcion =="2":
        #INCISO B
        print('La correlación de Pearson es igual: ', data['V1'].corr(data2['V1'], method='pearson'))
        print('La correlación de spearman es igual: ', data['V1'].corr(data2['V1'], method='spearman'))

    if opcion == "3":
    #INCISO C

        df = pd.DataFrame(data, columns = ['V1'])
        my_array = df.values

        df = pd.DataFrame(data2, columns = ['V1'])
        my_array2 = df.values

        plt.scatter(my_array,my_array2, label = 'scatter')
        linreg = LinearRegression()
        linreg.fit(my_array,my_array2)  # Ajuste de regresión
        y_pred = linreg.predict(my_array) # Ingrese los datos de Yuanshu en el modelo para obtener el valor predicho
        plt.plot(my_array, y_pred, 'r', label = 'plot')  # Dibuja un gráfico de líneas
        plt.legend()
        plt.show()

    if opcion == "4":
        print("Muchas gracias. Adios.")
        break

    else:
        print("INGRESE UN VALOR CORRECTO")