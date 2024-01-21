### Guía de Instalación de Django y Paquetes Relacionados para CargaFacil

#### Requisitos Previos
- Asegúrate de tener Python instalado en tu sistema. Django requiere Python 3.6 o superior.
- Es recomendable usar un entorno virtual para mantener las dependencias del proyecto aisladas.

#### Pasos para la Instalación

1. **Instalación de Django**
   - Abre una terminal o línea de comandos.
   - Escribe `pip install Django` y presiona Enter.
   - Esto instalará la última versión de Django.

2. **Instalación de django-request**
   - En la misma terminal, escribe `pip install django-request`.
   - Este paquete permite manejar fácilmente los datos de las solicitudes HTTP en Django.

3. **Instalación de Django REST Framework**
   - Escribe `pip install djangorestframework`.
   - Django REST Framework es una potente herramienta para construir APIs web.

4. **Instalación de Crispy Bootstrap 4**
   - Escribe `pip install crispy-bootstrap4`.
   - Este paquete te ayudará a integrar formularios de Django con Bootstrap 4.

5. **Instalación de Django CORS Headers**
   - Finalmente, instala los CORS Headers con `python -m pip install django-cors-headers`.
   - Esto es útil para manejar los Cross-Origin Resource Sharing (CORS) en proyectos de Django, especialmente en APIs.

#### Verificación

- Para verificar que todo esté instalado correctamente, puedes ejecutar el servidor de desarrollo de Django con `python manage.py runserver` y verificar que no hay errores.

#### Documentación Adicional

- Para más detalles, consulta la documentación oficial de cada paquete:
  - [Django](https://www.djangoproject.com/)
  - [Django REST Framework](https://www.django-rest-framework.org/)
  - [Crispy Bootstrap 4](https://django-crispy-forms.readthedocs.io/en/latest/install.html#bootstrap4-install)
  - [Django CORS Headers](https://github.com/adamchainz/django-cors-headers)

Esta guía te proporciona una base sólida para comenzar a trabajar con Django y los paquetes adicionales que has mencionado.
