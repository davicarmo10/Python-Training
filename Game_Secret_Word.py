wordSystem = 'odio'
checked_word = ''

while True:
    userDigit = input('digite uma letra ')
    
    if len(userDigit) > 2:
        print('digite uma letra só, caralho')

    if userDigit in wordSystem:
        checked_word += userDigit

    for x in wordSystem:
        if checked_word in 
    op = input('continuar? ').lower().startswith('s')
    if op is True:
        continue
    else:
        break