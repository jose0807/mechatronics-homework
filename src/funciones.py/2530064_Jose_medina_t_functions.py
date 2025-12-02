"""
Manejo de funcones en python
Jose Carlos Medina Lopez
2530064
IM 1-1
""" 
#Resumen ejecutivo

#En este documento se vera el manejo de funciones en python
#las cuales cumplen diferentes papeles, tales como "def" la cual define una funcion
#y "return" la cual devuelve un valor de una funcion
#de igual forma parametros con valor por defecto y argumentos

# Principios y buenas practicas
# Es recomendable crear funciones pequeñas que realicen una sola tarea (single responsibility),
# lo cual facilita entenderlas, probarlas y reutilizarlas.
# Evita repetir código: si notas que copias y pegas lógica, es mejor extraerla en una función aparte.
# Siempre que sea posible, intenta que las funciones sean “puras”; es decir, que el mismo input
# produzca el mismo output y que no dependan de variables externas.
# Documenta cada función con comentarios simples indicando qué hace y qué parámetros recibe.
# Usa nombres claros y descriptivos para las funciones (por ejemplo, calculate_bmi en lugar de f1 o do_it).

#7.3 Problem 1: Rectangle area and perimeter (basic functions)
#Define two functions to calculate the area and perimeter of a rectangle.
#The functions should take the width and height of the rectangle as parameters

# Inputs:
# - width (float)
# - height (float)
# Outputs:
# - "Area" (value)
# - "Perimeter" (value)

#validations:
# - width and height must be positive numbers

# Test cases:
# 1) Normal:
#    Input: width=5, height=3
#    Expected: Area=15, Perimeter=16
#
# 2) Border:
#    Input: width=0.01, height=0.01
#    Expected: Area=0.0001, Perimeter=0.04
#
# 3) Error:
#    Input: width=-4, height=2
#    Expected: "Error: invalid input"
# ----------------------------------------------------

def calculate_area(width, height):
    """Returns the area of a rectangle."""
    return width * height


def calculate_perimeter(width, height):
    """Returns the perimeter of a rectangle."""
    return 2 * (width + height)


# ---- Main program (test values) ----
width = float(input("Enter the width of the rectangle: "))
height = float(input("Enter the height of the rectangle: "))    

if width > 0 and height > 0:
    area = calculate_area(width, height)
    perimeter = calculate_perimeter(width, height)

    print("Area:", area)
    print("Perimeter:", perimeter)
else:
    print("Error: invalid input")



#7.3 Problem 2: Grade classifier (functions with return string)
# ----------------------------------------------------
# Description:
#   This program defines a function that receives a
#   numeric grade (0–100) and returns a letter category
#   according to standard grading ranges.
#
# Inputs:
# - score (float or int)
#
# Outputs:
# - "Score:" <score>
# - "Category:" <grade_letter>
#
# Validations:
# - 0 <= score <= 100
# - If invalid, print "Error: invalid input"
#
# Test cases:
# 1) Normal:
#    Input: score=85
#    Expected: Category="B"
#
# 2) Border:
#    Input: score=90
#    Expected: Category="A"
#
# 3) Error:
#    Input: score=150
#    Expected: "Error: invalid input"
# ----------------------------------------------------

def classify_grade(score):
    """Returns a letter grade based on the numeric score."""
    
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


# ---- Main program ----

score = float(input("Enter the score: "))

if 0 <= score <= 100:
    category = classify_grade(score)
    print("Score:", score)
    print("Category:", category)
else:
    print("Error: invalid input")


# =========================================================
# 7.3 Problem 3: List statistics function (min, max, average)
# =========================================================
# ENTRADAS:
#   - Lista de números ingresados por el usuario separados por comas.
# SALIDAS:
#   - Diccionario con {min, max, average}
# VALIDACIONES:
#   - Entrada vacía
#   - Conversión a número
#   - Lista no vacía
# TESTING:
#   summarize_numbers([1,2,3]) -> {"min":1, "max":3, "average":2}

def summarize_numbers(numbers_list):
    min_value = min(numbers_list)
    max_value = max(numbers_list)
    average_value = sum(numbers_list) / len(numbers_list)
    return {"min": min_value, "max": max_value, "average": average_value}


numbers_text = input("Ingresa números separados por comas: ").strip()

if numbers_text == "":
    print("Error: input vacío")
else:
    try:
        numbers_list = [float(x) for x in numbers_text.split(",")]

        if len(numbers_list) == 0:
            print("Error: lista vacía")
        else:
            stats = summarize_numbers(numbers_list)
            print("---- RESULTADOS ----")
            print("Min:", stats["min"])
            print("Max:", stats["max"])
            print("Average:", stats["average"])

    except ValueError:
        print("Error: input no numérico")


