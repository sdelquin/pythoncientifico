# Curso de Python Científico

Curso de Python Científico planteado para impartirlo en 20 horas presenciales con los siguientes objetivos:

- Introducir el entorno interactivo **Jupyter Notebook** para escribir código y ejecutarlo.
- Conocer los **elementos básicos del lenguaje**, las estructuras de control, estructuras de datos y elementos sintácticos específicos de **Python**.
- Aprender los elementos necesarios para trabajo con **arrays numéricos en Python**.
- Hacer uso de **mecanismos avanzados de análisis de datos**.
- Conocer los distintos métodos de **representación gráfica de datos**.
- Utilizar de forma adecuada algoritmos de **aprendizaje automático** en Python.

## Setup del proyecto

### Requerimientos

- [Python 3.6](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installing/)
- [pipenv](https://pipenv.readthedocs.io/en/latest/install/#installing-pipenv) (`pip install pipenv`)
- [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

### Procedimiento

~~~console
$ git clone https://github.com/sdelquin/pythoncientifico.git
$ cd pythoncientifico
pythoncientifico$ pipenv install
pythoncientifico$ pipenv run jupyter notebook
~~~

## Docker

Para recrear el entorno de trabajo basta con hacer lo siguiente:

~~~console
$ git clone https://github.com/sdelquin/pythoncientifico.git
$ cd pythoncientifico
pythoncientifico$ ./build-docker.sh
pythoncientifico$ ./run-docker.sh
~~~

Ahora podremos acceder a: http://127.0.0.1:8080 y veremos *Jupyter Notebook* funcionando y mostrando los archivos del proyecto.

> **VOLUMEN**: La carpeta del proyecto está "sincronizada" con la del contenedor de Docker. Eso significa que los cambios que hagamos se verán reflejados en la carpeta de la *máquina real*.

## Generando las transparencias

~~~console
$ make notebook={<nombre_del_notebook_sin_extension>}
~~~
