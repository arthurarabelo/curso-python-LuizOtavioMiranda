produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
import copy

novos_produtos = copy.deepcopy(produtos)
for produto in novos_produtos:
    produto['preco'] *= 1.1
    produto['preco'] = round(produto['preco'], 2)

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
produtos_ordenados_por_nome = copy.deepcopy(novos_produtos)

def sortByName(product):
    return product['nome']

produtos_ordenados_por_nome.sort(key=sortByName, reverse=True)
for product in produtos_ordenados_por_nome:
    print(product)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
produtos_ordenados_por_preco = copy.deepcopy(novos_produtos)

def sortByPrice(product):
    return product['preco']

produtos_ordenados_por_preco.sort(key=sortByPrice)
for product in produtos_ordenados_por_preco:
    print(product)