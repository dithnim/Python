# This code will add the input data into a list

list_1 = list()
# Building a while loop
i = 1
while i <= 5:
    marks = int(input(f'Enter the marks {i}:'))
    list_1.append(marks)
    i += 1

print(list_1)
