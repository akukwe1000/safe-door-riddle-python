


print('\n                                          Safe Door riddle')

riddle_one = '''
                You are trapped in a room with three doors, the first door contains fire , the second door is filled with
                naked electricity, and the third door is filled with poisonous gas which of the door will you choose to
                follow if door containing fire type 'FIRST', if door containing electricity type 'SECOND' and if door 
                containing gas type 'THIRD' anything order thand this response would display an error please note
            '''
print(riddle_one)
answer_one = (input('Enter answer:'))



# First case 
if answer_one.lower() == 'first':
    riddle_fire = '''
                    In this room you see a foam to cover your body and a fire extinguisher to put off the fire which 
                    would you use type 'FOAM' to choose foam and 'EXTINGUISHER' to choose the fire extinguisher
                '''
    print(riddle_fire)
    answer_fire = input('Enter answe:')
    if answer_fire.lower() == 'extinguisher':
        riddle_even_number = '''
                                You are able to put off the fire and you are faced with the last door if the code 
                                needed to open this door is an even number what would you write 
                            '''
        print(riddle_even_number)
        answer_even_number = int(input('Enter an even number to unlock the door:'))
        if answer_even_number % 2 == 0:
            print('\nYou escpaped.....You won!!!!')
        else:
            print(f"\nYou loose '{answer_even_number}' is not an even number")
    else:
        print('You loose foam do not prevent fire instead aids it so you burn.....')



# Second case
elif answer_one.lower() == 'second':
    riddle_electric = '''
                    In this room you see an iron sheet to cover your self and a switch to off the electricity which 
                    would you pick type 'IRON' to choose iron sheet and 'SWITCH' to choose the switch
                '''
    print(riddle_electric)
    answer_electric = input('Enter answe:')
    if answer_electric.lower() == 'switch':
        riddle_odd_number = '''
                                You are able to put off the electricity and you are faced with the last door if the code 
                                needed to open this door is an odd number what would you write 
                            '''
        print(riddle_odd_number)
        answer_odd_number = int(input('Enter a odd number to unlock the door:'))
        if answer_odd_number % 2 != 0:
            print('\nYou escpaped.....You won!!!!')
        else:
            print(f"\nYou loose '{answer_odd_number}' is not an odd number")
    else:
        print('You loose metal is a good condutor of electricity hence you get electricuted.....')



# third case
elif answer_one.lower() == 'third':
    riddle_gas = '''
                    In this room you see a strong helmet and a gas nose mask  which would you choose  
                     'HELMET' to choose the strong helmet and 'MASK' to choose the face mask
                '''
    print(riddle_gas)
    answer_gas = input('Enter answe:')
    if answer_gas.lower() == 'mask':
        riddle_prime_number = '''
                                You are able to get to the last door which is  the last door if the code 
                                needed to open this door is a multiple of 5 what would you write 
                            '''
        print(riddle_prime_number)
        answer_prime_number = int(input('Enter any multiple of 5 to unlock the door:'))
        if answer_prime_number % 5 == 0:
            print('\nYou escpaped.....You won!!!!')
        else:
            print(f"\nYou loose '{answer_prime_number}' is not a multiple of five")
    else:
        print('You loose helmet only protect the head from injury so u end up taking in the poisonous gas.....')

        
    
# my else block 
else:
    print('You typed the wrong respons please start the game again.....')