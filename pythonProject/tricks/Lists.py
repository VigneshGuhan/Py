


#Typecasting of all items in a list
list1= list(map(int, ['1', '2', '3']))
print(list1)
list2= list(map(float, ['1', 2, '3.0', 4.0, '5', 6]))
print(list2)

#Sum of digits of an integer
sum_of_digits = lambda x: sum(map(int, str(x)))
print(sum_of_digits(1789))#1+7+8+9=25

#Flat a list that contains sublists
l = [[1, 2, 3], [4, 5], [6], [7, 8], [9]]
print(l)
#one way:
flattened_list = []
for sublist in l:
    for item in sublist:
        flattened_list.append(item)
print(flattened_list)
#other way
flattened_list1 = [item for sublist in l for item in sublist]
print(flattened_list1)



#Transpose of a Matrix
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transpose_A = [list(i) for i in zip(*A)]
print(transpose_A)


# import numpy as np
# A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(np.matrix(A))
# transpose_A = [list(i) for i in zip(*A)]
# print()
# print(np.matrix(transpose_A))


# Swap keys and values in a dictionary
staff = {'Data Scientist': 'John', 'Django Developer': 'Jane'}
staff = {i:j for j, i in staff.items()}
print(staff)