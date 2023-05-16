from models.dish import Dish
from models.ingredient import Ingredient
import pandas as pd


class MenuData:
    def __init__(self, source_path: str) -> None:
        # inicializa o set de pratos
        self.dishes = set()
        # carrega os dados do arquivo csv especificado pelo parâmetro
        # source_path

        self.csv_data = pd.read_csv(source_path)
        # cria um dicionário de pratos, onde a chave é o nome do prato e o
        # valor é uma instância de Dish
        # com o nome e preço do prato
        dishes = {
            name: Dish(name, price)
            for name, price, ingredient, amount in self.csv_data.itertuples(
                index=False
            )
        }
        # itera sobre o arquivo csv e adiciona as dependências de ingredientes
        # de cada prato
        # para isso, cria uma instância de Ingredient para cada ingrediente
        # e chama o método add_ingredient_dependency
        # para adicionar a dependência no prato correspondente

        for name, _, ingredient, amount in self.csv_data.itertuples(
            index=False
        ):
            ingredient_data = Ingredient(ingredient)
            dishes[name].add_ingredient_dependency(ingredient_data, amount)
        # atualiza o set de pratos com os pratos do dicionário criado
        # anteriormente

        self.dishes.update(dishes.values())
