Manejo de Usuarios

Descripción

Este proyecto implementa el patrón DAO (Data Access Object) para interactuar con la tabla de usuarios en una base de datos. Se han implementado las operaciones básicas de CRUD
(Crear, Leer, Actualizar, Eliminar) utilizando Python y una conexión a la base de datos a través de un pool de conexiones. El proyecto está diseñado para gestionar la información de usuarios, como su nombre de 
usuario y contraseña, utilizando clases para representar los datos y ejecutar las consultas en la base de datos.


Tecnologías Utilizadas

Python: Lenguaje de programación principal.
POSTGRESQL: Base de datos para el almacenamiento de los usuarios.
Logging: Para el registro de eventos y depuración.
Conexión a la base de datos: Uso de un pool de conexiones para interactuar con la base de datos.


Características

CRUD completo: Implementa las operaciones de Crear, Leer, Actualizar y Eliminar para los registros de usuario.
Uso de pool de conexiones: Se utiliza un pool de conexiones para manejar la base de datos de forma eficiente.
Registro de actividades: Las operaciones son registradas mediante el uso de un logger para facilitar la depuración y el monitoreo.
Interfaz orientada a objetos: Cada usuario es representado por un objeto de la clase Usuario.


Requisitos Previos

Python 3.6 o superior
Base de datos POSTGRESQL
