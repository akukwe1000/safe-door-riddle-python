
# # the story assignment week 1   ----------------11111111111111111111111111111111111

# print("\n")  # added a line break here to create a spce between at the top of the program
# instruction = 'Please enter the following words:'

# print(instruction)b 
# # print("\n")  #  a line break to add a space between the intruction and the questions
# adjective = input('\n adjective: ')  # u can also use /n to creat a space before the statement
# animal = input('animal: ')
# verb = input('verb: ')
# exclamation = input('exclamation: ')
# verb_two = input('verb: ')
# verb_three = input('verb: ')

# print("\n")  # a line break 
# story = 'Your story is: '

# # i used a formatted string bellow to display my message 
# message = f'The other day, I was really in trouble. It all started when i saw a very {adjective} {animal} {verb} down the hallway. "{exclamation.capitalize()}!"   I yelled. But all I  could think to do was to {verb_two} over and over. Miraculously, that caused it to stop, but not before it tried to {verb_three} right in front of my family '

# print(story)
# print("\n")   # a line break

# print(message)

# # story assignment ends here 

# # week two assignment mileStone calculator  111111111111111111111111111111111111111

# child_price = float(input("\n What is the price of a child's meal? "))
# adult_price = float(input(" What is the price of an adult's meal? "))
# child_population = int(input(" How many children are there? "))
# adult_population = int(input(" How many adults are there? "))

# subtotal = (child_price *child_population)  + (adult_price * adult_population)
# print(f" \nSubtotal: ${subtotal:.2f}")

# tax_rate  = float(input(" \n What is the sales tax rate ? "))
# sales_tax = (subtotal * tax_rate) / 100
# total = sales_tax + subtotal
# print(f"\nSales Tax: ${sales_tax:.2f}")
# print(f"Total: ${total:.2f}")

# # Am adding a water field that calculate base on the quantity of bottle water you want in elation to a fixed price
# bottle_water = print('\na bottle of water is sold at  $1.2 if interested specify the number of bottles else input zerro thankyou!!  ')
# water_quantity = int(input('How mmany bottle of water do u want? '))
# water_price = 1.2 * water_quantity
# food_water_sumtotal = water_price + total
# print(f"Food and water sumtotal: ${food_water_sumtotal:.2f}")

# payment = float(input("\nWhat is the payment amount? "))
# change = payment - food_water_sumtotal
# print(f"Change: ${change:.2f}")

# # mileStone calculator ends here 

# week 3 assignment 111111111111111111111111111111 11111111111111111111111111111111111111

# my creativity was added first on line 32 where u need to type only an even number to unlock the last door  if u took the fire door
# another one was on line 57 where u need to type only an odd number to unlock the last door if u take the elcetric door
# another one was on line 82 where u need to type only a multiple of 5 to unlock the last door if u take the poisonous gas door


# print('\n                                          Safe Door riddle')

# riddle_one = '''
#                 You are trapped in a room with three doors, the first door contains fire , the second door is filled with
#                 naked electricity, and the third door is filled with poisonous gas which of the door will you choose to
#                 follow if door containing fire type 'FIRST', if door containing electricity type 'SECOND' and if door 
#                 containing gas type 'THIRD' anything order thand this response would display an error please note
#             '''
# print(riddle_one)
# answer_one = (input('Enter answer:'))



# # First case 
# if answer_one.lower() == 'first':
#     riddle_fire = '''
#                     In this room you see a foam to cover your body and a fire extinguisher to put off the fire which 
#                     would you use type 'FOAM' to choose foam and 'EXTINGUISHER' to choose the fire extinguisher
#                 '''
#     print(riddle_fire)
#     answer_fire = input('Enter answe:')
#     if answer_fire.lower() == 'extinguisher':
#         riddle_even_number = '''
#                                 You are able to put off the fire and you are faced with the last door if the code 
#                                 needed to open this door is an even number what would you write 
#                             '''
#         print(riddle_even_number)
#         answer_even_number = int(input('Enter an even number to unlock the door:'))
#         if answer_even_number % 2 == 0:
#             print('\nYou escpaped.....You won!!!!')
#         else:
#             print(f"\nYou loose '{answer_even_number}' is not an even number")
#     else:
#         print('You loose foam do not prevent fire instead aids it so you burn.....')



# # Second case
# elif answer_one.lower() == 'second':
#     riddle_electric = '''
#                     In this room you see an iron sheet to cover your self and a switch to off the electricity which 
#                     would you pick type 'IRON' to choose iron sheet and 'SWITCH' to choose the switch
#                 '''
#     print(riddle_electric)
#     answer_electric = input('Enter answe:')
#     if answer_electric.lower() == 'switch':
#         riddle_odd_number = '''
#                                 You are able to put off the electricity and you are faced with the last door if the code 
#                                 needed to open this door is an odd number what would you write 
#                             '''
#         print(riddle_odd_number)
#         answer_odd_number = int(input('Enter a odd number to unlock the door:'))
#         if answer_odd_number % 2 != 0:
#             print('\nYou escpaped.....You won!!!!')
#         else:
#             print(f"\nYou loose '{answer_odd_number}' is not an odd number")
#     else:
#         print('You loose metal is a good condutor of electricity hence you get electricuted.....')



