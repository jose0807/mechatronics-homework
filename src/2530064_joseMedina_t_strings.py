# nombre : Jose Carlos Medina Lopez
# matricula: 2530064
# mecatronica 1-1



#resumen
"""
En Python, un string es un tipo de dato inmutable que representa una secuencia
de caracteres y permite operaciones como concatenación, slicing, búsqueda,
reemplazo y formato de texto. Su inmutabilidad implica que cada modificación
genera una nueva cadena, lo cual exige un manejo cuidadoso y estructurado.
La validación y normalización de entradas —como eliminar espacios, ajustar
mayúsculas/minúsculas y verificar patrones simples— es esencial para evitar
errores y garantizar la calidad de los datos procesados.
Este documento desarrolla seis problemas que aplican estos principios,
describiendo entradas, salidas, validaciones, métodos de string y casos
de prueba concretos para cada ejercicio.

"""
"""
PRINCIPLES AND BEST PRACTICES

- Strings are immutable: every modification creates a new string, so operations
  must be planned to avoid unnecessary processing.
- It is good practice to normalize input using strip(), lower(), and split()
  before validating or comparing text.
- Avoid magic numbers in slices; always document why specific index ranges
  are used when extracting substrings.
- Prefer built-in string methods (replace, find, split, join) instead of
  manually re-implementing basic text logic.
- Design validations in a clear order: first check for empty input, then format,
  then content.
- Write readable code with descriptive variable names and consistent output
  messages in English.
"""

"""
Problem 1: Full name formatter (name + initials)
Description:
given a person's full name in a single string the progtam must:
1) normalize the name (uppercase, lowercase, strip, extra spaces)
2) show the formated name in title case antd initials (for example: J.C.T.).

inputs:
- full_name (string; full name, might come in uppercase, lowercase, or mixed with extra spaces).

outputs:
- "Formatted name: <Name In Title Case>"
- "Initials: <X.X.X.>"

Validations:
- full_name must not be empty after strip().
- must at least contain two words (for example, name y surname).
- must not accept strings made of just spaces.
test cases:

1) Normal
Input: "juan carlos tovar"
Output:
formatted name : Juan Carlos Tovar
initials: J.C.T

2) Border
Input: " ana   lu "
Output:
formatted name : Ana Lu
initials: A.L

3) Error
Input: "     Pedro"
Output:
invalid input please reset the program.
"""

full_name = input("introduce your full name\n")
list=full_name.split()
if full_name.isspace() or len(list)<2 : #FULL NAME MUST NOT BE BLANK OR LESS THAN TWO WORDS
    print ("invalid input please reset the program.")
else:
    name_lower =full_name.lower().split() #THIS SPLITS THE STRING IN SEVERAL PARTS AND NORMALIZES IT IN LOWERCASE
    formatted_name= " "
    for names in name_lower: 
        formatted_name = formatted_name + " " + names #PUTS EVERY PART OF THE STRING TOGETHER CREATING A CORRECT STRUCTURE
    print(f"formatted name :{formatted_name.title().strip()}") #PRINTS THE CORRECT STRUCTURE AND MAKES SURE THERE ARE NO EXTRA SPACES
    initials=" "
    for word in formatted_name.title():#SEPARATES THE WORD IN CHARACTERS
        if word.isupper(): #ASKS IF THE CHARACTER IS AN UPPERCASE
            initials= initials +"."+  word # KEEPS ALL THE UPPER CASES IN A SINGLE STRING
    print (f"initials: {initials.strip('.')}") #PRITNS AND GETS RID OF THE INITIAL POINT THAT LEAVES THE ALGORITHM
    

"""
Problem 2: Simple Email Validator (structure + domain)
Description:
This program checks whether an email address follows a basic valid structure.
It must contain exactly one '@', include at least one '.' after the '@',
and must not contain whitespace. If the email is valid, the domain part
is extracted and shown.

Inputs:
- email_text (string): the email provided by the user.
Outputs:
- "Valid email: true" or "Valid email: false"
- If valid: "Domain: <domain_part>"
Validations:
- Input must not be empty after strip().
- Must contain exactly one '@'.
- Must contain no spaces.
- Must contain at least one '.' in the domain.
Test Cases:
Test cases:

1) Normal
Input: "usuario@gmail.com"
Output:
valid e-mail: True
@gmail.com

2) Border
Input: "  a@b.co  "
Output:
valid e-mail: True
@b.co

3) Error
Input: "user@@mail.com"
Output:
valid e-mail: False

"""
#CODIGO
mail = input("set your e-mail\n")
mail = mail.strip(" ")#normalizamos las entradas
lenght = len(mail)#contamos la longitud del mensaje
num = mail.find("@")#buscamos un @
point = mail.find(".",num) # buscamos un . despues de el @
if "@" not in mail or num > point or mail.count("@")>1 or " " in mail or lenght == 0 or point== lenght-1:#verificamos que tenga @que el punto este despues de @ ylas demas condiciones
    email = False 
    print (f"valid e-mail:{email}")
