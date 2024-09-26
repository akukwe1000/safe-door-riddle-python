successfull = False
for number in range(3):
    print("atemted!", number + 1, (number + 1) * '*')
    if successfull:
        print('success!!')
        break
else:
    print('you attempted 3 times!!!')