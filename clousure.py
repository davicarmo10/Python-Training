def criar_saudacao():
    def printar(saudacao, nome):
        return f'{saudacao}, {nome}!'
    return printar
s1 = criar_saudacao()
print(s1('oi', 'davi'))