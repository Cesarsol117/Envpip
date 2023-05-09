import utils                                                    # aca se importa el util donde se sacan los datos para la grafica
import read_csv                                                 # se importa la lectura del csv
import charts                                                   # se importa la funcion para la visualizacion de los datos
import pandas as pd
# importamos los modulos para los datos
'''
def run():                                                      #se llamma a la funcion para iniciar el programa
    data = read_csv.read_csv('world_population.csv')      # se llama la funcion read csv y se le envia la ubicacion del archivo y este retorna
                                                                # un diccionario que se almacena en data{}
    pais = input('Escriba un Pais => ')                         # un input para buscar el pais
    poblacion = utils.population_by_country(data, pais)         # de utils se envia la data que es un diccionario, y el nombre del pais en pais.
                                                                # devuelve poblacion que es una lista con un 
    if len(pais)>0:                                             # es par la verificacion de que encontro algo
        pais = poblacion[0]                                     # aca el pais se envia a la posicion cero de la lista que encontro
        keyes, values = utils.get_population(pais)              # aca se le envia a la funcion el dicionario del pais o lista y
                                                                # retorna solo dos valores,  las llaves y los valores de las llave.
        # print(keyes, values)
        charts.generate_bar_chart(pais['Country/Territory'], keyes, values)                # se envian las llaves y los valores a la funciopn que grafica

    print(poblacion)                                            #imprime la poblacion
# esta liena de codifo con el if es para que se ejecute el modulo sin necesidad de llamaarlo por medio de otra funcion.
if __name__ =='__main__':
        run()
# -------------------------------------------
'''
def run():
    df = pd.read_csv('world_population.csv')
    df = df[df['Continent'] == 'South America']
    countries = df['Country/Territory'].values
    percentages = df['World Population Percentage'].values
    charts.generate_pie_chart(countries, percentages)

    data = read_csv.read_csv('world_population.csv')
    country = input('Type Country => ')
    print(country)

    result = utils.population_by_country(data, country)

    if len(result) > 0:
        country = result[0]
        print(country)
        labels, values = utils.get_population(country)
        charts.generate_bar_chart(country['Country/Territory'], labels, values)

if __name__ == '__main__':
  run()