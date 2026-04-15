# Projeto Web Scrapping

Este projeto realiza coleta e análise de manchetes de tecnologia do portal G1 usando Python.

## Objetivo
Coleta automatizada de notícias para análise de tendências tecnológicas.

## Tecnologias
- Python 3.13+
- Requests
- BeautifulSoup4
- Pandas

## Como rodar

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/Anecy-Otta/Projeto-Web-Scrapping.git
   cd Projeto-Web-Scrapping
   ```

2. **Crie e ative o ambiente virtual:**
   ```bash
   python -m venv venv
   venv\Scripts\activate   # Windows
   source venv/bin/activate # Linux/Mac
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute o scraper:**
   ```bash
   python src/scraper.py
   ```

5. **Saída esperada:**
   - O script acessa o portal G1.
   - Coleta títulos, resumos e links das notícias.
   - Salva os resultados em `data/noticias_tech_data_hora.csv`.


## Estrutura do projeto
```
Projeto Web Scrapping/
├── src/
│   ├── scraper.py        # Código principal
│   └── data/             # Pasta onde os CSVs são salvos
├── requirements.txt      # Dependências do projeto
├── README.md             # Documentação
└── venv/                 # Ambiente virtual (não versionado)
```

## Observações
- Sempre que instalar novas bibliotecas, atualize o `requirements.txt`:
  ```bash
  pip freeze > requirements.txt
  ```
- O script cria/atualiza automaticamente o arquivo `noticias_tech_data_hora.csv` dentro da pasta `data/`.
```