import random
n: int = random.randint(0, 5)

num = int(input('Qual o numero que o PC pensou? '))

if num == n:
    print('Parabéns! Você acertou')
else:
    print('Você perdeu')




