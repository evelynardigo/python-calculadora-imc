#Cálculo de IMC
print('-=-' * 25)
peso = float(input('Qual é o seu peso em kg? '))
altura = float(input('Qual é a sua altura? '))
print('-=-' * 25)
imc = peso / (altura ** 2)
print('O valor do IMC é {:.2f} \nA situação da pessoa é:'.format(imc))
if imc < 18.5:
    print('\033[38;5;208mABAIXO DO PESO IDEAL\033[m')
elif imc >= 18.5 and imc <= 25:
    print('\033[1;32mPESO IDEAL\033[m')
elif imc > 25 and imc <= 30:
    print('\033[38;5;208mSOBREPESO\033[m')
elif imc > 30 and imc <= 40:
    print('\033[1;31mOBESIDADE\033[m')
elif imc > 40:
    print('\033[7mOBESIDADE MÓRBIDA\033[m')