nome = 'Gustavo';
print(nome)
idade = 18;

#print(f"O nome é {nome} e sua idade é {idade}")# f é usado para poder adicionar coisas dessa forma

#Função sem parametro
def saudacao():
    nomeS = input("Qual seu nome?");
    idadeS = input("Qual sua idade?")
    print(f"seu nome é {nomeS} e sua idade é {idadeS}")
#saudacao()

#Função com parametro
#nomeF = input("Qual seu nome? ");
#idadeF = input("Qual sua idade? ")
def saudacao_com_parametro(nomeF,idadeF):
    print(f'Seu nome é {nomeF} e sua idade é {idadeF}')
#saudacao_com_parametro(nomeF,idadeF)

#Condicionais
def verifica_se_pode_dirigir(idade):
    if idade>=18:
      print(f'Sua idade é {idade} e você pode dirigir');
    else:
     print(f'Sua idade e {idade} e você não pode dirigir');
# verifica_se_pode_dirigir(int(idadeF)) #convertendo idade em inteiro para poder fazer a verificação

#Listas
idades = [18,22,15,50];
print(type(idades))
print(idades[1])
print(idades[0:3])#printa os valores até o ultimo valor -1, nesse caso: [18, 22, 15]
print(idades[1:])#mostra todos os valores após o 2 valor do array
print(idades[-1])#mostra o ultimo valor do array

#Laços e loops
#for idade in idades: # cria um laço do tamanho das idades, e a cada execução passa um novo parametro para idade
    #verifica_se_pode_dirigir(idade)

#Booleano
print(idade >= 18)
print(idade == 15)
permissoes = [];
for idade in idades:
    if(idade >= 18):
        permissoes.append(True);#adiciona valores ao inicio do array
    else:
        permissoes.append(False);

for permissao in permissoes:
    print(permissao)