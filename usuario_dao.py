from laboratorio_usuarios.cursor_del_pool import CursorDelPool
from laboratorio_usuarios.logger_base import log
from laboratorio_usuarios.usuario import Usuario


class UsuarioDAO:
    '''
    DAO - Data Access Object para la tabla de Usuario
    CRUD - Create- Read - Update - Delete para la tabla de usuario
    '''

    _SELECT = 'SELECT * FROM usuario ORDER BY id_usuario'
    _INSERTAR = 'INSERT INTO usuario (username,password) VALUES(%s, %s)'
    _ACTUALIZAR = 'UPDATE usuario SET username=%s, password=%s WHERE id_usuario=%s'
    _ELIMINAR = 'DELETE FROM usuario WHERE id_usuario=%s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            log.debug('Seleccionando usuarios')
            cursor.execute(cls._SELECT)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuario = Usuario(registro[0], registro[1], registro[2])
                usuarios.append(usuario)
            return usuarios

    @classmethod
    def insertar(cls, usuario):
        with CursorDelPool() as cursor:
            log.debug(f'Usuario a insertar: {usuario}')
            valores = (usuario.username, usuario.password)
            cursor.execute(cls._INSERTAR, valores)
            return cursor.rowcount
    @classmethod
    def actualizar(cls, usuario):
        with CursorDelPool() as cursor:
            log.debug(f'Usuario a actualiza {usuario}')
            valores = (usuario.username, usuario.password, usuario.id_usuario)
            cursor.execute(cls._ACTUALIZAR, valores)
            return cursor.rowcount

    @classmethod
    def eliminar(cls, usuario):
        with CursorDelPool() as cursor:
            log.debug(f'Usuario a eliminar {usuario}')
            valores = (usuario.id_usuario,)
            cursor.execute(cls._ELIMINAR, valores)
            return cursor.rowcount

if __name__ == '__main__':
    # Insertar un registro
    #usuario1 = Usuario(username='mcordo18', password='010489')
    #usuarios_insertados = UsuarioDAO.insertar(usuario1)
    #log.debug(f'Usuarios insertados {usuarios_insertados}')

    # Actualizar registro
    #usuario1 = Usuario(username='mcordo11', password='78945', id_usuario=3)
    #usuarios_actualizados = UsuarioDAO.actualizar(usuario1)
    #log.debug(f'Usuarios actualizados {usuarios_actualizados}')

    #Eliminar registro
    usuario1 = Usuario(id_usuario=3)
    usuario_eliminados = UsuarioDAO.eliminar(usuario1)
    log.debug(f'Usuario eliminado {usuario_eliminados}')

    # Seleccionar Objetos
    usuarios = UsuarioDAO.seleccionar()
    for usuario in usuarios:
        log.debug(usuario)
