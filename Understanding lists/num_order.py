# This code blok prints out the given numbers in both ascending and descending order.

list_1 = [2, 5, 1, 4, 3, 6, 7, 8, 9, 10, 40, 15]

# sorting the list
list_1.sort()
print('Ascending:', end='\t')

for i in range(len(list_1)):
    print(list_1[i], end=' ')

print()  # Line Break

# reversing the list
list_1.reverse()
print('Descending:', end='\t')
for i in range(len(list_1)):
    print(list_1[i], end=' ')
