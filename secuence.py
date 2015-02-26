__author__ = 'juan'
#mutable
my_list = ["ship", "boat", "plain"]

print(my_list)
my_list.append("car")
print(my_list)
my_list.pop()
print(my_list)
my_list.insert(1, "car2")
print(my_list)
print(my_list[1:3])
if "ship" in my_list:
    print("True")
my_list.reverse()
print(my_list)
#inmutable tuples
my_tuple = ("car", "boat", "ship")
my_new_tuple = ("plane", "jetski")
my_really_new_tuple = my_tuple + my_new_tuple
print(my_really_new_tuple)

#ranges: list of numbers
my_range = list(range(0,22,2))
print(my_range)

