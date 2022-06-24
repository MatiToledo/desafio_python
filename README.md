# URL Heroku

https://desafio-python-coder.herokuapp.com/

# Instrucciones para ejecutar este proyecto

- Clonar el proyecto y cambiar de rama
```bash
git clone git@github.com:MatiToledo/desafio_python.git

cd desafio_python

```

- Crear y activar entorno virtual (Windows)
```bash
C:\>python -m venv c:\ruta\al\entorno\virtual
C:\>c:\ruta\al\entorno\virtual\scripts\activate.bat
```

- Crear y activar entorno virtual (Linux)
```bash
python3 -m venv venv
source venv/bin/activate
```

- Crear y activar entorno virtual (Linux)
```bash
export SECRET_KEY='django-insecure-)*rmd&=9b)43d!j25y=xym@uts)-i(x*^(gs4w=v%!z+!q9o=m'
export DEBUG='True'
export ALLOWED_HOSTS='*,'
```
o crear el archivo `coderhouse_project/.env` con el siguente contenido
```text
SECRET_KEY=django-insecure-)*rmd&=9b)43d!j25y=xym@uts)-i(x*^(gs4w=v%!z+!q9o=m
DEBUG=True
ALLOWED_HOSTS=*,
```

- Instalar las dependencias del proyecto
```bash

pip install -r requirements.txt
```

- Crear base de datos a partir de las migraciones
```bash
python manage.py migrate
```

- Crear super-usuario
```bash
python manage.py createsuperuser
```


- Crear estáticos
```bash
python manage.py collectstatic
```

- Ejecutar proyecto
```bash
python manage.py runserver
```
