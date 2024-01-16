# formulario_Django
Creacion de un formulario simple en conjunto a bases de datos 
para guardar la informacion del formulario

<a href="https://uiverse.io/Yaya12085/short-turtle-53">
    Estilos Formulario
</a>

# Iniciar servidor Django
```
py manage.py runserver
```

# Configuracion STATIC

Dentro del archivo **setings.py** se debe identificar la ruta **STATICFILES_DIRS**,
 se debe incluir las siguientes rutas de carga para nuestros archivos estaticos. 

```
STATICFILES_DIRS =[
    BASE_DIR / 'static',
    '/var/www/static',
]
```

Tambien se especifica la ruta para el Deploy de la aplicacion que se crea mediante el siguiente comando.

````
mkdir -p /var/www/static
```

<img src="formulario/documents/img/load_static_dir.png" alt="">

# Crear BD 
