print("welcome to the statistics calculator")
numbers=[]#inicializamos una lista
counter=0#definimos variables que nos serviran mas tarde
while True:#nos pedira que volvamos a ingresar los numeros hasta que estos sean enteros
    num1 = input("please set your first \n")
    num2 = input("please set your second \n")
    num3 = input("please set your third \n")
    try:#verificamos que los numeros sean enteros
        nat1= int(num1)
        nat2= int(num2)
        nat3= int(num3)
        numbers.extend([nat1,nat2,nat3])#agregamos todo a numbers
        break #rompe el ciclo si las condiciones se cumplen
    except ValueError:
        print("error:invalid number")#mensaje de error si la entrada no es valor numerico
for number in numbers:#compara si los valores son pares
    if number%2==0:
        counter=counter+1
print(f"sum:{sum(numbers)}")#imprime la suma de los numeros
print(f"average:{(sum(numbers))/3}")#imprime el promedio de los numeros
print(f"maximum value:{max(numbers)}")#imprime el valor maximo de los numeros
print(f"minimum value: {min(numbers)}")# imprime el valor minimo de los numeros
print(f"all even: {counter==3}")#nos dice si todos los valores son pares
