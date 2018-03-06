# # Uppercase a String
# mystring = "Uppercase this string!"
# print(mystring.upper())

# # Capitalize a String
# cap_string = "this string needs to be capitalized"
# print(cap_string.capitalize())

# # Reverse a String
# rev_string = "Hello There"
# print(rev_string[::-1])

# # Leetspeak
# def leetspeak(string):
#     leet = {"A":4,"E":3,"G":6,"I":1,"O":0,"S":5,"T":7}
#     for i in string.upper():
#         if i in leet:
#           print(leet.get(i), end="")
#         else:
#             print(i, end="")

# leetspeak("hello")


# # Leetspeak --> if want to print instead of calling function. Whole line print in terminal instead of joined with path.
# def leetspeak(string):
#     leet = {"A":4,"E":3,"G":6,"I":1,"O":0,"S":5,"T":7}
#     new_string = ''
#     for i in string.upper():
#         if i in leet:
#           new_string += str(leet.get(i))
#         else:
#             new_string += i
#     return new_string

# print(leetspeak("hello"))


# #Long-long Vowels
# def long_vowels(string):
#     l_string = ''
#     if "oo" in string:
#         l_string = string.replace("oo","ooooo")
#         return l_string
#     elif "ee" in string:
#         l_string = string.replace("ee","eeeee")
#         return l_string
#     else:
#         return "String does not contain long vowel"
            

# print(long_vowels("Cheese"))


# Caesar Cipher

# alph = {0: "a",1:"b", 2: "c", 3:"d"}
# alph2 = {"a":0,"b":1,"c":2,"d":3}
# string = "abc"
# e = 1
# for s in string:
#     num = alph2.get(s)
#     back = num + e
#     get = alph.get(back)
#     print(get,end='')