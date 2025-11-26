print("welcome to the debt elegibility system")
while True:#mientras qeu mis condiciones no se cumplan el codigo se repetira
    monthly_income=input("set your income\n")
    monthly_debt = input("set your monthly debt studio\n")
    credit_score = input("set your creditscore")

    try:#prueba que las entradas si sean compatibles con los datos requeridos
        income=float(monthly_income)
        debt=float(monthly_debt)
        score=int(credit_score)
        if income>0 and debt>=0 and score>=0:
            break
        else:
            print("Error: invalid input.") 
    except ValueError:#mensajes de error por formato incorrecto
        print("please insert a valid input")
debt_ratio=debt/income#calculo para el debt ratio
if income >=8000.0 and debt_ratio<=.4 and score>=650:#se busca por las condiciones de elgibilidad
    elegible=True
else:
    elegible= False
#salidas    
print(f"Debt ratio: {round(debt_ratio,2)}")
print(f"Eligible: {elegible}")