# 1-10
for v in range(1,11):
    print(v)
    
    
# n to m
n = int(input("Start from: " ))
m = int(input("End on: "))

for v in range(n,m+1):
    print(v)
    
    
# Odd Numbers
for v in range(1,11):
    if v % 2 != 0:
        print(v)
        

# Print a Square
for v in range(1,6):
    print("*" * 5)
    
    
# Print a Square 2
n = int(input("How big is the square? "))
for v in range(1,n+1):
    print("*" * n)
    

# Print a Box
w = int(input("Width? "))
h = int(input("Height? "))
print('*' * w)
for i in range(h-2):
    print ('*' + ' ' * (w-2) + '*')
print('*' * w)

# Print a Triangle and Print Triangle II
def triangle(h, t=0):
    if h == 0:
        return 0
    else:
        print (' ' * h + '*' * (t * 2 + 1))
        return triangle(h - 1, t + 1 )

triangle(7)


# Print a Banner
text = input("Text? ")
w = len(text)
h = 3
print('*' * (w + 4))
for i in range(h-2):
    print ('*' + " " + text + " " + '*')
print('*' * (w + 4))







