# se cambia el nombre a utils porque es mas parecido a la lo que se uttiliaa en la vida real

def get_population(dict_pais):                                    # se crea una funcion con que recibe un diccionaro como parametro
    population_dict = {                                           # se crea el dicionario que contiene las llaves y valores que se van a requerir
        '2022': int(dict_pais['2022 Population']),                # se añade manualmente las keys es decir los años                     
        '2020': int(dict_pais['2020 Population']),                # se convierte en etero y en cada valor se accede al dicicionario y se se le 
        '2015': int(dict_pais['2015 Population']),                # dice que nos traiga solo lo que hay en la columna ['xxxx pupulation']
        '2010': int(dict_pais['2010 Population']),                # 
        '2000': int(dict_pais['2000 Population']),                # 
        '1990': int(dict_pais['1990 Population']),                # 
        '1980': int(dict_pais['1980 Population']),                # 
        '1970': int(dict_pais['1970 Population']),                # 
    }
    keyes = population_dict.keys()                                # con una funciion de  los diccionarios se sustrae las keys llamando 
                                                                  # a la varible que contiene el diccionario y la funcion .keys()
    values = population_dict.values()                             # lo mismo pero ahora con la funcion .values()
    return keyes, values                                          # se retorna las llaves y valores en forma de lista

def population_by_country(data, country):                                               #se crea una funcion que recibe el diccionario y el pais 
    result = list(filter(lambda cosa:  cosa['Country/Territory'] == country, data ))    # se usa una funcion filter que tiene anidada
                                                                                        #una funcion lambda que la varaible cosa va extraer
                                                                                        # lo que haya en country, y ese country lo va a filtrar 
                                                                                        # en la data y lo va a guardar en forma de lista
    return result                                                                       # y lo envia al result