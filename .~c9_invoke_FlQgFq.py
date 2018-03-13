# Electronic Phone Book
# =====================
# 1. Look up an entry
# 2. Set an entry
# 3. Delete an entry
# 4. List all entries
# 5. Quit

# import json
# data = {'name': 'Paul'}
# with open('data.json', 'w') as fh:
#   json.dump(data, fh)
# with open('data.json', 'r') as fh:
#   data = json.load(fh)
#   print(data)

import pickle
print("Eletronic Phone Book")
print("====================")
print("1. Look up an entry")
print("2. Set an entry")
print("3. Delete an entry")
print("4. List all entries")
print("5. Quit")


def lookup():
    with open('phonebook.pickle', 'r') as f:
        phonebook = pickle.load(f)
        print(phonebook)
        
def app():
    quest = input("What do you want to do (1-5)? ")
    if quest == 1:
        lookup()
    elif quest == 2:
        set_entry()
        
def set_entry():
    name = input(Person's N)
    with open('data.pickle', 'wb') as fh:
      pickle.dump(data, fh)
app()
    
    
# lst = []
# lst.append({'fn':'b','ln':'d'})
# lst.append({'fn':'a', 'ln':'c'})
# print(lst)

# data=[
#     {
#         "Nelson": "222-222-2222"
#     },
#     {
#         "dgbgbrs": "333-333-3333"
#     }
# ]

# length = len(data)
# # print(length)
# # print(data[0])
# for n in range(length):
#     print(data[n])