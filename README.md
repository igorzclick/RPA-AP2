# 🌍📚 Sistema de Coleta de Dados de Países e Livros

Este projeto em Python permite coletar e armazenar dados de **países** (via API REST Countries) e **livros** (via web scraping no site [Books to Scrape](https://books.toscrape.com/)) em bancos de dados SQLite. Ele é ideal para aprender sobre manipulação de dados, uso de APIs, scraping com BeautifulSoup e persistência com SQLite.

---

## 🧠 Funcionalidades

- 🔎 Buscar informações de até 3 países e salvar no banco `paises.db`.
- 📚 Realizar scraping dos 10 primeiros livros disponíveis no site `books.toscrape.com` e armazenar no banco `livraria.db`.
- 🧼 Limpar dados dos bancos de dados de forma seletiva ou total.
- 🗃️ Menu interativo via terminal.

---

## 📂 Estrutura dos Bancos de Dados

### `paises.db` – Tabela: `paises`
| Campo             | Tipo     | Descrição                          |
|------------------|----------|------------------------------------|
| nome_comum       | TEXT     | Nome comum do país                 |
| nome_oficial     | TEXT     | Nome oficial                       |
| capital          | TEXT     | Capital                            |
| continente       | TEXT     | Continente                         |
| regiao           | TEXT     | Região                             |
| sub_regiao       | TEXT     | Sub-região                         |
| populacao        | INTEGER  | População                          |
| area             | REAL     | Área em km²                        |
| moeda_nome       | TEXT     | Nome da moeda                      |
| moeda_simbolo    | TEXT     | Símbolo da moeda                   |
| idioma_principal | TEXT     | Idioma principal                   |
| fuso_horario     | TEXT     | Fuso(s) horário(s)                 |
| url_bandeira     | TEXT     | Link da bandeira em PNG           |

### `livraria.db` – Tabela: `livraria`
| Campo           | Tipo | Descrição                   |
|----------------|------|-----------------------------|
| Titulo         | TEXT | Título do livro             |
| Preco          | TEXT | Preço do livro              |
| Avaliacao      | TEXT | Avaliação em estrelas       |
| Disponibilidade| TEXT | Status de disponibilidade   |

---

## ▶️ Como Usar

### ✅ Requisitos

- Python 3.8+
- Bibliotecas:
  - `requests`
  - `beautifulsoup4`
  - `urllib3`

Instale com:

```bash
pip install requests beautifulsoup4 urllib3
▶️ Execução
Salve o script como main.py e execute:

bash
Copiar
Editar
python main.py
Use o menu interativo para:

Buscar dados de países

Coletar dados de livros

Limpar os bancos de dados


Tradução automática de campos para múltiplos idiomas

🧑‍💻 Autor
Desenvolvido por [Igor Almeida Rozendo da Silva]
Sinta-se livre para contribuir com melhorias e correções!
