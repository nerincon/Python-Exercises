# Exercise 1:
# file = input("File Name: ")
# with open(file,"r") as f:
#     contents = f.read()
#     print(contents)
    
# # Exercise 2:
# file = input("File Name: ")
# string = input("What do you want to write in the file? " )
# with open(file,"r+") as f:
#     lines = f.readlines()
#     length = len(lines)
#     if length > 0:
#         f.write("\n")
#         f.write(string)
#     else:
#         f.write(string)


# # Exercise 3:
# def count():
#     file = input("File Name: ")
#     with open(file,"r") as f:
#         lines = f.readlines()
#         return {"number of words": sum(len(line.split(" ")) for line in lines),
#                 "number of characters": sum(len(line) for line in lines)}
        
# print(count())

# # Bonus Exercise
# import io
# file = io.StringIO()
# while True:
#     data = file.write("A")
#     data = file.getvalue()
#     print(data)
#     print(len(data))
    
# # At what count did your computer crash? - Will test later
# # What kind of error did you get?
# # Did your program crash earlier or later than expected? Why do you think?