# =========================================================
# 7.4 Problem 4: Apply discount list (pure function)
# =========================================================
# ENTRADAS:
#   - Lista de precios separados por comas
#   - Tasa de descuento entre 0 y 1
# SALIDAS:
#   - Lista nueva con los precios descontados
# VALIDACIONES:
#   - Lista vacía, precios negativos, descuento incorrecto
# TESTING:
#   apply_discount([100, 200], 0.10) -> [90, 180]

def apply_discount(prices_list, discount_rate):
    return [price * (1 - discount_rate) for price in prices_list]


prices_text = input("Ingresa precios separados por comas: ").strip()

try:
    discount_rate = float(input("Ingresa la tasa de descuento (0 a 1): "))
except ValueError:
    print("Error: la tasa debe ser numérica")
    discount_rate = -1  # Forzar error

if prices_text == "" or not (0 <= discount_rate <= 1):
    print("Error: input inválido")
else:
    try:
        prices_list = [float(p) for p in prices_text.split(",")]

        if any(p < 0 for p in prices_list):
            print("Error: los precios deben ser mayores que 0")
        else:
            discounted_list = apply_discount(prices_list, discount_rate)

            print("---- RESULTADOS ----")
            print("Original prices:", prices_list)
            print("Discounted prices:", discounted_list)

    except ValueError:
        print("Error: input no numérico")


# =========================================================
# 7.5 Problem 5: Greeting function (default parameters)
# =========================================================
# ENTRADAS:
#   - Nombre y título opcional
# SALIDAS:
#   - Cadena con saludo formateado
# TESTING:
#   greet("Alice") -> "Hello, Alice!"
#   greet("Bob", "Dr.") -> "Hello, Dr. Bob!"

def greet(name, title=""):
    name = name.strip()
    title = title.strip()
    if title:
        full_name = f"{title} {name}"
    else:
        full_name = name
    return f"Hello, {full_name}!"

print(greet("Alice"))
print(greet("Bob", "Dr."))
print(greet(name="Charlie", title="Eng."))

# ----------------------------------------------------
# Problem 6: Factorial function (iterative or recursive)
# Description:
#   This program defines a function factorial(n) that
#   returns the factorial of a non-negative integer n.
#   The implementation used here is iterative, because
#   it avoids recursion depth limits and is easier to
#   understand for large values of n.
#
# Inputs:
# - n (int)
#
# Outputs:
# - "n:" <n>
# - "Factorial:" <factorial_value>
#
# Validations:
# - n must be an integer
# - n >= 0
# - Optional: n <= 20 to avoid extremely large numbers
# - If validation fails, print "Error: invalid input"
#
# Test cases:
# 1) Normal:
#    Input: n=5
#    Expected: Factorial=120
#
# 2) Border:
#    Input: n=0
#    Expected: Factorial=1
#
# 3) Error:
#    Input: n=-3
#    Expected: "Error: invalid input"
# ----------------------------------------------------

def factorial(n):
    """Returns n! using an iterative approach."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# ---- Main program ----

# Ask user for input
user_input = input("Enter a non-negative integer: ")

# Validate that input is an integer
if user_input.isdigit():  # ensures digits only, no negatives
    n = int(user_input)

    # Validate range
    if 0 <= n <= 20:
        fact_value = factorial(n)
        print("n:", n)
        print("Factorial:", fact_value)
    else:
        print("Error: invalid input")
else:
    print("Error: invalid input")

# Conclusion
"""
En estos ejercicios pude aplicar y entender mejor varios métodos y conceptos 
clave de programación. Utilicé funciones definidas por el usuario para organizar 
el código en tareas específicas, como calculate_area(), classify_grade(), 
summarize_numbers(), apply_discount() y factorial(). También trabajé con métodos 
internos de Python como min(), max(), sum() y el uso de list comprehensions, que 
permiten procesar datos de forma más eficiente. Además, reforcé validaciones mediante 
métodos como .isdigit() y el manejo de errores usando try–except. En conjunto, estos 
métodos me ayudaron a estructurar programas más limpios, seguros y funcionales, lo cual 
es fundamental para desarrollar soluciones confiables en aplicaciones de mecatrónica.
"""
# Referencias
# https://ellibrodepython.com/funciones-en-python
# https://www.datacamp.com/es/tutorial/functions-python-tutorial
# https://ebac.mx/blog/funciones-de-python
# https://aprendeconalf.es/docencia/python/manual/funciones/
# https://aulavirtual.espol.edu.ec/courses/4558/pages/funciones-en-python