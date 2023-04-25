import matplotlib.pyplot as plt                     #se llama la libreria para graficar y se utiliza un namespace plt

def generate_bar_chart(name,labels, values):             #se crea un a funcion que va crear una imagen de barras, recibe las labels y valores
    fig, ax = plt.subplots()                        # se crean dos variables que contienen los subplots de la libreria 
    ax.bar(labels, values)                          # se le envian a ax la funcion bar que es de barras y se le envian los parametros de la funcion    
    plt.savefig(f'./img/{name}.png')
    plt.close()                                      # con la funcion.show se llama para que lo muestre en forma de barras
    
def generate_pie_chart(labels, values):             
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plt.savefig('pie.png')
    plt.close()
    
if __name__ == '__main__':                          # para que la funcion se ejecute cuando sea llamada por la terminal
    labels = ['a', 'b','c']                         #valores para la prueba
    values = [100, 200, 30]                         # Valores para la prueva
    # generate_bar_chart(labels, values)            # se llama la funcion y se le envia los argumentos que son los valores de prueba.
    generate_pie_chart(labels, values)
