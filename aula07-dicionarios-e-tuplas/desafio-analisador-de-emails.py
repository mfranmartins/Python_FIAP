#joao.silva@fiap.com.br, maria.souza@fiap.com.br, ana.paula@fiap.com.br
emails = entrada.split(",")

#Separar cada email em nome de usuário e domínio
dominios = {}
usuarios = ()
for email in emails:
    username, dominio = email.strip().split("@")
    if dominio not in dominios:
        dominios[dominio] = 1
    else:
        dominios[dominio] += 1
    usuarios += (username,)
print("Quantidade de e-mails por domínio:", dominios)
print("Lista de usuários:", usuarios)
usuarios = (usuarios[-1],) + usuarios[1:-1] + (usuarios[0],)
print("Após troca de posições:", usuarios)

'''Receber lista de emails digitada pelo usuário
entrada = input("Digite a lista de e-mails:")
emails = entrada.split(",")
print(emails)

#Separar cada email em nome de usuário e domínio
dominios = {}
usuarios = ()
for email in emails:
    username, dominio = email.strip().split("@")
    if dominio not in dominios:
        dominios[dominio] = 1
    else:
        dominios[dominio] += 1
    usuarios += (username,)
print("Quantidade de e-mails por domínio:", dominios)
print("Lista de usuários:", usuarios)
a = usuarios[0]
b = usuarios[-1]
a, b = b, a
print("Após troca de posições:", a, *usuarios[1:-1], b)'''
