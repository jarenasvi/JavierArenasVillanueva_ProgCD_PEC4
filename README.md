# PEC4 Programación para la Ciencia de Datos: Rendimiento de los estudiantes universitarios en Cataluña
Javier Arenas Villanueva

## Contexto
El conjunto de datos recoge los principales indicadores vinculados a la medida del rendimiento académico de los estudiantes, como son las tasas de rendimiento, de graduación, de eficiencia y de abandono. Los datos han sido descargados desde el siguiente enlace: https://recercaiuniversitats.gencat.cat/ca/03_ambits_dactuacio/xifres/docencia/Rendiment-dels-estudiants/

Se trabajará con dos datasets principales:
  1. Tasa de rendimiento (rendiment_estudiants.xlsx):
     Para un determinado curso, es el cociente entre el número de créditos superados respecto al número de créditos matriculados en los estudios de grados y másteres.
     - En este cálculo solo se tienen en cuenta los créditos ordinarios, que son los propios de un estudio.
     - Se excluyen los créditos reconocidos, los adaptados y los transferidos de otros planes de estudios.
       
  2. Tasa de abandono (taxa_abandonament.xlsx)
     Para un determinado curso, es la proporción de estudiantes de grado o máster que abandonan el Sistema Universitario Catalán (SUC) en el primer curso sobre el total de nuevo acceso de aquel curso.
     - Se establece que el estudiante ha abandonado el SUC si no se matricula en el próximo curso en ninguna de las universidades catalanas.
    
## Ejercicio 
El trabajo consta de cuatro ejercicios, cada ejercicio se realiza con los modulos indicados:
1. Ejercicio 1. Load dataset y EDA --> data_loader.py + eda.py
2. Ejercicio 2: limpieza de los datos y filtrado --> cleaning.py
3. Ejercicio 3: Análisis Visual de Tendencias Temporales --> visualization.py
4. Ejercicio 4: Análisis estadístico automatizado --> analysis.py

Para más detalle de los enunciados se puede consultar el archivo "Enunciado_PEC4.pdf".

## Estructura de las carpetas
La estructura de las carpetas es la que se muestra a continuación. En todo caso, en el siguiente apartado se detalla cada una.
```bash
JavierArenasVillanueva_ProgCD_PEC4
                                  │
                                  ├─ src/
                                  │ ├─ data/
                                  │ ├─ img/
                                  │ ├─ report/
                                  │ ├─ main.py
                                  │ ├─ modules/
                                  │   ├─ data_loader.py
                                  │   ├─ eda.py
                                  │   ├─ cleaning.py
                                  │   ├─ visualization.py
                                  │   └─ analysis.py
                                  │
                                  ├─ doc/
                                  ├─ screenshots/
                                  ├─ requirements.txt
                                  ├─ Enunciado_PEC4.pdf
                                  ├─ LICENSE.txt
                                  ├─ README.md
                                  └─ pep8.pylintrc
```
### Información detallada
#### src/
  1. **data/**: carpeta con los dos archivos ```.xlsx``` rendiment_estudiants y taxa_abandonament.
  2. **img/**: carpeta con la imagen resultante del ejercicio 3.
  3. **report/**: carpeta con el archivo JSON generado en el ejercicio 4.
  4. **main.py**: archivo principal que importa todos los módulos y ejecuta los distintos ejercicios.
  5. **modules/**: carpeta con los diferentes módulos necesarios para llevar a cabo los ejercicios. Dichos módulos contienen varias funciones cuyas especificaciones pueden consultarse en la carpeta ``doc/``.
     - **data_loader.py**: módulo correspondiente a la primera parte del ejercicio 1, donde se cargan los datos.
     - **eda.py**: módulo módulo correspondiente a la segunda parte del ejercicio 1, donde se realiza el análisis exploratorio de los datos (EDA).
     - **cleaning.py**: módulo del ejercicio 2, donde se lleva a cabo la limpieza y transformación de los datos.
     - **visualization.py**: módulo en el que se genera un archivo ``.png`` en la carpeta ``img/``, mostrando la Evolución del % de Abandono por curso académico y la Evolución de la Tasa de Rendimiento por curso académico.
     - **analysis.py**: módulo correspondiente al ejercicio 4, donde se realiza un análisis estadístico automatizado que se guarda en un archivo ``.json`` dentro de la carpeta ``report/``.
#### doc/
- Carpeta con la documentación de cada función.
#### screenshots/
- Carpeta con las capturas de pantalla de las evidencias.
#### requirements.txt
- Documento de texto con las librerias necesarias para el proyecto. 
#### Enunciado_PEC4.pdf
- Documento con el enunciado de la práctica donde están más detallados los ejercicios.
#### LICENSE.txt
- Documento con la licencia. 
#### README.md
- Este miso documento que se está leyendo ahora mimso. 
#### pep8.pylintrc
- Documento `.pylintrc` con la configuración de Pylint para comprobar el estilo y la calidad del código siguiendo la norma PEP8.
  Se han puesto las siguinetes excepciones:
  - R0914: evitar el warning de demasiadas variables locales.
  - E1101: evitar warning de matplotlib.cm.tab10.
  - CO301: evitar warning de líneas demasiado largas, ya que no son excesivas.

## Instalación
1. `Iniciar un terminal e indicar el cirectorio de la carpeta donde irá el proyecto.`
2. `git clone https://github.com/jarenasvi/JavierArenasVillanueva_ProgCD_PEC4`
3. `cd ./JavierArenasVillanueva_ProgCD_PEC4
4. `pip install -r requirements.txt`
5. `python -m pylint --rcfile=pep8.pylintrc src`
6. `cd ./src`
7. `python main.py`
    o
    `python main.py -ex X` donde X es el número del ejercicio o `python main.py -h` para ayuda
