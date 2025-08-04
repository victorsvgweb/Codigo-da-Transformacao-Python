print("ola, mundo!")
print(type("ola"))
print(type(10))

 # solicita o nome do usuario
 nome = input("digite seu nome: ")

# exibe uma mengasem personalizada
print(f"ola, {nome}! seja bem-vindo(a) ao mundo da programaçao!")

from detetime import detetime

# solicita o nome do usuario
nome = input("digite seu nome: ")

#obtem data e hora atuais
agora = datetime.now()
hora_atual = agora.strftime("%H:%M")

# saudaçao com hora 
print(f"ola, {nome}! Agora sao {hora_atual}. seja bem vindo(a)!")