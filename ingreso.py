# enter
passwords = []
users = []
print("Bienvenido a AcSystem")
print('''Por favor, selecciona una opción:
a) Ingresar
b) Registrarme''')
option = input('Oprime la tecla: ')
if option == "a" or option == "A":
    print("Usted es un usuario con una cuenta existente, por favor dígite su usuario y contraseña")
    user = input('User: ')
    password = input('Password: ')
    while password not in passwords and user not in users:
        print('Usuario y/o contraseña incorrecta, digíte nuevamente')
        user = input('User: ')
        password = input('Password: ')
if option == "b" or option == "B":
    print('Procederemos con el registro de su usuario en nuestra base de datos')
    a = input('Ingresa tu usuario: ')
    users.append(a)
    b = input('Ingresa tu contraseña: ')
    passwords.append(b)