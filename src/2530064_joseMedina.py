# Name: Jose Carlos Medina Lopez
# Student ID: 2530064
# Group: 1-1


# EXECUTIVE SUMMARY
# In Python, integers (int) represent whole numbers, while floats represent
# numbers with decimals. Booleans (True/False) are logical values produced
# mainly from comparisons and conditional expressions. Validating numerical
# ranges is essential to prevent runtime errors, including division by zero,
# negative values where not allowed, or impossible physical conditions.
# This document includes six problems using ints, floats, and booleans to
# perform arithmetic, comparisons, logical evaluations, decisions, and data
# validation. Each problem contains a description, inputs, outputs, and
# validations following the project's specifications.

# PRINCIPLES AND BEST PRACTICES
# - Use appropriate data types: int for counters, float for decimal values.
# - Avoid repeating complex expressions: store intermediate results in variables.
# - Validate all user inputs before operating (non-negative values, correct ranges).
# - Use descriptive variable names and clear output messages for the user.
# - Document the meaning of boolean values in each context so the program is easy
#   to interpret and maintain.
"""
PROBLEM 1: Temperature converter and range flag
Description:
Converts a temperature in Celsius to Fahrenheit and Kelvin. Also determines
a boolean flag indicating whether the Celsius temperature is high (>= 30.0).
Inputs:
temp_c (float)
Outputs:
"Fahrenheit:" <temp_f>
"Kelvin:" <temp_k>
"High temperature:" true|false
Validations:
temp_c must be convertible to float.
Kelvin temperature must not be physically impossible (>= 0.0).

"""
# (CODE HERE)

temp = input("set your temperature in celsius\n")
high_temp=False
try:
    celcious=float(temp)
    if celcious >-273.15:
        fahrenheit = (celcious*9/5)+32
        kelvin = celcious+273.15
        print(f"fahrenheit: {fahrenheit}")
        print(f"kelvin: {kelvin}")
        if celcious>= 30:
            high_temp=True
        
        print(f"high temperature: {high_temp}")
    else:
        print("Error:invalid input")
    
except ValueError:
    print("error : invalid input")
"""
PROBLEM 2: Work hours and overtime payment
Description:
Calculates total weekly payment including overtime at 150% of the hourly rate
when hours worked exceed 40. Determines a boolean indicating overtime.
Inputs:
hours_worked (float)
hourly_rate (float)
Outputs:
"Regular pay:" <regular_pay>
"Overtime pay:" <overtime_pay>
"Total pay:" <total_pay>
"Has overtime:" true|false
Validations:
hours_worked >= 0
hourly_rate > 0
If not satisfied, print "Error: invalid input".
"""

# (CODE HERE)

"""
PROBLEM 3: Discount eligibility with booleans
Description:
Determines if a customer is eligible for a discount based on student status,
senior status, or purchase total. Applies a 10% discount when eligible.
Inputs:
purchase_total (float)
is_student_text ("YES" or "NO")
is_senior_text ("YES" or "NO")
Outputs:
"Discount eligible:" true|false
"Final total:" <final_total>
Validations:
purchase_total >= 0.0
is_student_text and is_senior_text must be "YES" or "NO"
Otherwise print "Error: invalid input".
"""

# (CODE HERE)


"""
PROBLEM 4: Basic statistics of three integers
Description:
Reads three integers and calculates sum, average, maximum, minimum, and a
boolean indicating whether all three numbers are even.
Inputs:
n1 (int)
n2 (int)
n3 (int)
Outputs:
"Sum:" <sum_value>
"Average:" <average_value>
"Max:" <max_value>
"Min:" <min_value>
"All even:" true|false
Validations:
All three values must be convertible to int.
"""

# (CODE HERE)

"""
PROBLEM 5: Loan eligibility (income and debt ratio)
Description:
Determines whether a person qualifies for a loan based on income, debt ratio,
and credit score.
Inputs:
- monthly_income (float)
- monthly_debt (float)
- credit_score (int)
Outputs:
- "Debt ratio:" <debt_ratio>
- "Eligible:" true|false
Validations:
- monthly_income > 0.0
- monthly_debt >= 0.0
- credit_score >= 0
- Otherwise print "Error: invalid input".
"""

# (CODE HERE)

"""
PROBLEM 6: Body Mass Index (BMI) and category flag
Description:
Calculates BMI and evaluates whether a person is underweight, normal, or
overweight using boolean flags.
Inputs:
weight_kg (float)
height_m (float)
Outputs:
"BMI:" <bmi_rounded>
"Underweight:" true|false
"Normal:" true|false
"Overweight:" true|false
Validations:
weight_kg > 0.0
height_m > 0.0
Otherwise print "Error: invalid input".
 """

#(CODE HERE)


# CONCLUSIONS
# Integers and floats work together in many real-life calculations, allowing
# programs to model quantities, rates, and ratios. Boolean values arise from
# comparisons and form the basis of decisions through if-statements. Proper
# validation prevents incorrect results and runtime errors such as division by
# zero or negative values where they are not allowed. Logical operators like
# and, or, and not enable complex conditions such as discount eligibility,
# loan approval, and category classification. These patterns are present in
# payroll systems, financial evaluations, and measurement tools.

# REFERENCES
# References:
# 1) Python documentation – Built-in Types: Numeric Types (int, float)
# 2) Python documentation – Boolean type (bool)
# 3) Python documentation – Expressions and operators
# 4) Python tutorial – Input validation and exception handling
# 5) Introductory Programming textbooks and course notes
#
# GITHUB REPOSITORY
# URL: ______________________________________________
