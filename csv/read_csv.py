import csv
def read_csv(path):
    with open(path, 'r') as archivo:
        lector = csv.reader(archivo, delimiter=',')
        cabecera = next(lector)
        # print(cabecera)
        data = []
        for fila in lector:
            iterable = zip(cabecera, fila)
            dict_pais = {key:value for key, value in iterable }
            # print('***'*5)
            # print(list(iterable))
            data.append(dict_pais)
        return data

if __name__ == '__main__':
   data= read_csv('./app/world_population.csv')
   print(data[0])