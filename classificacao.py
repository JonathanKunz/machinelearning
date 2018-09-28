from sklearn.naive_bayes import MultinomialNB


goodClient = [0, 1, 1]
goodClient = [0, 0, 1]
goodClient = [0, 1, 1]
badClient = [1, 0, 0]
badClient = [1, 1, 0]
badClient = [1, 0, 0]

dados = [goodClient, goodClient, goodClient, badClient, badClient, badClient]

marcacoes = [1, 1, 1, -1, -1, -1]   

modelo = MultinomialNB() 
modelo.fit(dados, marcacoes) 


misterioso1 = [0, 1, 1]   
misterioso2 = [0, 1, 1]    
misterioso3 = [1, 1, 0]   

lista = [misterioso1, misterioso2, misterioso3]

marcacoes_teste = [1, 1, -1]

resultado = modelo.predict(lista)

diferencas = resultado - marcacoes_teste

acertos = [d for d in diferencas if d == 0]

total_de_acertos = len(acertos)
total_de_elementos = len(lista)

taxa_de_acerto = 100.0 * total_de_acertos / total_de_elementos

print(resultado)
print(diferencas)
print(taxa_de_acerto)
