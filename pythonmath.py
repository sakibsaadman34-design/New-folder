L = [1, 2, 4, 7, 6, 12, 10, 9, 3]

print("Original amount of the list is: ",L)

sum = 0

for i in L:
    sum += i

avg = sum/len(L)

print("The total of the numbers in list is:", sum)
print("The average of the numbers in list is: ",avg)

L.sort()

print("The smallest number in the list is:", L[0])
print("The greatest number in the list is:", L[-1])