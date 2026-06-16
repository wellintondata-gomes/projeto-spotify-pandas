"""
AULA 3 - Analise do Catalogo
==============================

Topicos aplicados:
- Resumo estatistico (sum, mean, max, min, describe)
- Agrupamento com groupby
- Ordenacao com sort_values
"""

import pandas as pd


def estatisticas_gerais(df: pd.DataFrame) -> dict:
    """
    Retorna um dicionario com:
      - total_streams: soma de streams
      - media_bpm: media de bpm
      - media_danceability: media de 'danceability_%'
      - ano_mais_recente: maior released_year
      - ano_mais_antigo: menor released_year
    """

    return {
        'total_streams': df['streams'].sum(),
        'media_bpm': df['bpm'].mean(),
        'media_danceability': df['danceability_%'].mean(),
        'ano_mais_recente': df['released_year'].max(),
        'ano_mais_antigo': df['released_year'].min()
    }


def top_n_artistas_por_streams(df: pd.DataFrame, n: int = 10) -> pd.Series:
    """
    Retorna uma Series com os N artistas que mais somam streams.
    """

    return (
        df.groupby('artist(s)_name')['streams']
        .sum()
        .sort_values(ascending=False)
        .head(n)
    )


def media_features_por_modo(df: pd.DataFrame) -> pd.DataFrame:
    """
    Agrupa por 'mode' (Major / Minor) e retorna a media de:
      - danceability_%
      - energy_%
      - valence_%
    """

    return (
        df.groupby('mode')[
            ['danceability_%', 'energy_%', 'valence_%']
        ]
        .mean()
    )


def lancamentos_por_ano(df: pd.DataFrame) -> pd.Series:
    """
    Contagem de musicas lancadas por ano.
    """

    return (
        df.groupby('released_year')
        .size()
        .sort_index()
    )


def artista_mais_streamado_do_ano(df: pd.DataFrame, ano: int) -> str:
    """
    Retorna o artista que mais somou streams em um determinado ano.
    """

    df_ano = df[df['released_year'] == ano]

    if df_ano.empty:
        return f"Nenhuma musica encontrada para {ano}"

    return (
        df_ano.groupby('artist(s)_name')['streams']
        .sum()
        .sort_values(ascending=False)
        .index[0]
    )


def top_n_musicas_mais_dancantes(df: pd.DataFrame, n: int = 10) -> pd.DataFrame:
    """
    Retorna as N musicas mais dancantes.
    """

    return (
        df.sort_values(
            by='danceability_%',
            ascending=False
        )
        .head(n)[
            ['track_name', 'artist(s)_name', 'danceability_%']
        ]
    )


def streams_por_decada(df: pd.DataFrame) -> pd.Series:
    """
    Soma os streams por decada.
    """

    df_novo = df.copy()

    df_novo['decada'] = (
        df_novo['released_year'] // 10
    ) * 10

    return (
        df_novo.groupby('decada')['streams']
        .sum()
        .sort_index()
    )


def bpm_medio_por_modo(df: pd.DataFrame) -> pd.Series:
    """
    Retorna o BPM medio por modo.
    """

    return (
        df.groupby('mode')['bpm']
        .mean()
    )


def musicas_por_quantidade_de_artistas(df: pd.DataFrame) -> pd.Series:
    """
    Conta quantas musicas existem para cada quantidade de artistas.
    """

    return (
        df['artist_count']
        .value_counts()
        .sort_index()
    )


def ano_com_mais_streams(df: pd.DataFrame) -> int:
    """
    Retorna o ano que acumulou mais streams.
    """

    return (
        df.groupby('released_year')['streams']
        .sum()
        .idxmax()
    )