import pickle
#
#
# honda = (
#     'model',
#     'grey',
#     '2019',
#     (
#         (1, 'James Brown'),
#         (2, 'Jane lite'),
#         (3, 'Jake Green')
#     )
#
# )
#
#
# with open('honda.pickle', 'wb') as honda_file:
#     pickle.dump(honda, honda_file)


with open('honda.pickle', 'rb') as honda_f:
    honda_a = pickle.load(honda_f)

print(honda_a)

model, color, year, owner_list = honda_a

print(model)    
print(color)
print(year)
print(owner_list)


for i in owner_list:
    a, b = i
    print(a,b)
