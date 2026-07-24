# Python program to find the largest number in a list 

list = [10,20,35,98,76,90]
largest = list[0]

for i in list:
  if i > largest:
    largest = i
print("the largest num is ",largest)

   