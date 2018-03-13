## Hello
# def hello(name):
#     print("Hello {}".format(name))

# hello("Nelson")

## Y = X + 1
# import matplotlib
# matplotlib.use("Agg")

# from matplotlib import pyplot

# def f(x):
#     return x + 1
    
# xs = list(range(-3,4))
# ys = []
# for x in xs:
#     ys.append(f(x))

# pyplot.plot(xs, ys)
# pyplot.savefig('myplot1.png')
# pyplot.close() # start a new plot


## Square of x
# import matplotlib
# matplotlib.use("Agg")

# from matplotlib import pyplot

# def f(x):
#     return x ** 2
    
# xs = list(range(-100,100))
# ys = []
# for x in xs:
#     ys.append(f(x))

# pyplot.plot(xs, ys)
# pyplot.savefig('myplot2.png')
# pyplot.close() # start a new plot


# # Odd or Even
# import matplotlib
# matplotlib.use("Agg")

# from matplotlib import pyplot

# def f(x):
#     if x % 2 != 0:
#         return 1
#     else:
#         return -1
    
# xs = list(range(-5,7))
# ys = []
# for x in xs:
#     ys.append(f(x))

# pyplot.bar(xs, ys)
# pyplot.savefig('myplot3.png')
# pyplot.close() # start a new plot

# # Sine
# import matplotlib
# matplotlib.use("Agg")

# from matplotlib import pyplot
# import math

# def f(x):
#     return x
    
# xs = list(range(-5,6))
# ys = []
# for x in xs:
#     ys.append(f(math.sin(x)))

# pyplot.plot(xs, ys)
# pyplot.savefig('myplot4.png')
# pyplot.close() # start a new plot


# # Sine 2
# import matplotlib
# matplotlib.use("Agg")

# from matplotlib import pyplot
# import math
# from numpy import arange

# def f(x):
#     return x
    
# xs = list(arange(-5,6, 0.1))
# ys = []
# for x in xs:
#     ys.append(f(math.sin(x)))

# pyplot.plot(xs, ys)
# pyplot.savefig('myplot5.png')
# pyplot.close() # start a new plot


# # Degree Conversion
# import matplotlib
# matplotlib.use("Agg")

# from matplotlib import pyplot

# def func(x):
#     return temp * 1.8 + 32
    
    
# c = list(range(-40,40))
# f = []
# for x in c:
#     temp = x
#     f.append(func(temp))

# pyplot.plot(c, f)
# pyplot.title('Celcius vs Farenheit')
# pyplot.ylabel('Farenheit')
# pyplot.xlabel('Celcius')
# pyplot.savefig('myplot6.png')
# pyplot.close()


# # Play again?
# def play_again():
#     play = input("Do you want to play again (Y on N)? ").lower()
#     if play == "y":
#         return True
#     else:
#         return False
        
# print(play_again())



# # Play again? Again. ---> Note: Will not see in console because returning instead of printing. 
# # Must Print instead of return if calling function. If print func then, "None" will appear.
# def play_again():
#     play = input("Do you want to play again (Y on N)? ").lower()
#     if play == "y":
#         return True
#     elif play == "n":
#         return False
#     else:
#         print("Invalid Input")
#         play_again()
        
# play_again()
