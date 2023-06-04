#This python code displays the total number of positive and negative integers

list_1  = [1,-4,5,2,-7,8,10,-57]

positives = 0
negatives = 0

#Building a for loop to iterate through list items
for i in range(len(list_1)):
    if list_1[i] >= 0:
        positives += 1
    else:
        negatives += 1


print('Number of positive integers:', positives)
print('Number of negative integers:', negatives) 
    