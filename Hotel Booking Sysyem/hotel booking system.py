room_no = ['1','2','3','4','5']
names = ['','','','','']
members = [0,0,0,0,0]

while True:
    code  = int(input('Press 1=check in | 2=check out | 3=display | 9=exit: '))

    #!Check-in Section
    if code == 1:

        while True:
            available_rooms = 0
            for i in range(5):
                if members[i] == 0:
                    available_rooms += 1

            if available_rooms == 0:
                print('All rooms are booked',end='\n\n')
                break
            else:
                print('Available rooms')
                for i in range(5):
                    if members[i] == 0:
                        print(room_no[i],end=' ')
                print()
                checkin_no = int(input('Select a room number: '))
                print()

                if checkin_no <= 0 or checkin_no >= 6:
                    print('Invalid room number. Try again',end='\n\n')
                    continue
                elif members[checkin_no-1] > 0:
                    print('This room is already booked',end='\n\n')
                    continue
                else:
                    name = input('Enter the name: ')
                    while True:
                        no_members = int(input('Enter the number of members: '))
                        if no_members > 4:
                            print('\nMaximum number is 4',end='\n\n')
                            continue
                        if no_members == 0:
                            print('\nMinimum number is 1',end='\n\n')
                            continue
                        if no_members > 0 and no_members < 5:
                            names[checkin_no-1] = name
                            members[checkin_no-1] = no_members

                            print()
                            print('Booking successful')
                            print('Room',checkin_no,'is reserved for',name,end='\n\n')
                            break
                    break
                    


    #!Check-out Section
    if code == 2:
        if sum(members) != 0:
            while True:
                print('Booked rooms')
                for i in range(5):
                    if members[i] != 0:
                        print(room_no[i],end=' ')
                print()
                checkout_no = int(input('Enter the room number: '))
                print()


                #? Checking if the room number is correct
                if checkout_no <=0 or checkout_no >=6:
                    print('Invalid room number. Try again',end='\n\n')
                    continue
                
                #? Checking if the room is empty
                elif members[checkout_no-1] == 0:
                    print('This room is empty',end='\n\n')
                    continue

                else:
                    print(names[checkout_no-1],'checked out from room number',checkout_no)
                    print('Room',checkout_no,'is free now',end='\n\n')
                    members[checkout_no-1] = 0
                    break
        else:
            print('All rooms are empty')


    #! Display Section
    if code == 3:
        #? Printing Room Numbers
        print('\nRoom Numbers:',end='\t')
        for i in range(5):
            print(room_no[i],end='\t')

        #?Printing Current status
        print('\nCurrent Status:',end='\t')
        for i in range(5):
            if members[i] == 0:
                print('free',end='\t')
            else:
                print('booked',end='\t')

        #?Printing Member Count
        print('\nMembers:',end='\t')
        for i in range(5):
            print(members[i],end='\t')

        print('\n')

    if code == 9:
        break

