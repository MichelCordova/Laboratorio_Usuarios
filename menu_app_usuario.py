from laboratorio_usuarios.usuario_dao import UsuarioDAO
from laboratorio_usuarios.logger_base import log
from laboratorio_usuarios.usuario import Usuario

opcion = None

while opcion != 5:
    print('Opciones:')
    print('1 Listar Usuarios')
    print('2 Agregar Usuarios')
    print('3 Modificar Usuarios')
    print('4 Eliminar usuarios')
    print('5 Salir')
    opcion = int(input('Escribe tu opcion (1-5): '))

    if opcion == 1:
        usuarios = UsuarioDAO.seleccionar()
        for usuario in usuarios:
            log.info(usuario)
    elif opcion == 2:
        username_var = input('Escribe el username: ')
        password_var = input('Escribe el password: ')
        usuario = Usuario(username=username_var, password=password_var)
        usuarios_insertados = UsuarioDAO.insertar(usuario)
        log.info(f'Usuario insertados: {usuarios_insertados}')

    elif opcion == 3:
        id_usuario_var = int(input('Escribe el id_usuario a modificar: '))
        username_var = input('Escribe el username: ')
        password_var = input('Escribe el password: ')
        usuario = Usuario(id_usuario_var, username_var, password_var)
        usuarios_actualizados = UsuarioDAO.actualizar(usuario)
        log.info(f'Usuario actualizados: {usuarios_actualizados}')

    elif opcion == 4:
        id_usuario_var = int(input('Escribe el id_usuario a eliminar: '))
        usuario = Usuario(id_usuario=id_usuario_var)
        usuarios_eliminados = UsuarioDAO.eliminar(usuario)
        log.info(f'Usuarios Eliminados: {usuarios_eliminados}')

else:
    log.info('SALIMOS DE LA APLICACION')