n1 = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é: {} '.format(n1.upper))
print('Seu nome em minúsculas é: {} '.format(n1.lower))
print('Seu nome tem {} letras ao todo' .format(len(n1) - n1.count(' ')))
#print('Seu primeiro nome tem {} letras' .format(n1.find(' ')))
separa = nome.split()
print('seu primeiro nome é {} e ele tem {} letras' .format(separa[0], len(separa[0])))
