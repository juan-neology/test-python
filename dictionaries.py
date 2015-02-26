__author__ = 'juan'

my_string = 'The Red Hat'
print(my_string[1:4])
print(my_string[1:])

for i in my_string:
    print(i)

my_list = my_string.split()
print(my_string)
print(my_list)
print("-------")
print(my_string.join(my_list))

my_new_string = ' -  TheRedHat  '
print(my_new_string.strip())
print("-"+my_new_string)
print("+++++++++++++++++++")
my_dict = {'ship': 'RX44', 'car': 'Fiesta', 'plane': '747'}
print(my_dict.keys())
print(my_dict.values())
print(len(my_dict))
my_dict['train'] = 'BG108'
print(my_dict)
print(my_dict['car'])
my_dict['car'] = 'Escort'
print(my_dict['car'])


for k,v in my_dict.items():
    print(k + ":" + v)


