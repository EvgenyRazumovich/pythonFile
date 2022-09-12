number = input('Enter some number: ')
try:
    print(int(number) / 2)
except:
    print('You have to enter a number!')
else:
    print('You entered correctly')
finally:
    print('You entered correctly value ')
