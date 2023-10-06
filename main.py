# Criar um array bidimensional com dados diferentes dos utilizados em sala;
# abrindo base de dados
import numpy as np

arquivo = np.genfromtxt("arquivo.txt", delimiter=";", dtype="float64")
print('Aqui um array bidimensional:\n ', arquivo)
print('')

# Obter dados estatísticos (uma com axis=1, a outra com axis = 0 e a última sem axis);
# Calculando a média de cada linha
media_eixo1 = np.mean(arquivo, axis=1)
print("Média de cada linha:")
print(media_eixo1)

# Calculando a soma de cada coluna
soma_eixo0 = np.sum(arquivo, axis=0)
print("Soma de cada coluna:")
print(soma_eixo0)

# Calculando a variância de todo o array
variancia = np.var(arquivo)
print("Variância do array completo:")
print(variancia)
print('')

# Obter a transposta da matriz e realizar uma operação com ela
transposta = np.transpose(arquivo)
print("Transposta da matriz:")
print(transposta)

soma_linhas = np.sum(transposta, axis=1)
print("\nSoma de cada linha da matriz transposta:")
print(soma_linhas)
print('')

# Realizar um produto escalar entre duas matrizes ou de um array com uma matriz;
matriz1 = np.array([[1, 2], [3, 4]])
matriz2 = np.array([[5, 6], [7, 8]])

produto_escalar_matrizes = np.dot(matriz1, matriz2)
print("Produto escalar entre duas matrizes:")
print(produto_escalar_matrizes)
print('')

# Criar um filtro para a sua matriz;
# arquivo = np.genfromtxt("arquivo.txt", delimiter=";", dtype="float64")
filtro = arquivo > 4
dados_filtrados = arquivo[filtro]

print("Matriz após a aplicação do filtro:")
print(dados_filtrados)
print('')

# Realizar alguma operação aritmética (número com matriz, array com matriz, etc.)
# Definindo um número e um array
numero = 5
array = np.array([5, 9])

resultado1 = numero + arquivo
print("Resultado da adição de um número à matriz:")
print(resultado1)

resultado2 = np.dot(array, arquivo)
print("Resultado da multiplicação de um array pela matriz:")
print(resultado2)