# py_stats

Programa para aplicar un análisis estadístico sobre dos conjuntos
de datos para determinar si uno tiene una media mayor al otro o
si la diferencia entre las medias de ambos conjuntos no es 
estadísticamente significativa.

Específicamente, este programa está diseñado para comparar las
soluciones y el tiempo de ejecución
obtenidos por dos algoritmos distintos (denotados _A_ y _B_)
aplicados sobre un mismo conjunto de casos específicos. 

### Instrucciones de uso

El programa `py_stats` recibe tres valores como entrada: 

1. El tipo de análisis estadístico que se va a aplicar.
Este valor se especifica con la bandera
`-a` o `--analysis-type` y debe ser uno de dos valores 
posibles: `hyp` para aplicar
una prueba de hipótesos o `ci` para calcular un intervalo
de confianza.  Si no se especifica ningún valor
para esta bandera, se aplica la prueba de hipótesis por defecto.
2. El tipo de datos que serán analizados. Este valor
se especifica con la bandera `-d` o `--data-type` y 
debe ser uno de dos valores posibles: `time` para analizar 
los tiempos de ejecución o `sol` para analizar las soluciones.
Si no se especifica ninguno, se analizan soluciones por
defecto. 
3. El nombre del archivo CSV que contiene los datos que
serán analizados. 

Así, el programa `py_stats` se puede ejecutar desde la interfaz
de línea de comandos de la siguiente manera:

```
$ python -m py_stats -a <tipo de análisis> -d <tipo de datos> <nombre del archivo>
```

Si se aplica una prueba de hipótesis, el programa mostrará como
resultado en la pantalla uno de tres mensajes posibles:
`A > B` para indicar que la media de los datos del algoritmo _A_ es mayor
a la media de los datos del algoritmo _B_, `A < B` para indicar el
caso contrario y `A = B` si no hay una diferencia estadísticamente
significativa entre las medias. 

Por otro lado, si se calcula un intervalo de confianza, este
se desplegará en la pantalla como dos números separados por un
guión; el primer número es el límite inferior del intervalo y
el segundo es el límite superior.

Es importante recalcar que los valores de ambos conjuntos de datos
deben ser diferentes, de lo contrario el programa lanzará un
error al intentar calcular el intervalo de confiaza. 

En cuanto al archivo CSV que `py_stats` recibe como entrada,
este debe consistir de cinco columnas.
La primera columna debe contener un nombre que identifique
cada caso específico sobre el cual se aplicaron los algoritmos
_A_ y _B_. La segunda y tercera columna contienen respectivamente la 
cardinalidad de la solución y el tiempo de ejecución obtenidos tras 
aplicar el algoritmo _A_ sobre cada caso específico. Lo mismo ocurre 
con la cuarta y quinta columna, excepto que los datos contenidos en 
estas columnas corresponden a la cardinalidad de la solución y el 
tiempo de ejecución obtenidos por el algoritmo _B_. El primer renglón 
del archivo debe contener un encabezado que describa cada columna. 

Un ejemplo de un archivo CSV siguiendo este formato se presenta
a continuación:

```
Grafo,SolucionA,TiempoA,SolucionB,TiempoB
erdos_renyi_01,20,60,18,39
erdos_renyi_02,21,58,20,25
erdos_renyi_03,18,57,17,12
...
```

El programa `py_stats` supone que el archivo CSV de entrada sigue
este mismo formato; si se proporciona un archivo con un formato
distinto, el comportamiento del programa es impredecible.

### Requerimientos

El programa `py_stats` hace uso de las siguientes librerías:
NumPy, SciPy y statmodels. Los primeros dos vienen
incluidos en Anaconda y sus derivados, pero statmodels debe
instalarse individualmente, por ejemplo, utilizando pip (el 
administrador de paquetes de Python).
