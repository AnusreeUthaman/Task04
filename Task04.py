#Task04

#1) Write a Python program that prints a rectangular pattern of asterisks (*).
#The program should ask the user to input the number of rows and columns.

x=int(input("Number of rows:"))
y=int(input("Number of coloumns:"))
for i in range(3):
        print("*****",end="")
        print()
  
#2)Write a Python program to find the sum of all even numbers between 1 and 100 using a while loop.
i=0
c=0
while i<=100:
    c+=i
    i+=2
print("sum of all even numbers between 1 to 100:",c)



#3)Create a list of the first 10 multiples of a given number using a for loop.
num=int(input("Enter a number:"))
multi=[]
for i in range(1,11):
    multi.append(num*i)
print("first multiples of a given number",multi)


#4)Write a Python program to find the maximum number in a list without using the built-in max() function.
x=[5,4,2,6,3,7,1]
max=x[0]
c=[]
for i in range(1,len(x)):
    if x[i]>max:
        max=x[i]
c.append(max)
print(c)


#5)Generate a Fibonacci sequence of a given length using for loop.
n=7
a,b=0,1
print(a)
print(b)
for i in range(n):
    c=a+b
    print(c)
    a,b=b,c


#6)Write a Python program to calculate the factorial of a number using a for loop.
num=int(input("Enter a number:"))
factorial(n)
f=1
for i in range(1,n+1):
        f*=i
print(f)


#7)Write a Python program to reverse a list without using the built-in reverse() method or slicing.
x=[5,3,1,2,4]
n=len(x)
i=-1
d=[]
while(i<0):
    if(i<-(n)):
       break
    d.append(x[i])
    i-=1
print(d)


      
#8)Write a Python program to print all prime numbers between 1 and 50.
for num in range (2,51):
    is_prime=True
    for i in range (2,num):
        if num %i==0:
            is_prime=False
            break
    if is_prime:
        print(num)

       

#9)Write a Python program to find the intersection of two lists.
x=[4,5,3,2,1,6,2]
y=[9,8,7,4,6,8]
intersection=[]
for i in x:
    if i in y:
        intersection.append(i)
print("intersection of two lists:",intersection)


#10)Write a Python program to calculate the sum of squares of numbers in a given list.
x=[1,2,3,4,5]
sum_of_squares=0
for i in x:
    sum_of_squares+=i**2
    print("The sum of squares of numbers:",sum_of_squares)


#11)Perform various list operations like appending, inserting, removing, and sorting.
x=[23,34,55,32,51]
x.append(33)
print(x)

x=[23,34,55,32,51]
x.insert(2,46)
print(x)

x=[23,34,55,32,51]
x.remove(55)
print(x)

x=[23,34,55,32,51]
x.sort()
print(x)
    

#12) Write a Python program that prints a pattern of asterisks (*).
row=5
for i in range(row):
    for j in range(row-i):
        print("*",end="")
    print() 

#13)Write a Python program that determines if a student passes or fails based on their score.
score=int(input("Enter the score:"))
if (score>80):
    print("A Grade")
elif(score>60):
    print("B Grade")
elif(score>50):
    print("C Grade")
elif(score>40):
    print("D Grade")
else:
    print("Failed")
        


#14)Write a Python program to classify a person based on their age.
age=int(input("Enter your age:"))
if(age<13):
    print("Child")
elif(age<20):
    print("Teenager")
elif(age<60):
    print("Adult")
else:
    print("Senior Citizen")



#15)Write a Python program that prints numbers from 1 to 20 but skips multiples of 3.
for i in range(1,21):
    if i%3==0:
        continue
    print(i)









