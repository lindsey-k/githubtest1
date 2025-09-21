#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


#"""BMI 6018 Fall 2022 

#Problem 1: Lists, Sets and Coersion

#1.a Create a list of integers no fewer than 10 items from 0 to 9.
one_a = [0,1,2,3,4,5,6,7,8,9]
 #.b Add 3 to the 5th indexed element
one_b = one_a[5] + 3
 #.c Coerce all elements in the list to floats using list comprehension
one_c = [float(x) for x in one_a]
 #.d Coerce the list to a set
one_d = set(one_a)
 #.e Using a method, append int 10 to the set
one_e = set(one_d)
one_e.add(10)
 #.f Using a method, pop an item from the set
one_f = set(one_e)
one_f.pop()
 #.g Using a length counting function, count the number of items in the set
one_g = len(one_f)
 #.h Check if the number of items in the set is the same as the number of items in the list
one_h = (len(one_f) == len(one_a))
 #.i Coerce the set to a list and use the "+" operator combine the list to the list from 1.a
one_i = list(one_f) + one_a
 #.j Coerce 1.i to a set
one_j = set(one_i)
 #.k Count the number of elements in the 1.j
one_k = len(one_j)


#Problem 2: Dictionary woes

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




#2.a Combine the three sample dictionaries (given below) into a nested dictionary (nested in programming means joined), named 
    #two_a, ensure the key names are the same as the dictionary names.
two_a = { 
    "two_patient_dictionary_kinoko": two_patient_dictionary_kinoko,
    "two_patient_dictionary_dango": two_patient_dictionary_dango,
    "two_patient_dictionary_mochi": two_patient_dictionary_mochi,
}
 #.b Using keys, retrieve the Dango's name from 2.a
two_b = two_a["two_patient_dictionary_dango"]["name"]
 #.c Using keys, update the value of Mochi's year to 2018. This should not be a variable
    #and should simply update 2.a.
two_a["two_patient_dictionary_mochi"]["year"] = 2018
two_c = two_a["two_patient_dictionary_mochi"]["year"]
 #.d Manually create a dictionary that has a single level and contains each patient
    #as the key and the year as the value. Set Mochi's year to 2019.'
two_d = {"Kinoko": 2021, "Dango": 2019, "Mochi":2019}
 #.e Coerce the keys of 2.d into a list
two_e = list(two_d.keys())
 #.f Coerce the values of 2.d into a list
two_f = list(two_d.values())
 #.g Use the zip function to combine 2.e and 2.f into a dictionary again
two_g = dict(zip(two_e, two_f))



#Problem 3: Set combinations

three_setA = {1,2,3,4,5}
three_setB = {2,3,4,5,6}
three_setC = {3,5,7,9}
three_setD = {2,4,6,8}
three_setE = {1,2,3,4}


#Given the predefined sets below and using set methods
#3.a Is set E a subset of set A
three_a = three_setE.issubset(three_setA)
 #.b Is set E a strict subset of set A
three_b = three_setE < three_setA
 #.c Create a set that is the intersection of set A and set B
three_c = three_setA & three_setB
 #.d Create a set that is the union of sets C, D and E
three_d = three_setC | three_setD | three_setE
 #.e add 9 to the set
three_e = set(three_d)
three_e.add(9)

#.f Using == compare this set to the list in one_a
three_f = (three_e == one_a)

#.g Explain why they are not the same. What would you need to change if you
    #wanted this to be True?
three_g = (
    "Not the same because set and list and elements differ You would need to compare sets and include 0: set(one_a) == (three_e) | {0}."
)




#Problem 4: Changing variable types

#For each step you will modify a variable, then append the type of the variable
#to a list. Do not recreate the list variable, it should be a running list of 
#types.

#4.a Create a variable of type int with the value of 8
four_a = 8
 #.b Create an empty list 
four_b = []
 #.c Using type(), add the type of 4.a to this list
four_b.append(type(four_a))
four_c = four_b
 #.d Add 0.39 to 4.c
four_d = four_a + 0.39
# 4.e append the type of (the new numeric variable) to the list
four_b.append(type(four_d))
 #.f exponentiate to the -10, ie: 4.d^-10,(hint: there might be an artihmetic operator to do so) round it to no 
    #decimal places, and append to list.
four_f = round(four_d ** -10, 0)
four_b.append(type(four_f))
 #.g append the type to the list
four_b.append(type(four_b))
four_g = four_b
 
 
#Problem 5: More variable type changes

#Continue from where you left off in Problem 4.

#5.a Manually create a dictionary where the values are items in the list from where we left in 
    #problem 4, and the keys should be their index in the list. Print the dictionary.
five_a = {i: v for i, v in enumerate(four_b)}
print(five_a)

 #.b Add 300 and coerce it into a string
five_b = str(300)

 #.c append the type to the list
four_b.append(type(five_b))
five_c = four_b

 #.d slice the string up to the 2nd element
five_d = five_b[:2]

 #.e append the type to the list
four_b.append(type(five_d))
five_e = four_b

 #.f use list comprehension to convert this into a new list of integers
five_f = [int(ch) for ch in five_d]

 #.g append the type to the list
four_b.append(type(five_f))
five_g = four_b

 #.h append the type of three_setA to the list
four_b.append(type(three_setA))
five_h = four_b

#Start your assignment here
print("Assignment 3")


