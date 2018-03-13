from turtle import *


def trg(size, fill, color):
    for i in range(3):
        forward(90)
        left(120)
        
def sqr(size, fill, color):
    for i in range(4):
        forward(90)
        left(90)
    
def pegn(size, fill, color):
    for i in range(5):
        forward(90)
        left(72)
        
def hexgn(size, fill, color):
    for i in range(6):
        forward(90)
        left(60)
        
def octgn(size, fill, color):
    for i in range(8):
        forward(80)
        left(45)
        
def star(size, fill, color):
    for i in range(5):
        forward(90)
        right(144)
        
def crl(size, fill, color):
    circle(90)
    
    
if __name__ == "__main__":
    print("shapes.py is being run directly")
else:
    print("shapes.py is being imported into another module")