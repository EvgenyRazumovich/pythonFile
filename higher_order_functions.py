# def product(n, func):
#     result = 1
#     for number in range(1, n):
#         result *= func(number)
#     return result
#
#
# def square(x):
#     return x * x
#
#
# def cube(x):
#     return x * x * x
#
#
# print(product(3, square))
# print(product(4, cube))
# ***********************************************************************************

# def my_function(a, b, func):
#     result = func([a, b])
#     return result
#
# print(my_function(2, 3, sum))
# **************************************************************************************
# from random import choice
#
#
# def colorize(thing):
#     def get_color():
#         colors = ('red', 'yellow', 'blue')
#         color = choice(colors)
#         return color
#
#     result = get_color() + ' ' + thing
#     return result
#
#
# print(colorize('apple'))
# *******************************************************************
# from random import choice
#
#
# def my_car(car):
#     def color_car():
#         color = ('red', 'blue', 'black', 'yellow')
#         colors = choice(color)
#         return colors
#
#     result = color_car() + ' ' + car
#     return result
#
#
# print(my_car('Mercedes'))
# ********************************************************************************
# from random import choice
#
#
# def random_color():
#     def ra_color():
#         color = ('red', 'blue', 'yellow')
#         colors = choice(color)
#         return colors
#
#     return 'My car' + ' ' + ra_color()
#
#
# first_car = random_color()
# print(first_car)
#
# second_car = random_color()
# print(second_car)
#
# third_car = random_color()
# print(third_car)

