import products
def func():
    print('''Selecciona la opción:
a) Añadir producto
b) Eliminar producto
c) Vizualizar productos''')
    op3 = input("Ingresa la opción: ")
    if op3 == "a" or op3 == "A":
        print('''Selecciona la opción:
    a) Agregar Tintas
    b) Agregar Teclados
    c) Agregrar mouses''')

    func()
