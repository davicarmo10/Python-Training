lista = []

while True:
    try:
        op = int(input('[1]inserir [2]apagar [3]listar [4]sair '))
    except:
        print('apenas numeros')
        continue
    if op==1:
        lista.append(input('digite '))
        continue
    if op==2:
        print(next(enumerate(lista)))
        apagar=int(input('qual item deseja apagar? apenas números '))
        lista.pop(apagar)
        continue
    if op==3:
        try:
            print(next(enumerate(lista)))
            continue
        except:
            print('lista vazia')
            continue
    if op==4:
        break
   