#To Do project

## Inicio

El proyecto consta de un backend realizado con Django con las siguientes rutas disponibles:

-/ (home)
- admin/
- signin/
- signup/
- notes/
- notes/<int:note_id>/
- notes/<int:note_id>/complete
- notes/<int:note_id>/delete
- notes/create/
- logout/
- login/

## Requeriments

asgiref                  3.5.2
Django                   4.1.4
django-babel-transpiling 0.3.2
pip                      22.2.2
py-mini-racer            0.6.0
setuptools               63.2.0
sqlparse                 0.4.3
tzdata                   2022.7
whitenoise               6.2.0

## Detalles

Se diseño sin el uso de REST framework donde cada endpoint permite realizar el registro e inicio de sesion de usuarios
y el registro, modificacion, consulta y eliminacion de notas de cada usuario con la debida proteccion de cada ruta

Por cuestiones de dificultades con la integracion de archivos estaticos compilados con babel para el uso de componentes de react,
sin embargo el componente de nota fue diseñado de todas formas y se simulo la obtencion de datos de la api mediante
JSON Placeholder usando el hook de efecto para demostrar la comprension de conceptos
