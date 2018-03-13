import pickle

while True:
    print("Electronic Phone Book")
    print("=====================")
    print("1. Look up an entry")
    print("2. Set an entry")
    print("3. Delete an entry")
    print("4. List all entries")
    print("5. Save entries")
    print("6. Restore saved entries")
    print("7. Quit")
    
            
    phonebook = {}        
    def app():
        lookup()
        quest = int(input("What do you want to do (1-7)? "))
        if 0 < quest < 8:
            if quest == 1:
                specific_lookup()
            elif quest == 2:
                set_entry()
                save_entry()
            elif quest == 3:
                delete_entry()
            elif quest == 4:
                lookup()
                for k, v in phonebook.items():
                    print ('Name: {}  Phone Number: {}'.format(k, v.get("Phone Number")))
            elif quest == 5:
                save_entry()
            elif quest == 6:
                lookup()
            else:
                print("Until Next Time!")
                quit()
        else:
            print("Please pick a number from 1-7")
            
    
    def lookup():
        global phonebook
        with open('data.pickle', 'rb') as f:
            phonebook = pickle.load(f)
        
    def specific_lookup():
        person = input("Person Name: ")
        lookup()
        if person in phonebook:
            for n in range(1):
                print("Phone Number: " + phonebook[person]["Phone Number"])
        else:
            print("Person not in phonebook")
            
    def set_entry():
        name = input("Person's Name: ")
        phone = input("Person's Phone: ")
        phonebook[name] = {}
        phonebook[name]["Phone Number"] = phone
        print("An Entry has been created for {}".format(name))
        
    def save_entry():
        with open('data.pickle', 'wb') as f:
            pickle.dump(phonebook, f)
            
    def delete_entry():
        person = input("Person Name: ")
        lookup()
        if person not in phonebook:
            print("{} not in phonebook!".format(person))
        else:
            del phonebook[person]
            save_entry()
            print("Deleted: {}".format(person))
        
        
        
    app()
