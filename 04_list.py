# Listas

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 24, 61, 52, 20, 20, 17]

print(my_list)
print(len(my_list))
print(type(my_list)) 
 

my_other_list = [39, 1.72  , "Oscar", "Alvarez" ]

print(my_other_list)

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])

print(my_other_list.count("Oscar"))
print(my_list.count(20))

age, heigth , name , surname = my_other_list

print(age)

print(my_list + my_other_list)

my_other_list.append ("DevOps")
print(my_other_list)

my_other_list.insert(1, "Naranja")
print(my_other_list)

my_other_list.remove("Naranja")
print(my_other_list)

my_list.remove(20)
print(my_list)

print(my_list.pop())
print(my_list)

print(my_list.pop(2))
print(my_list)

del my_list[2]
my_new_list = my_list.copy()
my_list.clear()
print(my_list)
print(my_new_list)
my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

print(my_new_list[1:2])
print(my_new_list[1:3])










