class Person():
    def __init__(self, name):
        self.name = name
        
    def greet(self, friend):
        print("Hello {} I'm {}".format(friend.name, self.name))

me = Person("Nelson")
f = Person("Paula")
me.greet(f)

#OR-------------

class Person():
    def __init__(self, name):
        self.name = name
        
    def greet(self, friend):
        print("Hello {} I'm {}".format(friend, self.name))

me = Person("Nelson")
me.greet("Paula")





