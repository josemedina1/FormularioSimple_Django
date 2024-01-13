# formulario_Django
Creacion de un formulario simple en conjunto a bases de datos 
para guardar la informacion del formulario



# Configuracion STATIC

Al identificar el directorio 'static', se debe incluir las siguientes rutas de carga para nuestros archivos estaticos. Tambien se especifica la ruta para el Deploy de la aplicacion.

```
STATICFILES_DIRS =[
    BASE_DIR / 'static',
    '/var/www/static',
]
```