# # third case
# elif answer_one.lower() == 'third':
#     riddle_gas = '''
#                     In this room you see a strong helmet and a gas nose mask  which would you choose  
#                      'HELMET' to choose the strong helmet and 'MASK' to choose the face mask
#                 '''
#     print(riddle_gas)
#     answer_gas = input('Enter answe:')
#     if answer_gas.lower() == 'mask':
#         riddle_prime_number = '''
#                                 You are able to get to the last door which is  the last door if the code 
#                                 needed to open this door is a multiple of 5 what would you write 
#                             '''
#         print(riddle_prime_number)
#         answer_prime_number = int(input('Enter any multiple of 5 to unlock the door:'))
#         if answer_prime_number % 5 == 0:
#             print('\nYou escpaped.....You won!!!!')
#         else:
#             print(f"\nYou loose '{answer_prime_number}' is not a multiple of five")
#     else:
#         print('You loose helmet only protect the head from injury so u end up taking in the poisonous gas.....')

        
    
# # my else block 
# else:
#     print('You typed the wrong respons please start the game again.....')


# week 4 assignment 1111111111111111111111111111111111111111111111111111111111 

# my first creativity is on line 4 where by after u win the guess instead of the game ending it ask if you want to continue if you type yes with any case be it upper or lower or mix it continues
# my second creativity is on line 6 where i have more than one word this implies that if you continue the game after wining the first guess the next guess might not be the same because the words are selected at random
# import random
# keep_playing = 'yes'
# while keep_playing.lower() == 'yes':
#     words = ['test', 'gold' , 'hope', 'love']
#     secrete_word = random.choice(words)
#     print('\n                                                          welcome to the four letter guessing game')
#     print('try to guess the secrete four leter words')

#     guess_count = 0
#     guess = ''

        


#     while guess != secrete_word :
#         guess = input('what is your guess: _ _ _ _ ')
#         guess_count = guess_count + 1

#         if len(guess) != len(secrete_word):
#             print('error the word is four letters plesase try again')
#             continue
#         hint = ['_'] * 4

#         for i in range(4):
#             if guess[i] == secrete_word[i]:
#                 hint[i] = guess[i].upper()
#             elif guess[i] in secrete_word:
#                 hint[i] = guess[i].lower()
        
#         print('hint:', ''.join(hint))

#         if ''.join(hint).upper() == secrete_word.upper():
#             print(f"you won!!  it took u {guess_count} times to guess the correct word")
#         else:
#             print("sorry you are incorrect  keep guessing")
#     keep_playing = input('Woul you like to play again (yes/no) ')

# print('thank you for playing good bye')

# week  5 assignment 111111111111111111111111111111111111111111111111111111111111111111111

# my creativity i handeled a case when u enter number greater or lesser than 5 in my select action 
# i also handled the part if my action is equal to 5 it says thank you good bye  and the program stops running
# i also handeled the action if a different data type is entered using a try catch block instead of my program breaking it continues untill u enter an integer for the select option

# instruction = '''
# Please select one of the following:
# 1. Add items
# 2. View cart
# 3. Remove item
# 4. Compute total
# 5. Quit
# '''
# print(instruction)

# item_list = []
# price_list = []

# while True:
#     print(instruction)
#     try:
#         action = int(input('Please enter an action: '))
#     except ValueError:
#         print('you did not enter a number')
#         continue

#     if action > 5 or action < 1:
#         print("Your action does not match the above options.")
#     elif action == 1:
#         add_item = input('What item would you like to add? ')
#         add_price = float(input(f'What is the price of the {add_item}? '))
#         item_list.append(add_item)
#         price_list.append(add_price)
#     elif action == 2:
#         print('\nThe shopping list is:')
#         for i in range(len(item_list)):
#             item = item_list[i]
#             price = price_list[i]
#             print(f"{i + 1}. {item} : ${price:.2f}")
#     elif action == 3:
#         print('\nThe shopping list is:')
#         for i in range(len(item_list)):
#             item = item_list[i]
#             price = price_list[i]
#             print(f"{i + 1}. {item} : ${price:.2f}")
#         remove = int(input('What is the number of the item you want to remove? ')) - 1
#         if 0 <= remove < len(item_list):
#             removed_item = item_list.pop(remove)
#             removed_price = price_list.pop(remove)
#             print(f'Removed {removed_item} - ${removed_price:.2f}')
#         else:
#             print("Invalid item number.")
    
#     elif action == 4:
#         total = sum(price_list)
#         print(f'The total is ${total:.2f}')
#     elif action == 5:
#         print('Thank you good bye ')
#         break



# week 7 assignment 111111111111111111111111111111111111111111111111111111111111111111111111111111 

# def windChill(T, V):
#     cal = 35.74 + (0.6215 * T) - 35.75 * (V ** 0.16) + 0.4275 * T * (V ** 0.16)
#     return cal

# def temConvertor(C):
#     # Convert Celsius to Fahrenheit
#     return (C * 9/5) + 32

# quest = int(input('What is the temperature? '))
# unit = input('Fahrenheit or Celsius (F/C)? ').upper()  

# # Iterate through wind speeds from 5 to 60 mph, in steps of 5
# for V in range(5, 61, 5):
#     if unit == 'C':
#         converted = temConvertor(quest)
#         windcal = windChill(converted, V)
#         print(f"At temperature {converted:.1f}F, and wind speed {V} mph, the windchill is: {windcal:.2f}F")
#     elif unit == 'F':
#         windcal = windChill(quest, V)
#         print(f"At temperature {quest:.1f}F, and wind speed {V} mph, the windchill is: {windcal:.2f}F")


    

