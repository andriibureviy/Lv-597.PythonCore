num1 = int(input("Enter ur num for Fibonacci: "))
while num1 <= 0:  # check if the number is valid
   print("Please enter a positive integer")
   num1 = int(input("Enter ur num for Fibonacci: "))

num1 += 1
list1 = [0, 1]
i = 0

while i < num1:
    num2 = list1[i] + list1[i + 1]
    list1.append(num2)
    i += 1

#list1 = list1[:len(list1)-1] #remove last n elements from list

while list1[-1] > num1:
    list1 = list1[:len(list1) - 1]
else:
    list1 = list1[:len(list1) + 1]

for b in range(num1):
    print(list1[b], end= ",")
