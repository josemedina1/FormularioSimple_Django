# formulario_Django
Creacion de un formulario simple (sin editar ni eliminar datos)
en conjunto a bases de datos SQLite3
para guardar la informacion del formulario

<a href="https://uiverse.io/Yaya12085/short-turtle-53">
    Estilos CSS utilizados para el Formulario
</a>
<img src="https://www.animatedimages.org/data/media/562/animated-line-image-0184.gif" width="1920" />

# Iniciar servidor Django
Dentro de la carpeta "formulario" se ejecuta el siguiente comando:
```
py manage.py runserver
```

<img src="https://www.animatedimages.org/data/media/562/animated-line-image-0184.gif" width="1920" />

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

```
mkdir -p /var/www/static
```

<img src="formulario/documents/img/load_static_dir.png" alt="">

<img src="https://www.animatedimages.org/data/media/562/animated-line-image-0184.gif" width="1920" />

# Crear APP
Se debe crear la aplicacion que contendrá el modelo de la base de datos
y donde se consumirá la base de datos mediante funciones y templates.
Utilizando el siguiente comando se crea la app, en este caso la app se llama CRUD:

```
    django-admin startapp crud
```

<img src="https://www.animatedimages.org/data/media/562/animated-line-image-0184.gif" width="1920" />

# Crear BD 

Luego de crear la app, dentro del archivo **models.py** 
se crea el modelo de la tabla que contendrá los datos del formulairo.

Al tener el modelo listo se debe crear la migracion del modelo hacia 
la base de datos utilizando los siguientes comandos:

```
    py manage.py makemigrations
```

```
    py manage.py migrate
```

<img src="formulario/documents/img/models.py.png" alt="">

<img src="https://www.animatedimages.org/data/media/562/animated-line-image-0184.gif" width="1920" />
