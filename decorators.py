def ask_name(func):
    def wrapper(*args):
        print('Hi what is your name')
        func(*args)
    return wrapper


@ask_name
def person_one(name):
    print('Hi my name is ' + name)


person_one('Jack')


@ask_name
def person_second(name):
    print('Hi my name is ' + name)


person_second('Sofia')


@ask_name
def breakfast(food, drink):
    print(f'my name Jame I like {food} and {drink}')


breakfast('chips', 'Kola')