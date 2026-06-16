"""
AULA 4 - Dashboard Visual + Export
====================================

Topicos aplicados:
- Visualizacao de dados (matplotlib)
- Conectando dados (concat e merge)
- Salvando dados (to_csv, to_excel, download)

As funcoes de grafico devem RETORNAR a figura matplotlib (fig), nao chamar
plt.show(). O Streamlit cuida de exibir.
"""

import io
import pandas as pd
import matplotlib.pyplot as plt


def grafico_barras_top_artistas(df: pd.DataFrame, n: int = 10):


    top_artistas = (
        df.groupby('artist(s)_name')['streams']
        .sum()
        .sort_values(ascending=False)
        .head(n)
    )

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.barh(
        top_artistas.index,
        top_artistas.values
    )

    ax.set_title(f"Top {n} artistas por streams")
    ax.set_xlabel("Streams")
    ax.set_ylabel("Artista")

    return fig


def grafico_pizza_modo(df: pd.DataFrame):

    modos = df['mode'].value_counts()

    fig, ax = plt.subplots(figsize=(8, 8))

    ax.pie(
        modos.values,
        labels=modos.index,
        autopct='%1.1f%%'
    )

    ax.set_title("Distribuição dos modos musicais")

    return fig


def grafico_linha_lancamentos_por_ano(df: pd.DataFrame):

    dados = (
        df[df['released_year'] >= 2000]
        .groupby('released_year')
        .size()
    )

    fig, ax = plt.subplots(figsize=(10, 5))

    ax.plot(
        dados.index,
        dados.values
    )

    ax.set_title("Lançamentos por ano")
    ax.set_xlabel("Ano")
    ax.set_ylabel("Quantidade")

    return fig


def juntar_com_info_artistas(
    df_spotify: pd.DataFrame,
    df_info: pd.DataFrame
) -> pd.DataFrame:

    return pd.merge(
        df_spotify,
        df_info,
        left_on='artist(s)_name',
        right_on='artist_name',
       how='left'
    )


  

def unir_novos_lancamentos(
    df_atual: pd.DataFrame,
    df_novos: pd.DataFrame
) -> pd.DataFrame:

    return (
        pd.concat(
            [df_atual, df_novos],
            axis=0
        )
        .drop_duplicates()
    )


def salvar_resultado(
    df: pd.DataFrame,
    caminho: str
) -> None:

    df.to_csv(
        caminho,
        index=False,
        encoding='utf-8'
    )


def grafico_dispersao_energia_dancabilidade(df: pd.DataFrame):

    fig, ax = plt.subplots(figsize=(8, 6))

    ax.scatter(
        df['energy_%'],
        df['danceability_%'],
        alpha=0.5
    )

    ax.set_title(
        "Energia x Dançabilidade"
    )

    ax.set_xlabel("Energia (%)")
    ax.set_ylabel("Dançabilidade (%)")

    return fig


def grafico_histograma_bpm(
    df: pd.DataFrame,
    bins: int = 30
):

    fig, ax = plt.subplots(figsize=(8, 6))

    ax.hist(
        df['bpm'],
        bins=bins
    )

    ax.set_title("Distribuição de BPM")
    ax.set_xlabel("BPM")
    ax.set_ylabel("Quantidade")

    return fig


def salvar_em_excel(
    df: pd.DataFrame,
    caminho: str
) -> None:

    df.to_excel(
        caminho,
        index=False
    )


def preparar_csv_para_download(
    df: pd.DataFrame
) -> bytes:

    csv_string = df.to_csv(index=False)

    return csv_string.encode('utf-8')