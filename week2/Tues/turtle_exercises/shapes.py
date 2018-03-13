from turtle import *


def trg():
    for i in range(3):
        forward(90)
        left(120)
        
def sqr():
    for i in range(4):
        forward(90)
        left(90)
    
def pegn():
    for i in range(5):
        forward(90)
        left(72)
        
def hexgn():
    for i in range(6):
        forward(90)
        left(60)
        
def octgn():
    for i in range(8):
        forward(80)
        left(45)
        
def star():
    for i in range(5):
        forward(90)
        right(144)
        
def crl():
    circle(90)
    
    
if __name__ == "__main__":
    print("shapes.py is being run directly")
else:
    print("shapes.py is being imported into another module")