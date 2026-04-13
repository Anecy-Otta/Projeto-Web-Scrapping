import os
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import pandas as pd

def buscar_noticias():
    url = "https://g1.globo.com/tecnologia/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    print(f"Acessando: {url}...")
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print("Erro ao acessar o site!")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    lista_noticias = []

    posts = soup.find_all('div', class_='feed-post-body')

    for post in posts:
        link_tag = post.find('a', class_='feed-post-link')
        resumo_tag = post.find('div', class_='feed-post-body-resumo')
        
        if link_tag:
            titulo = link_tag.text.strip()
            link = link_tag['href']
            resumo = resumo_tag.text.strip() if resumo_tag else "Sem resumo"
            
            lista_noticias.append({
                "titulo": titulo,
                "resumo": resumo,
                "link": link,
                "data_coleta": datetime.now().strftime("%d/%m/%Y %H:%M")
            })

    df = pd.DataFrame(lista_noticias)

    # Caminho para a pasta 'data' dentro de 'src'
    data_dir = os.path.join(os.path.dirname(__file__), "data")
    os.makedirs(data_dir, exist_ok=True)

    output_path = os.path.join(data_dir, "noticias_tech.csv")
    df.to_csv(output_path, index=False, encoding="utf-8-sig")

    print(f"Sucesso! {len(lista_noticias)} notícias coletadas e salvas em '{output_path}'.")

if __name__ == "__main__":
    buscar_noticias()