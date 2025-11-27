#Problem: Fibonacci series generator  
#Description: Program that reads an integer n and prints the
# first n terms of the Fibonacci series starting at 0 and 1.  

number = input("welcome to the fibonacci\n please set how many numbers you need? ")
counter=0
out =0
valid=False
fib=0
fibonacci_series=""
ready=False
try :
    fib=int(number)
    valid=True
except ValueError:
    print("error:invalid input")

if valid and fib>=1:
    print(f"number of terms:{number}")
    while counter<fib :
        counter+=1
        if counter==1:
            out=0
            fibonacci_series="Fibonacci series: " + str(out)
            ready=True
        elif counter<=2:
            out=1
            anterior=out
            fibonacci_series=fibonacci_series+", "+str(out)
        elif counter>2:
            anterior=out-anterior
            out= out+ anterior
            fibonacci_series=fibonacci_series+", "+str(out)
        
            
elif fib<1 and valid==True:
    print("error:invalid input you must put a number bigger than 0")


if ready==True:
    print(fibonacci_series)

