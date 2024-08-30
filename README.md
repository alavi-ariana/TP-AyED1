![Welcome, dear student, seeking answers. May my knowledge assist you.](https://i.pinimg.com/originals/62/63/86/626386f9cccc8c77fe94ce0532b8af90.jpg) 

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







