nome = 'Gustavo';
print(nome)
idade = 18;

print(f"O nome é {nome} e sua idade é {idade}")# f é usado para poder adicionar coisas dessa forma

#Função sem parametro
def saudacao():
    nomeS = input("Qual seu nome?");
    idadeS = input("Qual sua idade?")
    print(f"seu nome é {nomeS} e sua idade é {idadeS}")
#saudacao()

#Função com parametro
nomeF = input("Qual seu nome? ");
idadeF = input("Qual sua idade? ")
def saudacao_com_parametro(nomeF,idadeF):
    print(f'Seu nome é {nomeF} e sua idade é {idadeF}')
#saudacao_com_parametro(nomeF,idadeF)

#Condicionais
def verifica_se_pode_dirigir(idade):
    if idade>=18:
      print('Você pode dirigir');
    else:
     print('Você não pode dirigir');
verifica_se_pode_dirigir(int(idadeF)) #convertendo idade em inteiro para poder fazer a verificação