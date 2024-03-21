import requests
import pandas as pd
def get_fakestore_data():
    url = "https://fakestoreapi.com/products"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print("Erro ao obter os dados:", response.status_code)
            return None
    except Exception as e:
        print("Ocorreu um erro na requisição:", e)
        return None
def review_ranking(products):
    #Ordena os produtos pela contagem de avaliações em ordem decrescente
    sorted_products = sorted(products, key=lambda x: x["rating"]["count"], reverse=True)

    print("Todos os produtos com maior até a menor números de avaliações:")
    for i, product in enumerate(sorted_products, start=1):
        print(f"{i}.{product['title']}")
        print(f"   Avaliações: {product['rating']['count']}")
        print(f"   Classificação: {product['rating']['rate']}")
        print()

def products_categories(products):
    #Conjunto vazio para armazerar as categorias
    categories = set()

    #Adiciona as categorias no conjunto
    for product in products:
        categories.add(product["category"])
    #Exibe as categoria
    print("Tipos de categorias dos produtos:")
    for category in categories:
        print(f"- {category}")
    print()

def display_top_rated_product(products):
    #Inicializa variáveis para armazenar o produto com a melhor classificação e sua taxa
    top_rated_product = None
    max_rating = float('-inf')

    #Percorre a lista de produtos para encontrar o produto com a melhor classificação
    for product in products:
        if product["rating"]["rate"] > max_rating:
            max_rating = product["rating"]["rate"]
            top_rated_product = product
    #Exibe as informações do produto
    print("Produto com a melhor classificação:")
    print("Título:", top_rated_product["title"])
    print(f"Preço: ${top_rated_product["price"]}")
    print("Descrição:", top_rated_product["description"])
    print("Categoria:", top_rated_product["category"])
    print("Classificação:", top_rated_product["rating"]["rate"])
    print("Número de avaliações:", top_rated_product["rating"]["count"])
    print("Imagem:", top_rated_product["image"])
def main():
    products = get_fakestore_data()
    if products:
        review_ranking(products)
        products_categories(products)
        display_top_rated_product(products)

if __name__ == "__main__":
    main()