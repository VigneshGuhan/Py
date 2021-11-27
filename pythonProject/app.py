#https://www.youtube.com/watch?v=kqtD5dpn9C8
print('Hello World')

#Variable
age=20
print(age)

price=19.95
print(price)

first_name='Vignesh'
print('first_name'+first_name)

is_online=False
print(is_online)

#To get value from window
#name=input("What is your name? ")
#print("Welcome "+name)

#Type conversion:
#birth_year=input("What is your DOY? ")
#age=2021-int(birth_year)
#print('Age : '+str(age))

#int(),float(),bool(),str();

i=1
while i<=10:
    print(i)
    i=i+1


#combining char with number
j=1
while j<10:
    print(j*'*')
    j=j+1


#Collection
#List
name=["john","b","c","d"]
print(name)
print(name[0])
print(name[-2])
print(name[0:2])
name.append("1")
name.insert(1,"2")
name.remove("b")
print(name)
print("b" in name)
print(len(name))

#for loop
numbers=[1,2,3,4,5]
for item in numbers:
    print(item*'@')

print(range(5))
print((range(5,10)))
print((range(5,10,2)))

for i in range(0,10,3):
    print(i)


#tupples: inmutable - cant be changed;
numbers=(1,2,3)
#numbers[0]=1 > Error as its tupples






