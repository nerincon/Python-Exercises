# SUM THE NUMBERS
numbers = [1,2,3,4,5]
added = sum(numbers)
print(added)

# LARGEST NUMBER
numbers2 = [2,4,6,8,10]
largest = max(numbers2)
print(largest)

# SMALLEST NUMBER
numbers3 = [2,4,6,8,10]
smallest = min(numbers3)
print(smallest)

# EVEN NUMBERS
numbers4 = [1,2,3,4,5,6,7,8,9]
for num in numbers4:
    if num % 2 == 0:
        print(num)
        
# POSITIVE NUMBERS
numbers5 = [-7,-5,-2,1,4,7,9,12]
for num in numbers5:
    if num > 0:
        print(num)
        
# POSITIVE NUMBERS II
numbers5 = [-7,-5,-2,1,4,7,9,12]
numbers5_upd = []
for num in numbers5:
    if num > 0:
        numbers5_upd.append(num)
print(numbers5_upd)

# MULTIPLY A LIST
numbers6 = [1,2,3,4,5]
factor = 2
new_nums = []
for num in numbers6:
    if num > 0:
        new_nums.append(num * factor)
print(new_nums)

# MULTIPLY VECTORS --> with list compr - faster
list1 = [2,4,5]
list2 = [2,3,6]
new_list = [i[0] * i[1] for i in zip(list1, list2)]
print(new_list)

# MATRIX ADDITION
x = [[1,3],[2,4]]
y = [[5,2],[1,0]]
result = [[0,0],
         [0,0]]
# iterate through rows
for i in range(len(x)):
      # iterate through columns
  for k in range(len(x[0])):
      result[i][k] = x[i][k] + y[i][k]
for r in result:
     print(r)

# MATRIX ADDITION II
x = [[1,3],[2,4],[4,8]]
y = [[5,2],[1,0],[5,2]]
result = [[0,0],
         [0,0],
         [0,0]]
# iterate through rows
for i in range(len(x)):
      # iterate through columns
  for k in range(len(x[0])):
      result[i][k] = x[i][k] + y[i][k]
for r in result:
     print(r)
     
# DE-DUP
mylist = [2,6,9,5,"Hello", 1, "Goodbye","Hello",2,5]
set_result = list(set(mylist))
back_to_list_result = list(set(mylist))
print(set_result)
print(back_to_list_result)

