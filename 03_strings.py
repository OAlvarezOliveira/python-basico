# Strings Y formateo

name , surname , age = "Oscar" , "Alvarez" , 39

print("Mi nombre es {} {} y mi edad es {}".format(name,surname,age))
print("Mi nombre es %s %s y mi edad es %d" %(name,surname,age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

#Desempaquetado de caracteres
language = "python"
a, b, c, d, e, f = language
print(a)
print(f)

#División
language_slice = language [1:3]
print(language_slice)

language_slice = language [1:]
print(language_slice)

language_slice = language [-2]
print(language_slice)

reversed_language = language [::-1]
print(reversed_language)

language_slice = language [0:6:2]
print(language_slice)

# Funciones 
print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.upper().isupper())
print(language.startswith("Py"))




