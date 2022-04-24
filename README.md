# blogpersonal

_Ejemplo simple de un blog personal utilizando Python y Django, con una BD en sqlite3._

## Requerimientos
_Requerimientos para probar este ejemplo sencillo en Django._
* Crear un ambiente virtual.
    ```
    py -m venv env
    ```
* Iniciar el entorno virtual.
  * En windows
    ```
    env\Scripts\activate
    ```
  * En linux
    ```
    env\bin\activate
    ```
* Instalar librerías necesarias.
    ```
    pip install -r requirements.txt
    ```
## Pasos necesarios para ejecutar la aplicación.
> Nota: para revisar cada migración ejecutar las siguientes sentencias o pasar directo a ejecutar los comandos.

 ```
> py manage.py makemigrations perfil
# Despues puedes seleccionar del resultado arrojado la migracion para visualizar a detalle con el siguiente comando.
> py manage.py sqlmigrate perfil 0001

```

__Comandos__
```
py manage.py migrate blog
py manage.py migrate perfil
```

## Compilar aplicación.

```
py manage.py runserver
```