string = 'texto'
integrer = 23
booleano = True
flotante = 23.3

#Concatenacion de las variables.
concatenados = (f'{string} {integrer} {booleano} {flotante}')
print(concatenados)

#Limite en enteros:  Python 3 utiliza una representación interna variable para enteros, lo que significa que no tiene límites estrictos en términos de su tamaño. La cantidad de memoria disponible en la máquina es el principal factor que determina los límites prácticos.
#Limite en flotantes:  En Python 3 suele ser aproximadamente 1.8 x 10^308, y el valor mínimo positivo representable suele ser del orden de 2.2 x 10^-308.

#Formula de la suma de los primeros n numeros pares.
n = int(input("Ingrese la cantidad de terminos pares: "))
suma = n * (n + 1)
print(f'La suma de los primeros numeros pares es {suma}')
