
# # the story assignment week 1

# print("\n")  # added a line break here to create a spce between at the top of the program
# instruction = 'Please enter the following words:'

# print(instruction)
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

# # week two assignment mileStone calculator 

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