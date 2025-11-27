"""
Student: Jose carlos Medina Lopez
ID: 2530064
Group: 1-1
Assignment: Fibonacci Series Generator in Pytho
EXECUTIVE SUMMARY
The Fibonacci series is a sequence where each term is obtained by adding 
the previous two numbers, starting from 0 and 1. This program reads an 
integer n from the user and generates the first n Fibonacci terms. It 
includes input validation to ensure n is a valid integer and n >= 1. A 
loop is used to iteratively compute the sequence. The objective is to 
practice loops, validation, and formatted output in Python
PROBLEM: FIBONACCI SERIES GENERATOR
Description:
Program that reads an integer n and prints the first n terms of the 
Fibonacci series, starting from 0 and 1.

Inputs:
- n (int; number of terms to generate)

Outputs:
- "Fibonacci series:" followed by the n terms separated by spaces"""
"""
Test cases:

1) Normal case:
   Input: number = 7
   Expected output:
   Number of terms: 7
   Fibonacci series: 0, 1, 1, 2, 3, 5, 8

2) Border case:
   Input: number = 1
   Expected output:
   Number of terms: 1
   Fibonacci series: 0

3) Error case:
   Input: number = "abc"   (non-numeric)
   Expected output:
   error:invalid input

"""

"""
Problem: Fibonacci series generator  
Description: Program that reads an integer n and prints the
first n terms of the Fibonacci series starting at 0 and 1. 
"""
"""
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
"""

"""
CONCLUSIONS
Using a loop made it possible to build the Fibonacci sequence step by step 
without needing complex formulas. Handling special cases such as n = 1 or 
n = 2 ensures the program behaves correctly for all valid inputs. The logic 
for generating Fibonacci numbers can be reused in other programs that 
require iterative sequences or cumulative calculations.

REFERENCES
Python Official Documentation – Built-in Types (List, Tuple, Dict)
https://docs.python.org/3/library/stdtypes.html

Python Official Tutorial – Input & Output
https://docs.python.org/3/tutorial/inputoutput.html

W3Schools – Python Lists
https://www.w3schools.com/python/python_lists.asp

Real Python – Handling Errors With Exceptions
https://realpython.com/python-exceptions/

GeeksforGeeks – Python Program to Check Valid Strings / isalpha()
https://www.geeksforgeeks.org/python-string-isalpha-application/
"""