![Welcome, dear student, seeking answers. May my knowledge assist you.](https://i.pinimg.com/originals/62/63/86/626386f9cccc8c77fe94ce0532b8af90.jpg) 

# TRABAJO PRÁCTICO 1

## Ejercicio 1:
El 'try-except' se utiliza para manejar excepciones (errores) que podrían ocurrir cuando se ejecuta el código. 
- El 'try' se ejecuta primero, si no levanta ningun error el bloque 'except' se skipea.
- El 'except' ocurre cuando se levanta un error en el 'try', en este caso como estoy convirtiendo el input en un entero al poner un float o un string se levanta un 'ValueError' por lo tanto cuando aquello suceda uso un print para decirle al usuario su input es inválido. 
- Con el 'continue' se vuelve al inicio del bucle 'while' volviendo a solicitar un input.

## Ejercicio 2:
Para verificar si un año es bisiesto:
    Si el año es divisible por 100 y 4 y 400 o si solo si es divisible por 4 **es bisiesto**, caso contrario **no es bisiesto**.

Utilización de 'args' y 'returns':
- Args (argumentos): describe los parámetros que una función recibe. Especifica el nombre del parámetro, el tipo de dato esperado y una breve descripción de su propósito o uso.
- Return (retorno): describe el valor que una función devuelve después de ejecutarse. Especifica el tipo de dato que se devuelve y una breve descripción del valor devuelto.

## Ejercicio 3:
Como la consigna no aclara valor del pasaje y dice "Averiguar en internet el valor actualizado" me tomé la libertad de pedirle al usuario que ingrese su valor de pasaje.

## Ejercicio 4:
Nada para agregar.

## Ejercicio 5:
- oblongo: un número es oblongo cuando se puede obtener multiplicando dos números naturales consecutivos.
- triangular: un número es triangular si puede expresarse como la suma de un grupo de números naturales consecutivos comenzando desde 1.
- lambda argumentos: expresion

**lambda**: Indica que estás definiendo una función lambda.

**argumentos**: Son los parámetros de le función (pueden ser múltiples separados por comas).

**expresión**: Es la operación que la función realizará y cuyo resultado será el valor del retorno. 
- any : la función 'any' verifica si alguno de los elementos en una secuncia es True. Si al menos uno lo es, retorna True. Deja de evaluar el iterable cuando encuentra el primer True.
En este caso 'any' se fija en todas la iteraciones si se cumple la condición de num == k * (k+1).
- int() : convierte el resultado a un número entero quitando cualquier parte decimal.
- num ** 0.5 : elevar un número a la potencia 0.5 es lo mismo que calcular la raíz cuadrada.

Probar valores mayor que la raíz de num no es necesario ya que el resultado será mayor que num.
La raíz cuadrada de un número 'n' es el punto en el que la multiplicación de dos números iguales se aproxima a 'n'.

## Ejercicio 6:
Para concatenar los dos enteros recibidos se hace uso de una variable aux para guardar el mismo valor de 'b' y después hacer uso de esa variable sin modificar la original. Se hacen los calculos con la var 'aux' y se utiliza un contador:  mientras el resultado de la división no sea 0 va a seguir diviendo el aux con 10 y sumando al contador 1. Ese contador representa la cantidad de digitos que tiene el número. Por lo tanto cuando retorna *a * (10* ** *contador) + b* retorna el valor de 'a' multiplicado 10 elevado a la cantidad de digitos que tiene el número (si tiene 3 digitos será 10^3 = 1000) y se le suma el valor de b, lo que nos da un total que resembla los dos números casteados mediante una resolución matemática.

## Ejercicio 7:
- '29 if es_bisiesto(year) else 28':
    29: es el valor que se selecciona si la condición 'es_bisiesto(year) es True.
    28: es el valor que se selecciona si la condición 'es_bisiesto(year) es False.
- '_' para iteración: como en este caso no uso la 'i' pylint da error de variable no usada por lo tanto utilizo _ para que no genere advertencias indeseadas.
- Dia siguiente: 
    Primero se asigna a una variable 'dias' la cantidad de días que le corresponde al mes dado. En principio ya sumamos un día y en base a esta condición vamos a (o no) modificar mes y/o año.
    Si nuestro nuevo día es más grande que la cantidad de días en el mes significa que hemos cambiado de mes, se le suma 1 al mes y se asigna el día 1 (el mes empiza de nuevo). Si el mes supera el 12 significa que hemos empezado un año nuevo por lo que a año le sumamos 1, mes y día le asignamos 1 (luego de año nuevo empieza January 1st).
- Sumar días: 
    Se crea una lista 'fecha' que va a almacenar la fecha original dada por el usuario, en cada iteración se va actualizando la lista 'fecha' (con nuestra función anterior llamada 'diasiguiente' *multitasking*).
- Total days: 
    Se empieza el conteo de la cantidad de días que hay de diferencia entre fecha 1 y fecha 2.
    Desde el año 0 hasta el año anterior al dado, se le van sumando los días de cada año y desde el mes 1 hasta un mes anterior al dado se le suman los días de cada mes (que cambian dependiendo el mes).
    Por último sumamos los días del mes que se otorgó, como no se incluye en el range ya que ese mes no ha terminado se le agrega esos días.
- Desempaquetar: 
    Con '*fecha' hacemos algo llamado desempaquetar (una tupla o lista), tomamos cada elemento de la lista y lo asignamos a una variable por separado. Es lo mismo que escribir (en este caso): 'fecha[0], fecha[1], fecha[2]'.

## Ejercicio 8
No me divierte este ejercicio...

## Ejercicio 9
Nada para agregar. Vivan las naranjas.

# TRABAJO PRÁCTICO 2

## Ejercicio 1
- reduce() toma una función y una lista, y aplica la función de manera acumulativa a los elementos de la lista.
- lista[:] es una forma de actualizar el contenido de la lista original. Usar [:] significa que estamos operando sobre la lista en su lugar y no creando una nueva lista.
- def capicua(lista):
    supongamos que la lista es [1, 2, 3, 2, 1].

    primera iteración (i = 0):
    lista[0] es 1.
    lista[len(lista) - 0 - 1] es lista[4] que también es 1.
    comparación: 1 == 1, continúa con la siguiente iteración.

    segunda iteración (i = 1):
    lista[1] es 2.
    lista[len(lista) - 1 - 1] es lista[3] que también es 2.
    comparación: 2 == 2, continúa con la siguiente iteración.

    tercera iteración (i = 2):
    lista[2] es 3.
    lista[len(lista) - 2 - 1] es lista[2] que también es 3.
    comparación: 3 == 3, no hay más iteraciones.

## Ejercicio 6
¿Qué es normalizar una lista de números? 
Normalizar significa tomar una lista de números y ajustarlos de modo que la suma total de los números sea 1.0, pero manteniendo las proporciones relativas entre ellos. Es decir, los valores siguen manteniendo su relación de magnitud original (si uno es el doble de otro en la lista original, también lo será después de la normalización), pero ahora en una escala más manejable.

Ejemplo práctico:
Supongamos que tienes tres números: 1, 1 y 2. Esto puede representar, por ejemplo, la cantidad de votos que tres personas recibieron en una competencia.

La suma total de los votos es 1 + 1 + 2 = 4.
Para normalizar estos números, dividimos cada uno por la suma total:
El primer 1 se convierte en 1 / 4 = 0.25.
El segundo 1 se convierte en 1 / 4 = 0.25.
El 2 se convierte en 2 / 4 = 0.50.
El resultado es [0.25, 0.25, 0.50]. Este conjunto de números ahora suma 1.0 en total, lo que facilita la comparación y análisis de los valores en proporciones relativas.

## Ejercicio 7 
- SLICES
Syntax: secuencia[inicio:fin:paso]

inicio: el índice donde comenzará la rebanada. Si se omite se asume que es el principio de la secuencia.
fin: el índice donde terminará la rebanada (este índice no está incluido). Si se omite llegará hasta el final de la secuencia.
paso: es opciona y determina cuántos elementos saltar entre cada uno. 

- slicing fuera de los límites: si el inicio o el fin están fuera del rango de la secuencia, python no genera error, simplemente toma los elementos que pueda.
- si el inicio es mayor o igual que el fin, o si el paso es incorrecto, obtendrás una lista vacía.

- 'lista1[2 * i + 1:2 * i + 1] = [lista2[i]]':
la expresión '2 * i + 1' calcula la posición en lista1 donde se debe insertar el elemento de la lista2.

- [2 * i + 1:2 * i + 1]: es una rebana que selecciona un rango vacío en lista 1. esto permite insertar un nuevo elemento sin sobreescribir los existentes.

## Ejercicio 11
- set(): un conjunto no permite elementos duplicados.
    - add(): agregar elementos
    - eliminar elementos: remove() o  discard() <- este no genera error si el elemento no está en el set.
    - union(): combinar dos conjuntos
    - intersection(): encuentra los elementos comunes entre conjuntos
    - difference(): devuelve los elementos presentes en un conjunto pero no en el otro 

# TRABAJO PRÁCTICO 3

![hola mundo](https://www.profesorenlinea.cl/imagenmatematica/Matriz_tipos005.jpg)

Una matriz es una estructura rectangular de números organizados en filas y columnas.
Cada matriz siguen un patrón expecífico y al identificarlos se pueden construir las matrices de manera sistemática.

Pensamiento lógico:
1. identificar el patrón: observa cómo se distribuyen los números y trata de encontrar reglas generales para llenar las matrices.
2. usar la indexación: recorda que podes acceder a posiciones en la matriz utilizando índices. esto permite colocar valores específicos en las posiciones correctas.
3. generalización: cuando encuentres una regla, intenta formularla de manera que se aplique a matrices de cualquier tamaño (NxN)

## Ejercicio 1
a. Cargar números enteros en una matriz de N x N
Crear una matriz cuadrada (con el mismo número de filas y columnas) de tamaño 𝑁×𝑁, donde 𝑁 es un número que el usuario ingresa. Luego pedir al usuario que ingrese los números que llenarán esta matriz.

b. Ordenar en forma ascendente cada una de las filas de la matriz
Ordenar cada fila (es decir, cada lista de números) de menor a mayor.

c. Intercambiar dos filas
El usuario elije dos filas específicas de la matriz y luego intercambiar los elementos de esas filas. Por ejemplo, si intercambias la fila 0 con la fila 1, todos los elementos de la fila 0 deben pasar a la fila 1 y viceversa.

d. Intercambiar dos columnas
Similar a lo anterior, pero en este caso, se deben intercambiar dos columnas. El usuario debe indicar qué columnas desea intercambiar y todos los elementos de esas columnas deben ser intercambiados.

e. Trasponer la matriz sobre sí misma
La trasposición de una matriz implica cambiar la posición de sus elementos. Para cada elemento 𝐴𝑖𝑗 de la matriz original, debe ocupar la posición 𝐴𝑗𝑖 en la matriz transpuesta. Es decir, los elementos de las filas se convierten en columnas.

f. Calcular el promedio de los elementos de una fila
Pedir al usuario que ingrese el número de una fila y calcular el promedio de todos los elementos de esa fila. El promedio se obtiene sumando todos los elementos y dividiendo entre la cantidad de elementos.

g. Calcular el porcentaje de elementos con valor impar en una columna
El usuario ingresa el número de una columna. Luego contar cuántos de los elementos en esa columna son impares y calcular qué porcentaje del total de elementos de esa columna representan.

h. Determinar si la matriz es simétrica con respecto a su diagonal principal
Una matriz es simétrica respecto a su diagonal principal si los elementos de la posición 𝐴𝑖𝑗 son iguales a los de la posición 𝐴𝑗𝑖 para todos los 𝑖 y 𝑗. En otras palabras, si reflejas la matriz sobre su diagonal principal, los valores deben coincidir.

i. Determinar si la matriz es simétrica con respecto a su diagonal secundaria
La diagonal secundaria va de la esquina superior derecha a la esquina inferior izquierda. La matriz es simétrica respecto a esta diagonal si 𝐴𝑖𝑗 es igual a 𝐴𝑛−1−𝑗,𝑛−1−𝑖, donde 𝑛 es el tamaño de la matriz.

j. Determinar qué columnas de la matriz son palíndromos
Una columna es un palíndromo si sus elementos son iguales cuando se leen de arriba hacia abajo y de abajo hacia arriba. 

## Ejercicio 2
- matriz a: es una matriz diagonal, donde los valores en la diagonal son impares.
    patrón: se coloca un número impar en la diagonal principal y cero en el resto.

- matriz b: los valores decrecen desde la esquina superior derecha hacia la inferior izquiera.
    patrón: se coloca un número decreciente en la diagonal secundaria.
    iniciamos desde el valor máximo y lo decrecemos en cada posición de la diagonal.

- matriz c: se rellena con números crecientes en las filas inferiores y columnas a la izquiera, formando un triangulo inferior izquierdo.
    patrón: coloca un número creciente en una forma triangular.
    a medida que avanzamos por las filas, aumentamos el número que colocamos.

- matriz d: todas las filas contienen el mismo número, que decrece en cada fila sucesiva.
    patrón: rellena toda la fila con el mismo número, que decrece de fila a fila.

- matriz e: alterna entre colocar un valor creciente en la diagonal principal y en la diagonal secundaria.
    patrón: alternancia en la diagonal principal y secundaria
    colocamos un número en posiciones específicas basándonos en el índice
    (:=) :walrus operator permite actualizar el valor de una variable en el mismo lugar donde la usas, siempre y cuando se cumpla una condición.

# TRABAJO PRÁCTICO 4

## Ejercico 1 
- zip(): toma dos o más iterables y los empareja en pares de elementos. Crea parejas de caracteres de la cadena original y su versión invertida, reccoriéndolas simultáneamente. 
- all(): toma un iterable y devuelve True si todos los elementos del iterable son True, si uno solo es False devolverá False.

## Ejercicio 4
Los números romanos cubren hasta el 3999 por lo que si se cambian los rangos a valores menores o mayores habría que cambiar la  tabla de equivalencias.

## Ejercicio 5
- r'\b\w{' + str(n) + r',}\b' :
    r'' : indica que la cadena es una cadena cruda, los caracteres de escape no se procesan.
    \b : límite de palabra. esto asegura que el patrón busque coincidencias que comiencen y terminen en los límites de las palabras. Evita que coincida con caracteres que no sean parte de palabras (como signos de puntuación).
    \w : coincide con cualquier carácter de palabra. equivalente a [a-zA-Z0-9_]
    {n,} : indica que queremos buscar un mínimo de n repeticiones del carácter anterior (en este caso \w).
    '\b' (al final): asegurar que la coincidencia termine en un límite de palabra. garantiza que no se incluyan caracteres adicionales que no pertenezcan a la palabra.

## Ejercicio 7
- cadena[:start] : esto obtiene la parte de la cadena desde el inicio hasta la posición de inicio (sin incluirla)
- cadena[start + carac:] : esto obtiene la parte de la cadena que va desde la posición de inicio más la cantidad de caracteres a eliminar hasta el final de la cadena.
- eliminar_subcadena_sinslice: se usa un bucle para iterar por cada caracter de la cadena. si el indice no esta dentro del rango de la subcadena a eliminar, se añade al resultado
- map(int, input().split(",")):  obtengo una cadena con el input, lo divido en subcadena con split y lo convierto en un entero.

## Ejercicio 9
- re.findall(patron, cadena): extrae todas las palabras y sus signos de puntuación asociados
- patron = r'[.,¡¿;]*\w+[\w\']*[.,!?;]*'  : 
    \w+ : busca una o más (+) letras, números o guion bajos (\w); equivalente a [a-zA-Z-0-9_]
    [\w\']* : busca 0 o más caracteres que sean letras (*), números o guion bajos dentro de la palabra (\w), esto permite que se incluyan palabras que tiene apóstrofes (') como 'dónde'.
    [.,!?;]* : esto busca 0 o más (*) signos de puntuación, especificamente: punto(.), coma(,), interrogación(?), exclamación(!) y punto y coma(;) esto permite que si aparece algun signo de puntuación en el final o al principio de la palabra se incluya

## Ejercicio 10
- re.sub(pattern, repl, string): reemplaza todas las ocurrencias del patrón en string con repl y devuelve la cadena resultante.
- re.subn(): hace lo mismo que re.sub() pero también devuelve la cantidad de reemplazos realizados. retorna una tupla que contiene (cadena modificada, entero)
- patron = r'\b' + re.escape(og) + r'\b'  :
    r'\b: indica el inicio o el final de una palabra, asegura que coincida solo con palabras completas, no con fragmentos de otras palabras. ej: 'perro' coincide con 'perro' pero no con 'perros'.
    re.escape(): escapa cualquier carácter especial.

## Ejercicio 11
- '.*?'.join(subcadena) : busca cada carácter de la subcadena, permitiendo que haya cualquier número de caracteres entre ellos.
    .*? : cero o más caracteres de cualquier tipo. esto permite que cualquier carácter (incluyendo espacios y signos de puntuación) esten presentes entre los caracteres de la subcadena

## Ejercicio 14
- ^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.(com|com\.ar)$  :
    ^[a-zA-Z0-9]+ asegura que el nombre de usuario solo contenga caracteres alfanuméricos y no esté vacio
    @[a-zA-Z0-9]+ exige que haya un simbolo @ seguido de un dominio que también debe tener caracteres alfanuméricos
    \.(com|com\.ar)$ garantiza que el correo termine en .com o .com.ar

- correo.split("@")[1] : la primera parte es el nombre del usuario, la segunda parte es el dominio.

# TRABAJO PRÁCTICO 8
## Ejercicio 3:
- patron: ^([a-zA-Z0-9._-]+)@([a-zA-Z0-9.-]+)\.([a-zA-Z]{2,})(?:\.([a-zA-Z]{2,}))?$

1. ^ y $
    ^: indica el inicio de la cadena. 
    $: indica el final de la cadena.

2. ([a-zA-Z0-9._-]+)
    [a-zA-Z0-9._-]: Permite letras (a-z, A-Z), números (0-9), puntos (.), guiones bajos (_) y guiones medios (-).
    +: Indica que debe haber al menos un carácter válido.

3. @: carácter obligtoiro que separa el nombre del usuario del dominio.

4. \.([a-zA-Z]{2,})
    \.: Literal que detecta el punto separador (debe estar escapado con \ porque el punto es un carácter especial en regex).
    [a-zA-Z]: Permite solo letras.
    {2,}: Indica que debe haber al menos 2 caracteres.

5. (?:\.([a-zA-Z]{2,}))?
    (?:...): Es un grupo no capturante. Esto significa que no lo incluiremos en los resultados como un grupo separado, pero lo usamos para agrupar partes del patrón.
    \.: Detecta el punto separador.
    [a-zA-Z]{2,}: Permite solo letras, con al menos 2 caracteres.
    ?: Indica que esta parte es opcional.


- groups(): Devuelve todas las subcadenas capturadas en una tupla.

## Ejercicio 4:
Se utiliza el operador &, que es el operador de intersección de conjuntos en Python. Este operador devuelve un nuevo conjunto que contiene solo los elementos que están presentes en ambos conjuntos (es decir, los valores que son comunes entre las dos fichas).

