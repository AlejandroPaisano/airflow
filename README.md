# Airflow
# Introduccion
La actividad contenida en este repositorio es un ejemplo de un archivo sencillo que se puede realizar en airflow. Para este ejemplo en particular se ha usado dos inteligencias aritficiales, representadas como una escopba, que deben recorrer una matriz de 10*10 en busca de basura.
Un robot corre de forma completamente aleatoria, mientras que el otro observa si hay basura a su alrededor antes de moverse.
# Desarrollo
![image](https://github.com/AlejandroPaisano/airflow/assets/91223611/84e788f9-3af7-4dea-b701-2c5cef408f43)

Lo primero es el codigo, aqui importamos unas bibliotecas que necesitaremos, timedelta lo usaremos para programar la ejecucion de tareas, DAG es el formato que le daremos al codigo que le diremos a airflow que debe operar, el operador de python es para ayudar con la traduccion del codigo,
datetime eas para apoyarnos en cuestiones de asignar fechas de ejecucion y pandas para ayudarnos a manejar la informacion mas facilmente.

No entrare en detalle sobre el funcionamiento de los agentes, debido a que estos no son muy relevantes para la actvidad presente. Pero en resumen, se genera una matriz y se le introducen elementos basura de forma aleatoria, y le da una posicion aleatoria al elemento escoba,
una vez hecho esto, se le da un numero aleatorio al programa el cual interpreta como su movimiento, dichos movimientos estan limitados en arriba, abajo, izquieda y derecha, en caso de encontrar basura, el agente limpia la basura y se movera despues.
Por ultimo, si el agente se encuenrta en una pared, este simplemente volver a lanzar otro movimiento hasta encontrar un movimiento valido.

La unica diferencia entre agentes, es que uno mira si hay basura en sus posibles movimientos antes de moverse aleatoriamente.

![image](https://github.com/AlejandroPaisano/airflow/assets/91223611/e85f6491-1f36-429d-8578-8471f8328e41)

![image](https://github.com/AlejandroPaisano/airflow/assets/91223611/cb2caf36-ce94-4b9a-8072-1c7db70c0183)

Aqui podemos ver que ambos agentes son definidos como funciones para poder ser usados en el futuro.

![image](https://github.com/AlejandroPaisano/airflow/assets/91223611/6a7527ea-17f2-46f2-bc09-cae506ac46b0)

En esta imagen podemos observar el DAG y el como se define, cabe aclarar que ddebemos informarle al codigo que estas instrucciones seran ejecutadas con la biblioteca dag que antes importamos. Lo primero es el ID del dag, este sirve como identificador principal para el programa
y para decirle como debe guardar esste dag en la base de datos, despues esta el cronograma que le daremos, en este caso elegir por hora, debido a que quiero ver la eficiencia de los robots y tener datos de su ejecucion para guardar para despues.

Mas abajo tenemos los argumentos del DAG, el owner es a quien le pertenece el dag dentro del sistema, aqui usamos el usuario por defecto, retries es la cantidad de intentos que le daremos al codigo antes de considerarlo un fallo, retry_delay es la cantidad de tiempo que
daremos entre intentos y el start date es cuando empezara la tarea oficialmente, se recomienda inbsertar una fecha anterior al dia de inicio oficial.

![image](https://github.com/AlejandroPaisano/airflow/assets/91223611/91f04190-c114-4b9e-aa2b-240fbc3082f2)

por ultimo tenemos las variables de ambos agentes, les ponemos un numbre similar a su definicion para identificarlos facilmente. Aqui tenemos task_id que es el como se guardara esta actividdad edntro de airflow, luego tenemos el python_callable que es la funcion que llamaran
al ejecutars. Por ultimo esta provide_contxt, su funcion es ayudarnos a pasar ciertos argumentos mas facilmente entre funciones, aunque aqui no se usa por que las funciones no estan conectadas.

Debido a que ambas funciones estan puestas asi, estas se ejecutaran en paralelo, cosa que deseamos debido a que queremos medir su eficiencia. si quisieramos ejecutarlas una detras de la otra, usariamos elcomando ">>>" indicando que la funcion que va a la izquierda se
ejecuta primero

![image](https://github.com/AlejandroPaisano/airflow/assets/91223611/a476e6b7-decf-495e-a284-a7aba35482fd)

Dentro de airflow tenemos esta vista, esta nos permite ver los dags que tenemos, cuales estan activos y cuales estan pausados, en este caso, solo el dag de worflow, donde esta la IA, esta acivo. En esta imagen se ve tambien donde esta el dueño de ese dago y cuantas "runs"
o ejecuciones del DAG se han hecho.

Tambien es posible filtrar el DAG por su estadod de ejecucion mas reciente y por sus nombres, ademas de mostrarnos los resultados de su ultima ejecucion. Al final de la pagina, se puede ver un bote de basura que nos sirve para eliminar el DAG y una flecha que sirve para
ejecutar el DAG de golpe, y en medio podemos ver el cronograma que le dimos, su ultima ejecucion y cuando sera la siguiente

![image](https://github.com/AlejandroPaisano/airflow/assets/91223611/9c466d59-fd0b-46fe-8add-a48fee4266ba)    ![image](https://github.com/AlejandroPaisano/airflow/assets/91223611/e51faf70-8832-45b0-b288-96f163660aae)

En la vista de task instances podemos visualizar el estado de cada tarea que se ha hecho, filtrarlas y ademas podemos ver el log que generan

![image](https://github.com/AlejandroPaisano/airflow/assets/91223611/484d35a5-5558-424a-87c9-9faf6dfc0166) Aqui un ejemplo del log generado por el primer agente

![image](https://github.com/AlejandroPaisano/airflow/assets/91223611/c893afd9-4635-4a67-91ba-ff7d57082fc8)

Por ultimo tenemos la propia seccion del worflow, aqui podemos ver todo, tiempos de ejecucion comparados a ejecuciones pasadas, cuantos operadores hay y un grafo donde se muestra que, en este caso, operan de forma paralela.
Tambien podemos ver detalles que nos explican como opera el algoritmo, el propio codigo y un diagrama de gant con una linea de tiempo de los eventos que pasaron y su estado, asi como los logs de cada ejecucion.

![image](https://github.com/AlejandroPaisano/airflow/assets/91223611/c4ea1429-7ce3-4334-855e-6dce64467b5f)


# conclusion

Ariflow es una herramienta sumamente poderos acuandos e trata de poder programa flujos de trabajo y automatizarlos para recoger informacion. Lo unico malo que este tiene es lo dificil que llega a ser el poder usarlo de forma adecuada dentro de windows,
dado que no esta hecho para operar de forma nativa en este sistema, asi que hacerlo funcionar puede ser un dolor de cabeza, aun asi, eso no significa que no haya herramientas para poder usarlo mas facilmente, un ejemplo es docker que solo requier unas imagenes para operarlo.

Por ultimo, cabe decir que esta experiencia fue bastante interessante, instalar airflow fue complicado, pero eso me llevo a conocer docker que veo como una herramienta mas util, en general, un proceso que fue complicado per resulto en bastante aprendizaje al final
