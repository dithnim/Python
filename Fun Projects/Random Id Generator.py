import random as r
wordlist = list()


while True:
    wordlist.clear()
    code = input('Press 1-continue | 2-exit: ')
    try:
        code = int(code)
    except:
        print('Enter 1 or 2 to continue or exit..')
        continue

    if code == 1:
        while True:
            word = input("Enter first 4 letters: ")
            word = word.upper()
            if len(word) == 4:
                for i in range(10):
                # Godak code ona ^ nm methana 10 wenuwata ona gana dano
                    digit = r.randint(1000,9999)
                    if digit not in wordlist:
                        wordlist.append(word+str(digit))

                for i in range(len(wordlist)):
                    print(wordlist[i])
                break
            else:
                print('Please enter 4 letters to continue...!')
                continue


    if code == 2:
        print('Exiting....')
        break
