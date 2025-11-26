"""
Name: <your_name>
Student ID: <your_student_id>
Group: <your_group>
Assignment: Lists, Tuples and Dictionaries in Python
"""

"""
EXECUTIVE SUMMARY

This document presents six problems involving Python collections:
lists, tuples, and dictionaries. A list is an ordered and mutable 
collection, meaning its elements can be modified, inserted or removed.
A tuple is also ordered but immutable, meaning its content cannot be
changed once created. Dictionaries store key-value pairs that allow
fast retrieval of information using descriptive identifiers.
The problems demonstrate practical applications such as catalogs,
records, basic statistics and CRUD operations. Each problem includes
descriptions, inputs, outputs and validations following good coding
practices.
"""

"""
PRINCIPLES AND BEST PRACTICES
Use lists when elements need to be added or removed frequently.
Use tuples for data that must remain unchanged (e.g., coordinates).
Use dictionaries when data must be accessed by a key (e.g., names).
Avoid modifying a list while iterating unless done intentionally.
Use descriptive key names in dictionaries (e.g., "name", "price").
Write readable code and clear user messages.
"""
"""
PROBLEM 1: Shopping list basics (list operations)
Description:
Manage a simple shopping list using list operations. The program 
starts with an initial list of items, allows adding a new item, 
shows the total number of items, and checks if a searched item exists.
Inputs:
initial_items_text (string, comma-separated list).
new_item (string).
search_item (string).
Outputs:
"Items list:" <items_list>
"Total items:" <len_list>
"Found item:" true|false
Validations:
initial_items_text must not be empty.
Remove extra spaces and split by commas.
new_item and search_item must not be empty.
Document handling of empty initial list.
"""
# (code goes here)

"""
PROBLEM 2: Points and distances with tuples
Description:
Create two coordinate points using tuples and compute the Euclidean 
distance between them. Also compute the midpoint as a new tuple.
Inputs:
x1, y1, x2, y2 (float values).
Outputs:
"Point A:" (x1, y1)
"Point B:" (x2, y2)
"Distance:" <distance>
"Midpoint:" (mx, my)
Validations:
All four inputs must be convertible to float.
"""
# (code goes here)

"""
PROBLEM 3: Product catalog with dictionary
Description:
Use a dictionary to represent a product catalog where each product 
name maps to its unit price. The program reads a product name and 
quantity, checks if the product exists, and computes the total cost.
Inputs:
product_name (string)
quantity (int)
Outputs:
If product exists:
  "Unit price:" <unit_price>
  "Quantity:" <quantity>
  "Total:" <total_price>
Otherwise:
  "Error: product not found"
Validations:
quantity > 0
product_name must not be empty
The key must exist in the dictionary
"""
# (code goes here)

"""
PROBLEM 4: Student grades with dict and list
Description:
Manage student records using a dictionary where each key is a student 
name and each value is a list of grades. Compute the average and 
determine whether the student passes.
Inputs:
student_name (string)
Outputs:
If student exists:
  "Grades:" <grades_list>
  "Average:" <average>
  "Passed:" true|false
Otherwise:
  "Error: student not found"
Validations:
student_name must not be empty
student must exist in the dictionary
grades list must not be empty before averaging
"""
# (code goes here)

"""
PROBLEM 5: Word frequency counter (list + dict)
Description:
Count the frequency of each word in a sentence. Convert the sentence 
to lowercase, split into words, and build a frequency dictionary. 
Display the most common word.
Inputs:
sentence (string)
Outputs:
"Words list:" <words_list>
"Frequencies:" <freq_dict>
"Most common word:" <word>
Validations:
sentence must not be empty
optional: handle punctuation using replace()
words list must not be empty
"""
# (code goes here)

"""
PROBLEM 6: Simple contact book (dictionary CRUD)
Description:
Implement a basic contact book using a dictionary. The program 
supports three actions: ADD, SEARCH, DELETE.
Inputs:
action_text ("ADD", "SEARCH", or "DELETE")
name (string)
phone (string only for ADD)
Outputs:
For ADD:
  "Contact saved:" name, phone
For SEARCH:
  "Phone:" <phone> or "Error: contact not found"
For DELETE:
  "Contact deleted:" name or "Error: contact not found"
Validations:
action_text must be uppercase and valid
name must not be empty
phone must not be empty for ADD
"""
# (code goes here)


#
# CONCLUSIONS
#
# Lists provide flexibility for adding or removing elements and are
# ideal for dynamic collections. Tuples are useful when data must
# remain unchanged, such as coordinates or fixed records. Dictionaries
# allow fast lookups using descriptive keys and support structured data.
# Combining these collections enables powerful patterns such as 
# dictionaries of lists or lists of dictionaries, which frequently 
# appear in real-world applications. This assignment reinforces 
# practical handling of each structure.

#
# REFERENCES
#
# References:
# 1) Python documentation Built-in Types: list, tuple, dict
# 2) Python Software Foundation – The Python Tutorial
# 3) Automate the Boring Stuff with Python – Chapter on Data Structures
# 4) Real Python – Python Data Structures Guide
# 5) W3Schools Python Collections Reference

#
# GITHUB REPOSITORY
#
# GitHub URL: <insert_your_repository_url_here>
