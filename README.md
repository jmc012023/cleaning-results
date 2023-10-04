# Objetivo
Aprender a utilizar pandas, git, github y asyncio

# Descripcion
Se utiliza la libreria pandas para traer datos de los resultados de admision de la UNT, a traves de la url, luego se limpia los datos para finalmente devolverlos en columnas separadas
El archivo base-case se toma como referencia, luego en el archivo app se consulta mas de una url
y todas las urls consultadas se les aplica las mismas funciones que al archivo de referencia base-case

# Tener en cuenta
- Se consulta los resultados de admision de la UNT usando las url, pero ha sido probado con algunas muestras para que cumpla con ordinarios y cepunt, sin embargo los de tipo extraordinario puede que se encuentren bugs
- El resultado final contiene indices repetidos, ademas las 3 columnas finales no se encuentran
limpias pero se incluyeron para continuar aprendiendo otras herramientas de limpieza y transformacion de datos como Power BI
- Los print que se incluyen al final del archivo app son solo para comprobar los resultados 
y el tiempo que demoro en hacer toda la limpieza de la data con asyncio
- Todo el codigo esta en un solo archivo ya que lo hice para facilitar mi aprendizaje de pandas y
tener este archivo de referencia para consultar sintaxis y nombres de funciones de manera rapida,
y es la misma razon por la que no agrege sentencias try catch.
