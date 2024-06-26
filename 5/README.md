# Proyecto 5:

## Creación y gestión de un entorno virtual de Python, desarrollo de una aplicación web y su despliegue en un servicio en la nube [Render](https://render.com/) que la hará accesible al público.

##  El conjunto de datos original (notebooks/vehicles_us.csv), contiene la información para determinar el factores que influyen en el precio de un vehículo. Los campos que contiene son:

* price — precio del vehículo.
* model_year — año del modelo del vehículo.
* model — modelo del vehículo.
* condition — condición o estado en el que se encuentra el vehículo.
* cylinders — cilindros que tiene el vehículo.
* fuel — gasolina, diesel, etc.
* odometer — el millaje del vehículo cuando el anuncio fue publicado
* transmission — tipo de transmisión que tiene el vehículo.
* paint_color — color del vehículo.
* is_4wd — si el vehículo tiene tracción en las 4 ruedas (False=0, True=1)
* date_posted — la fecha en la que el anuncio fue publicado.
* days_listed — desde la publicación hasta que se elimina.

## Modificaciones a los datos (notebooks/EDA.ipynb):

1. Se remplazaron los valor asuntes
2. Se agruparon los vehículos por modelo
3. Se obtuvo el precio promedio del precio de los vehículos para diferentes modelo

Estas modificaciones se guardaron en el archivo **vehicles_us_filtered.csv**, que se utilizo para hacer la aplicación web

## Aplicación web:

1. Se graficó la información obtenida, utilizando la biblioteca de Python [plotly-express](https://plotly.com/python/plotly-express/)
2. Se creó una plicación web, utilizando las bibliotecas de Python [streamlit](https://streamlit.io/)
3. Se despliegue de la versión final de la aplicación en [proyecto5](https://proyecto5-g09k.onrender.com)