else :
    email = True
    print(f"valid e-mail:{email}")
    print (mail [num:lenght])
    

"""
PROBLEM 3: Palindrome Checker (ignoring spaces and case)

Description:
Determines whether a phrase is a palindrome by removing spaces and ignoring
case, then comparing the normalized phrase to its reverse.
Inputs:
phrase (string)
Outputs:
"Is palindrome: true/false"
(Optional) "Normalized phrase: <text>"
Validations:
Input must not be empty after strip().
Normalized phrase must have at least 3 characters.
Test Cases:
Test cases:

1) Normal
Input: "Anita lava la tina"
Output:
anitalavalatina
anitalavalatina
is palindrome: True

2) Border
Input: "A b A"
Output:
aba
aba
is palindrome: True

3) Error
Input: "  a "
Output:
is palindrome: False

"""
#codigo

word = input ("set your palindrome \n")
if word.strip().isspace()or len(word.strip())<3:#preguntamos si la palabra es espacio o si su longitud es menor a 3 caracteres
    is_palindrome= False 
else:
    word="".join(word.lower().strip().split())#unimos todo e ignoramos los espacios
    word2 = word[::-1]#ordenamos la palabra al revez ahora sin espacios
    if word2 == word: #compara las dos strings resultantes
        is_palindrome =True
    else:
        is_palindrome = False
print(f"is palindrome:{is_palindrome}")

"""
PROBLEM 4: Sentence Word Stats (lengths and first/last word)
Description:
Analyzes a sentence and outputs word statistics: total word count, first
word, last word, shortest word, and longest word.
Inputs:
- sentence (string)
Outputs:
- "Word count: <n>"
- "First word: <...>"
- "Last word: <...>"
- "Shortest word: <...>"
- "Longest word: <...>"
Validations:
- Input must not be empty after strip().
- There must be at least one word after splitting.
Test Cases:
Test cases:

1) Normal
Input: "  the quick brown fox jumps  "
Output:
the quick brown fox jumps
your word count is 5
your first word is the
your last word is jumps
your longest word is jumps with a lenght of 5
your shortest word is the with a lenght of 3

2) Border
Input: "hello"
Output:
hello
your word count is 1
your first word is hello
your last word is hello
your longest word is hello with a lenght of 5
your shortest word is hello with a lenght of 5

3) Error
Input: "      "
Output:
invalid input please retry

"""
#codigo

phrase = input("please set your sentence\n")
phrase=phrase.strip()#eliminamos los espacios extra
longest=0#inicializamos la variable longest
shortest =len(phrase)+1 #le damos un valor grande a la variable shortest
shortest_word="" #inicia la variable de shortest 
longest_word="" #inicia la variable de longest
print (phrase)
if phrase.isspace():
    print ("invalid input please retry")
else:
    phrase= phrase.strip()
    word_count= phrase.split()
    for word in word_count:#busca palabra por palbra 
        num=len(word)# iguala la longitud de la palabra a una variable
        if longest < num:#si numero es mayor a longest
            longest = len(word) #el valor de num pasa a ser el valor de longest
            longest_word= word #la palabra se guarda en la variable longest_word
    for word in word_count:#busca en todas las palabras 
            short =len(word)# el valor de len es igual a la longitud de la palabra
            if shortest>short:#si shortest es mayor a short
                 shortest= short #el valor de shortest pasa a ser short
                 shortest_word= word # el valor de word se guarda en la variable shortest word
    print(f"your word count is {len(word_count)}")
    print(f"your first word is {word_count[0]}")
    print(f"your last word is {word_count[-1]}")
    print(f"your longest word is {longest_word} with a lenght of {longest}")
    print(f"your shortest word is {shortest_word} with a lenght of {shortest}")

