string_entrada = input("Digite uma string: ")
string_invertida = ""

for caractere in string_entrada[::-1]:
    string_invertida += caractere

print(string_invertida)