nome = input(' Qual seu nome ?')
c = input(' Olá {}, prazer em conhecer você, Como você está ?'.format(nome)).upper()
if c == 'BEM' and 'BOM':
    print('Que bom')
else:
    print('Que pena, espero que as coisas melhorem para você')
a = input(' Você gosta de tropeiro ?').upper()

if a == 'SIM':
    b = input('Eu também, gosto muito do tropeiro do mercado central e você ?')
    if b == 'Sim' and 'Também':
        print('Que legal')
else:
    d = input('Que pena, ia te convidar para gente almoçar lá, \nTenho que ir, ate a proxima')
