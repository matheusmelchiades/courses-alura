from sklearn.svm import LinearSVC

# features (1 sim, 0 nao)
# pelo long?
# perna curta?
# faz auau?

porco1 = [0, 1, 0]
porco2 = [0, 1, 1]
porco3 = [1, 1, 0]

cachorro1 = [0, 1, 1]
cachorro2 = [1, 0, 1]
cachorro3 = [1, 1, 1]

dados = [porco1, porco2, porco3, cachorro1, cachorro2, cachorro3]

# 1 ==> porco, 0 ==> cachorro
classes = [1, 1, 1, 0, 0, 0]

modelo = LinearSVC()

modelo.fit(dados, classes)

animal_misterioso = [1, 1, 1]

modelo.predict([animal_misterioso])

print(modelo.predict([animal_misterioso]))
