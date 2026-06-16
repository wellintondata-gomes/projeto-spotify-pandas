"""
AULA 1 - Primeiros passos com Pandas
======================================

Topicos aplicados:
- Importacao da biblioteca
- Criacao de Series e DataFrames
- Importacao de dados (read_csv)
- Inspecao de conjunto (shape, columns, index)
- Inspecao de coluna (dtypes, info)
- Renomear colunas
- set_index / reset_index

Preencha as funcoes marcadas com `# TODO`.
"""

import pandas as pd


def criar_series_simples(valores: list, indices: list) -> pd.Series:
    """
    Cria uma pd.Series a partir de uma lista de valores e uma lista de indices.

    Exemplo:
      criar_series_simples([10, 22, 48], ['a', 'b', 'c'])
      -> Series com indice ['a', 'b', 'c'] e valores [10, 22, 48]

    Dica: pd.Series(data=..., index=...)
    """
    # TODO: implemente
    

    return pd.Series(data=valores, index=indices)
    raise NotImplementedError("Funcao criar_series_simples ainda nao implementada (aula 1)")


def criar_dataframe_de_dict(dados: dict) -> pd.DataFrame:
    """
    Cria um pd.DataFrame a partir de um dicionario onde cada chave vira
    uma coluna e cada lista vira os valores.

    Exemplo:
      criar_dataframe_de_dict({'nome': ['Ana', 'Bob'], 'idade': [20, 25]})
      -> DataFrame com colunas 'nome' e 'idade'
    """
    # TODO: implemente

    def criar_dataframe_de_dict(dados: dict) -> pd.DataFrame:
      return pd.DataFrame(dados)
    raise NotImplementedError("Funcao criar_dataframe_de_dict ainda nao implementada (aula 1)")


def obter_dimensoes(df: pd.DataFrame) -> tuple:
    """
    Retorna a quantidade de linhas e colunas como uma tupla (linhas, colunas).

    Dica: o atributo .shape ja retorna uma tupla pronta.
    """
    # TODO: implemente
    def obter_dimensoes(df: pd.DataFrame) -> tuple:
      return df.shape
    raise NotImplementedError("Funcao obter_dimensoes ainda nao implementada (aula 1)")


def renomear_colunas(df: pd.DataFrame, mapeamento: dict) -> pd.DataFrame:
    """
    Renomeia colunas do DataFrame seguindo o mapeamento.

    Exemplo:
      renomear_colunas(df, {'streams': 'reproducoes'})
      -> df com a coluna 'streams' renomeada para 'reproducoes'

    NAO modifique o df original. Retorne um NOVO DataFrame (use inplace=False
    ou nao use inplace).

    Dica: df.rename(columns=mapeamento) ja retorna um novo df.
    """
    # TODO: implemente
    def renomear_colunas(df: pd.DataFrame, mapeamento: dict) -> pd.DataFrame:
      return df.rename(columns=mapeamento)
    raise NotImplementedError("Funcao renomear_colunas ainda nao implementada (aula 1)")


def definir_indice(df: pd.DataFrame, coluna: str) -> pd.DataFrame:
    """
    Define a coluna informada como indice do DataFrame.

    Exemplo:
      definir_indice(df, 'track_name')
      -> df com 'track_name' como indice

    Dica: df.set_index(coluna)
    """
    # TODO: implemente
    def definir_indice(df: pd.DataFrame, coluna: str) -> pd.DataFrame:
      return df.set_index(coluna)
    raise NotImplementedError("Funcao definir_indice ainda nao implementada (aula 1)")


def tipos_das_colunas(df: pd.DataFrame) -> pd.Series:
    """
    Retorna uma Series onde o indice e o nome da coluna e o valor e o tipo
    de dado dela.

    Dica: o atributo .dtypes ja retorna isso.
    """
    # TODO: implemente
    def tipos_das_colunas(df: pd.DataFrame) -> pd.Series:
      return df.dtypes
    raise NotImplementedError("Funcao tipos_das_colunas ainda nao implementada (aula 1)")
