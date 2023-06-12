import random as r

dict1 = {1:'Rock', 2:'Paper', 3:'Scissors'}

while True:
    code = r.randint(1,3)
    guess = int(input('Enter Your Move || 1-Rock || 2-Paper || 3-Scissors: '))

    if code == guess:
        print('Draw')

    if code == 1 and guess ==2 or\
          code == 1 and guess == 3 or\
              code == 3 and guess ==2:
        print('Wrong. Computer Chose',dict1[code])

    if code == 2 and guess==1 or\
          code == 2 and guess == 3 or\
            code == 3 and guess ==1:
        print('You Won....! Computer chose',dict1[code])
        break
    