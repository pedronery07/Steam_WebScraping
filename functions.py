import requests
from bs4 import BeautifulSoup
    
def baixar_pagina(url : str) -> str:
    """
    Retorna o conteúdo html da página que se deseja baixar.

    Args:
        url (str): url da página sendo baixada.

    Returns:
        url.text (str): código html da página baixada.
    """

    url = requests.get(url)
    url.encoding = "utf-8"
    return url.text

def extrair_genero(pagina : str, lista_generos : list):
    """
    Devolve todos os gêneros associados ao jogo mostrado na página

    Args:
        pagina (str): conteúdo html da página do jogo.

    Returns:
        lista_generos (list): lista com todos os gêneros associados ao jogo.
    """

    soup = BeautifulSoup(pagina, "html.parser")
    for tag in soup.find_all("a", class_="app_tag"):
        lista_generos.append(tag.text.strip("\n\t"))
    return lista_generos