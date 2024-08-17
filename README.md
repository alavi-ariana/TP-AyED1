## Ejercicio 1:
El 'try-except' se utiliza para manejar excepciones (errores) que podrían ocurrir cuando se ejecuta el código. 
- El 'try' se ejecuta primero, si no levanta ningun error el bloque 'except' se skipea.
- El 'except' ocurre cuando se levanta un error en el 'try', en este caso como estoy convirtiendo el input en un entero al poner un float o un string se levanta un 'ValueError' por lo tanto cuando aquello suceda uso un print para decirle al usuario su input es inválido. 
- Con el 'continue' se vuelve al inicio del bucle 'while' volviendo a solicitar un input.

## Ejercicio 2:
Para verificar si un año es bisiesto:
    Si el año es divisible por 100 y 4 y 400 o si solo es divisible por 4 **es bisiesto**, caso contrario **no es bisiesto**.

Utilización de 'args' y 'returns':
- Args (argumentos): describe los parámetros que una función recibe. Especifica el nombre del parámetro, el tipo de dato esperado y una breve descripción de su propósito o uso.
- Return (retorno): describe el valor que una función devuelve después de ejecutarse. Especifica el tipo de dato que se devuelve y una breve descripción del valor devuelto.

## Ejercicio 3:
Como la consigna no aclara valor del pasaje y dice "Averiguar en internet el valor actualizado" me tomé la libertad de pedirle al usuario que ingrese su valor de pasaje.

## Ejercicio 4:
Nada para agregar.

## Ejercicio 5:
- oblongo: un número es oblongo
- triangular: un número es triangular: 
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