"""

PROBLEM 5: Password Strength Classifier
Description:
Classifies a password as weak, medium, or strong depending on the presence
of uppercase letters, lowercase letters, digits, and special characters.
Inputs:
- password_input (string)
Outputs:
- "Password strength: weak/medium/strong"
Validations:
- Password must not be empty.
- Must check length using len().
Test Cases:
Test cases:

1) Normal
Input: "Abc123$X"
Output:
8
password strenght:strong

2) Border
Input: "Abcdefgh"
Output:
8
password strength:medium

3) Error
Input: ""
Output:
0
must set a password, please retry

"""
#codigo
password=input("please set your password\n")
size= len(password) 
print(size)
is_strong= False
has_upper=False
has_lower=False
has_num=False
has_special=False
if size==0:#evalua que la contraseña no este vacia
    print ("must set a password, please retry")
elif size<8:#si la contraseña tiene menos de 8 caracteres te dice que es debil
     print("your password is weak")
elif size>=8:#si tu contraseña supera los 8 caracteresevalua las demas caracteristicas que pide
    for character in password:
        if character.isupper():
            has_upper=True
        elif character.islower():
            has_lower=True
        elif character.isdigit():
            has_num=True
        elif not character.isalnum():
            has_special=True
    if has_upper==True and has_lower==True and has_num==True and has_special== True:#si lo tiene todo es fuerte
        is_strong=True
    if is_strong== True:#si es fuerte imprimir password is strong
        print("password strenght:strong" )
    elif has_upper==True and has_lower==True or has_num==True:
        print("password strength:medium")#si no tiene todas las caracteristicas es medium
    
    else:
        print("password strength:medium")


"""
PROBLEM 6: Product Label Formatter (fixed-width text)

Description:
Creates a product label with the format:
Product: <NAME> | Price: $<PRICE>
The final string must be exactly 30 characters; shorter strings are padded
with spaces and longer strings are trimmed.
Inputs:
- product_name (string)
- price_value (string or number)
Outputs:
- "Label: <exactly 30 characters>"
Validations:
- product_name must not be empty after strip().
- price_value must be convertible to a positive number.
Test Cases:
Test cases:

1) Normal
Input:
name = "Laptop"
price = "12999"
Output:
label:'product: Laptop | price: $12999   '

2) Border
Input:
name = "USB"
price = "99"
Output:
label:'product: USB | price: $99       '

3) Error
Input:
name = "  "
price = "500"
Output:
please set a valid number or name

4) Error (price no numérico)
Input:
name = "Mouse"
price = "abc"
Output:
please set a valid number

"""
#codigo
name=input("please set your product:\n")
price= input("please set the price\n")
data = (f"product: {name.strip()} | price: ${price.strip()}") #normaliza todo quitando espacios y lo ingresa al formato indicado
try:#intenta convertir la 2da entrada en float y evaluar  que el 1er caracter
    cost=float(price)
    if cost <0 or len(name.strip())==0 or not name.strip().isalpha():#evaluaque el nombre sea alfanumerico y que el costo sea mayor a 0
        print("please set a valid number or name")
    else:
        if len(data)==30:#evaluan que el string sea de 30 caracteres
            print(f"label:'{data}'")
        elif len(data)>30:#si el dato es mayor a 30 lo recorta hasta que tenga 30 caracteres
            print(f"label:'{data[:30]}'")
        elif len(data)<30:#si el dato es menor a 30 le agrega espacios hasta que lleguen a los 30 caracteres
            while len(data)<30:
                data=data+" "
            print(f"label:'{data}'")
except ValueError:# 
    print("please set a valid number")

"""
 CONCLUSIONS

 String handling is fundamental in software development because most user
 interactions occur through text. Normalizing input with methods such as
 strip(), lower(), and split() helps avoid errors and inconsistencies.
 Validating input prevents incorrect or unsafe data from being processed.
 Through these exercises, the importance of immutability, string slicing,
 and built-in string methods becomes clear. The problems reinforce practical
 scenarios where proper text manipulation leads to cleaner, safer, and more
 reliable programs.
"""
"""
REFERENCES:

1) Python Documentation – Built-in Types: Text Sequence Type — str
   https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str

2) PEP 8 – Style Guide for Python Code (Naming conventions)
   https://peps.python.org/pep-0008/

3) Real Python – “Working With Strings in Python”
   https://realpython.com/python-strings/

4) W3Schools – Python Strings
   https://www.w3schools.com/python/python_strings.asp

5) Automate the Boring Stuff with Python – Input Validation Basics
   https://automatetheboringstuff.com/

6) GeeksForGeeks – String Methods in Python
   https://www.geeksforgeeks.org/python-string-methods/
"""

    


