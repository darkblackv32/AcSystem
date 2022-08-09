# enter

passwords = []
users = ['patty','sandro','emilio']
print("Bienvenido a AcSystem")
print('''Por favor, selecciona una opción:
a) Ingresar
b) Registrarme''')
option = input('Oprime la tecla: ')
if option == "a" or option == "A":
    print("Usted es un usuario con una cuenta existente, por favor dígite su usuario y contraseña")
    user = input('User: ')
    password = input('Password: ')
    while password not in passwords or user not in users:
        print('Usuario y/o contraseña incorrecta, digíte nuevamente')
        user = input('User: ')
        password = input('Password: ')
if option == "b" or option == "B":
    print('Procederemos con el registro de su usuario en nuestra base de datos')
    a = input('Ingresa tu usuario: ')
    while a in users or len(a) < 5:
        print("Usuario no disponible, escoja otro, por favor (debe tener minimo 5 caracteres)")
        a = input('Ingresa tu usuario: ')
    users.append(a)
    b = input('Ingresa tu contraseña: ')
    dot = []
    for i in b:
        dot.append(i)
    while '1' not in dot and '2' not in dot and '3' not in dot and '4' not in dot and '5' not in dot and '6' not in dot and '7' not in dot and '8' not in dot and '9' not in dot and '0' not in dot or len(a) < 5:
        print('La contraseña debe contener números y tener 5 caracteres como minimo')
        b = input('Ingresa tu contraseña: ')
        for i in b:
            dot.append(i)
    passwords.append(b)
    
    
