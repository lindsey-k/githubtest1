"""
BMI 6018 – Lists, Sets, Coercion, Dicts, and Types
Answer file: all answers are returned as variables with names like one_a, two_b, etc.
No imports used.
"""

# ----------------------------
# Example Problem (given)
# ----------------------------
zero_a = ['first','second','third','fourth','fifth']
zero_b = zero_a[1].upper()
zero_c = hex(ord(zero_a[1][1]))

# ----------------------------
# Problem 1: Lists, Sets and Coercion
# ----------------------------

# 1.a Create a list of integers no fewer than 10 items from 0 to 9.
one_a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 1.b Add 3 to the 5th indexed element
one_b = one_a[5] + 3  # 5th index is value 5 -> 8

# 1.c Coerce all elements in the list to floats using list comprehension
one_c = [float(x) for x in one_a]

# 1.d Coerce the list to a set
one_d = set(one_a)

# 1.e Using a method, append int 10 to the set
_one_e_work = set(one_d)
_one_e_work.add(10)
one_e = _one_e_work

# 1.f Using a method, pop an item from the set
_one_f_work = set(one_e)
_ = _one_f_work.pop()  # value popped is arbitrary; assignment cares about the operation/result
one_f = _one_f_work  # resulting set after the pop

# 1.g Using a length counting function, count the number of items in the set
one_g = len(one_f)

# 1.h Check if the number of items in the set is the same as the number of items in the list
one_h = (len(one_f) == len(one_a))

# 1.i Coerce the set to a list and use the "+" operator to combine with list from 1.a
one_i = list(one_f) + one_a

# 1.j Coerce 1.i to a set
one_j = set(one_i)

# 1.k Count the number of elements in the 1.j
one_k = len(one_j)


# ----------------------------
# Problem 2: Dictionary woes
# ----------------------------

two_patient_dictionary_kinoko = {
  "name" : "Kinoko",
  "year" : 2021
}
two_patient_dictionary_dango = {
  "name" : "Dango",
  "year" : 2019
}
two_patient_dictionary_mochi  = {
  "name" : "Mochi",
  "year" : 2020
}

# 2.a Combine the three sample dictionaries into a nested dictionary named two_a.
#     Keys should be the same as the original dictionary variable names.
two_a = {
    "two_patient_dictionary_kinoko": two_patient_dictionary_kinoko,
    "two_patient_dictionary_dango": two_patient_dictionary_dango,
    "two_patient_dictionary_mochi": two_patient_dictionary_mochi,
}

# 2.b Using keys, retrieve Dango's name from 2.a
two_b = two_a["two_patient_dictionary_dango"]["name"]

# 2.c Using keys, update the value of Mochi's year to 2018 (update 2.a directly)
two_a["two_patient_dictionary_mochi"]["year"] = 2018
# Provide the updated value as the answer variable as well (for autograding convenience)
two_c = two_a["two_patient_dictionary_mochi"]["year"]  # 2018

# 2.d Manually create a single-level dictionary {patient: year}, with Mochi's year set to 2019
two_d = {
    "Kinoko": 2021,
    "Dango": 2019,
    "Mochi": 2019,
}

# 2.e Coerce the keys of 2.d into a list
two_e = list(two_d.keys())

# 2.f Coerce the values of 2.d into a list
two_f = list(two_d.values())

# 2.g Use zip to combine 2.e and 2.f back into a dictionary
two_g = dict(zip(two_e, two_f))


# ----------------------------
# Problem 3: Set combinations
# ----------------------------

three_setA = {1,2,3,4,5}
three_setB = {2,3,4,5,6}
three_setC = {3,5,7,9}
three_setD = {2,4,6,8}
three_setE = {1,2,3,4}

# 3.a Is set E a subset of set A
three_a = three_setE.issubset(three_setA)

# 3.b Is set E a strict subset (proper subset) of set A
three_b = three_setE < three_setA  # True if E is subset of A and not equal to A

# 3.c Intersection of set A and set B
three_c = three_setA.intersection(three_setB)

# 3.d Union of sets C, D and E
three_d = three_setC.union(three_setD, three_setE)

# 3.e add 9 to the set
_three_e_work = set(three_d)
_three_e_work.add(9)  # (9 is already present, but operation still valid)
three_e = _three_e_work

# 3.f Using == compare this set to the list in one_a
three_f = (three_e == one_a)  # False: different types (set vs list)

# 3.g Explain why they are not the same, and what to change to make it True
three_g = (
    "They are not equal because the types differ (set vs list) and the elements differ (three_e lacks 0). "
    "To make it True, compare sets and include 0: set(one_a) == (three_e | {0})."
)


# ----------------------------
# Problem 4: Changing variable types
# For each step, modify the numeric variable and append its type to a running list.
# ----------------------------

# 4.a Create a variable of type int with the value of 8
four_a = 8

# 4.b Create an empty list (this will be our running list of types)
four_b = []

# 4.c Using type(), add the type of 4.a to this list
four_b.append(type(four_a))
four_c = four_b  # alias to show the state after this step

# 4.d Add 0.39 to the numeric variable
four_d = four_a + 0.39

# 4.e append the type of (the new numeric variable) to the list
four_b.append(type(four_d))

# 4.f exponentiate to the -10 (four_d ** -10), round to 0 decimals, and append type to list
four_f = round(four_d ** -10, 0)
four_b.append(type(four_f))

# 4.g append the type of the list itself to the list (keeps the "running" idea visible)
four_b.append(type(four_b))
four_g = four_b  # current snapshot/reference


# ----------------------------
# Problem 5: More variable type changes (continue from Problem 4)
# ----------------------------

# 5.a Manually create a dictionary where values are items in the list from Problem 4
#     and keys are their index in the list. Print the dictionary.
five_a = {i: v for i, v in enumerate(four_b)}
print(five_a)

# 5.b Add 300 and coerce it into a string
five_b = str(300)

# 5.c append the type to the list
four_b.append(type(five_b))
five_c = four_b  # snapshot

# 5.d slice the string up to the 2nd element
five_d = five_b[:2]  # "30"

# 5.e append the type to the list
four_b.append(type(five_d))
five_e = four_b  # snapshot

# 5.f use list comprehension to convert this into a new list of integers
five_f = [int(ch) for ch in five_d]  # [3, 0]

# 5.g append the type to the list
four_b.append(type(five_f))
five_g = four_b  # snapshot

# 5.h append the type of three_setA to the list
four_b.append(type(three_setA))
five_h = four_b  # final snapshot/reference of the running types list


# EOF
if __name__ == "__main__":
    print("Assignment 3 ready.")
