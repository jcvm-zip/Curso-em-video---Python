a = input("digite algo: ")
print("o tipo primitivo de {} é: ".format(a), type(a))
print("o valor: {}, tem espaços?".format(a), a.isspace())
print("O valor: {}, tem somente numeros? ".format(a), a.isnumeric())
print("O valor: {}, é alfabetico?".format(a), a.isalpha())
print("O valor: {}, é alphanumerico? ".format(a), a.isalnum())
print("O valor: {}, está em maiusculas? ".format(a), a.isupper())
print("O valor: {}, está em minusculas?".format(a), a.islower())
print("O valor: {}, está capitalizada?".format(a), a.istitle())
