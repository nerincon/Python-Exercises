class Person:
    
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0
        self.unique_greeted = []
        
    #OR(You can __repr__ this way if you want contact info for friends to be displayed this way. Only thing is that you will have to have friends attribute in Person Class)
    # def __repr__(self):
    #     return "Friend's Name: {}, Friend's Email: {}, Friend's Phone: {}".format(self.name, self.email, self.phone)
        
    def __repr__(self):
        return "{self.__class__.__name__}: {self.name} {self.email} {self.phone}".format(self=self)

    def greet(self, other_person):
        print('Hello {}, I am {}!'.format(other_person.name, self.name))
        self.greeting_count += 1
        self.unique_greeted.append(other_person.name)
        
    def contact_info(self):
        print("{}'s Email: {}, {}'s Phone Number: {}".format(self.name, self.email, self.name, self.phone))
        
    def add_friend(self, friend):
        return self.friends.append(friend.name)
        
    def num_friends(self):
        print(len(self.friends))
        
    def num_unique_people_greeted(self):
        uniques = set(self.unique_greeted)
        uniques_greeted = list(uniques)
        print(len(uniques_greeted))
        


#DON'T NEED THIS. JUST EXAMPLE OF INHERITANCE/ NEED IF EVERY PERSON WILL HAVE SOMETHING THAT THE PERSON CLASS WILL NOT HAVE---------------        
# class Sonny(Person):
#     def __init__(self, age, name, email, phone, friends):
#         super().__init__(name, email, phone, friends)
        
# class Jordan(Person):
#     def __init__(self, name, email, phone, friends):
#         super().__init__(name, email, phone, friends)

#-----------------------------------------------------------

#1-2(one extra name)
sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
jordan = Person("Jordan", "jordan@hotmail.com", "295-586-3456")
nelson = Person("Nelson", "nerincon1@gmail.com", "786-241-7822")


#3-4
sonny.greet(jordan)
sonny.greet(jordan)
sonny.greet(jordan)

jordan.greet(sonny)
jordan.greet(nelson)
jordan.greet(sonny)
jordan.greet(nelson)

# 5-6
sonny.contact_info()
jordan.contact_info()

#Append Friends
jordan.add_friend(sonny)
jordan.add_friend(nelson)
sonny.add_friend(jordan)

# Num Friends
jordan.num_friends()
sonny.num_friends()


# Count of Greetings
print(sonny.greeting_count)
print(jordan.greeting_count)

# Count of Unique Greetings
jordan.num_unique_people_greeted()
sonny.num_unique_people_greeted()

# Extra - Print Friends
print(jordan.friends)
print(sonny.friends)

# To Represent Person Object
print(jordan)


# 2. Make your own class
class Vehicle():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
    def print_info(self):
        print("{} {} {}".format(car.make, car.model, car.year))
        
car = Vehicle('Nissan', 'Leaf', 2015)
print(car.make, car.model, car.year)
car.print_info()



