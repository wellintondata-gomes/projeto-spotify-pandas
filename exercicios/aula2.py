"""
AULA 2 - Explorador de Faixas
==============================

Topicos aplicados:
- Inspecao de conteudo (describe, value_counts)
- Atribuicao e criacao de colunas
- Filtros simples e com AND/OR
- Dados faltantes e duplicados
"""

import pandas as pd


def carregar_e_limpar(caminho_csv: str) -> pd.DataFrame:
    """
    Carrega o CSV do Spotify e limpa os dados.

    Passos:
      1) Ler o CSV com encoding='latin-1'.
      2) Converter 'streams' para numero (pd.to_numeric com errors='coerce').
      3) Remover linhas com streams nulos (dropna).
      4) Remover duplicatas (drop_duplicates).
      5) Retornar o DataFrame limpo.
    """

    df = pd.read_csv(caminho_csv, encoding='latin-1')
    df['streams'] = pd.to_numeric(df['streams'], errors='coerce')
    df = df.dropna(subset=['streams'])
    df = df.drop_duplicates()

    return df


def inspecionar_coluna(df: pd.DataFrame, coluna: str):
    """
    Se a coluna for numerica, retorna df[coluna].describe().
    Caso contrario, retorna df[coluna].value_counts().

    Dica: use pd.api.types.is_numeric_dtype(df[coluna]).
    """

    if pd.api.types.is_numeric_dtype(df[coluna]):
        return df[coluna].describe()
    else:
        return df[coluna].value_counts()


def filtrar_por_artista(df: pd.DataFrame, artista: str) -> pd.DataFrame:
    """
    Retorna apenas as linhas em que o nome do artista CONTEM o texto buscado
    (sem diferenciar maiusculas/minusculas).

    Dica: .str.contains(artista, case=False, na=False)
    na coluna 'artist(s)_name'.
    """

    return df[
        df['artist(s)_name'].str.contains(
            artista,
            case=False,
            na=False
        )
    ]


def filtrar_hits(df: pd.DataFrame, ano_min: int, streams_min: int) -> pd.DataFrame:
    """
    Filtro com AND:
    released_year >= ano_min E streams >= streams_min.
    """

    return df[
        (df['released_year'] >= ano_min) &
        (df['streams'] >= streams_min)
    ]


def criar_categoria_streams(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cria uma coluna 'categoria_streams':
      - streams >= 1_000_000_000  -> 'Super Hit'
      - streams >= 500_000_000    -> 'Hit'
      - streams >= 100_000_000    -> 'Medio'
      - resto                     -> 'Underground'

    NAO altere o df original.
    """

    df_novo = df.copy()

    def categorizar(streams):
        if streams >= 1_000_000_000:
            return 'Super Hit'
        elif streams >= 500_000_000:
            return 'Hit'
        elif streams >= 100_000_000:
            return 'Medio'
        else:
            return 'Underground'

    df_novo['categoria_streams'] = df_novo['streams'].apply(categorizar)

    return df_novo


def filtrar_por_modo(df: pd.DataFrame, modo: str) -> pd.DataFrame:
    """
    Filtra o DataFrame por modo musical: 'Major' ou 'Minor'.
    """

    return df[df['mode'] == modo]


def filtrar_por_intervalo_ano(
    df: pd.DataFrame,
    ano_inicio: int,
    ano_fim: int
) -> pd.DataFrame:
    """
    Retorna as musicas lancadas entre ano_inicio e ano_fim.
    """

    return df[
        df['released_year'].between(
            ano_inicio,
            ano_fim
        )
    ]


def filtrar_super_dancante_ou_super_energica(
    df: pd.DataFrame,
    limite: int = 85
) -> pd.DataFrame:
    """
    Filtro com OR:
    danceability_% >= limite OU energy_% >= limite.
    """

    return df[
        (df['danceability_%'] >= limite) |
        (df['energy_%'] >= limite)
    ]


def contar_nulos_por_coluna(df: pd.DataFrame) -> pd.Series:
    """
    Retorna uma Series com a quantidade de valores nulos
    de cada coluna.
    """

    return df.isnull().sum()


def preencher_nulos_da_coluna(
    df: pd.DataFrame,
    coluna: str,
    valor
) -> pd.DataFrame:
    """
    Preenche os valores nulos da coluna informada
    sem alterar o DataFrame original.
    """

    df_novo = df.copy()
    df_novo[coluna] = df_novo[coluna].fillna(valor)

    return df_novo