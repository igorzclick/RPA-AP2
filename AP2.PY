import requests
import sqlite3
from bs4 import BeautifulSoup
from os import sys
sys.stdout.reconfigure(encoding='utf-8')
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



def criar_banco_livros():
    conn= sqlite3.connect('livraria.db')
    cursor=conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS livraria(
                   Titulo TEXT,
                   Preco TEXT,
                   Avaliacao TEXT,
                   Disponibilidade TEXT)    '''

    )
    conn.commit()
    conn.close()
def criar_banco_paises():
    conn = sqlite3.connect('paises.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS paises (
            nome_comum TEXT,
            nome_oficial TEXT,
            capital TEXT,
            continente TEXT,
            regiao TEXT,
            sub_regiao TEXT,
            populacao INTEGER,
            area REAL,
            moeda_nome TEXT,
            moeda_simbolo TEXT,
            idioma_principal TEXT,
            fuso_horario TEXT,
            url_bandeira TEXT
        )
    ''')
    conn.commit()
    conn.close()
    





def coletar_dados_paises():
    criar_banco_paises()
    conn = sqlite3.connect('paises.db')
    cursor = conn.cursor()

    print("\n🌍 Coleta de dados de países")
    paises = []
    for i in range(3):
        nome = input(f"Digite o nome do {i+1}º país: ").strip()
        paises.append(nome)

    for pais in paises:
        try:
            response = requests.get(f'https://restcountries.com/v3.1/name/{pais}')
            response.raise_for_status()
            data = response.json()[0]
            print(data)

            nome_comum = data['name']['common']
            nome_oficial = data['name']['official']
            capital = ', '.join(data.get('capital', ['Desconhecida']))
            continente = data.get('continents', ['Desconhecido'])[0]
            regiao = data.get('region', 'Desconhecida')
            sub_regiao = data.get('subregion', 'Desconhecida')
            populacao = data.get('population', 0)
            area = data.get('area', 0.0)

            moedas = list(data.get('currencies', {}).values())[0]
            moeda_nome = moedas.get('name', 'Desconhecida')
            moeda_simbolo = moedas.get('symbol', 'N/A')

            idiomas = list(data.get('languages', {}).values())
            idioma_principal = idiomas[0] if idiomas else 'Desconhecido'

            fuso = ', '.join(data.get('timezones', ['Desconhecido']))
            url_bandeira = data.get('flags', {}).get('png', '')

            cursor.execute('''
                INSERT INTO paises VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                nome_comum, nome_oficial, capital, continente, regiao, sub_regiao,
                populacao, area, moeda_nome, moeda_simbolo,
                idioma_principal, fuso, url_bandeira
            ))

            print(f"✅ Dados do país '{nome_comum}' inseridos com sucesso.")
        except Exception as e:
            print(f"❌ Erro ao buscar dados de '{pais}': {e}")

    conn.commit()
    conn.close()


def coletar_dados_livros():
    criar_banco_livros()
    conn = sqlite3.connect('livraria.db')
    cursor = conn.cursor()
    print("\n📚 Coleta de dados dos 10 primeiros livros:\n")
    url_base = 'https://books.toscrape.com/'
    
    try:
        response = requests.get(url_base, verify= False)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        livros = soup.select('article.product_pod')[:10]

        for i, livro in enumerate(livros, start=1):
            titulo = livro.h3.a['title']
            preco = livro.select_one('.price_color').text
            disponibilidade = livro.select_one('.availability',).text.strip()
            estrelas = livro.select_one('.star-rating')['class'][1]
            cursor.execute('''
            
                INSERT INTO livraria (Titulo, Preco, Avaliacao, Disponibilidade)
                            VALUES (?,?,?,?)
            ''', (titulo, preco, estrelas, disponibilidade,))
            conn.commit()
            print('Dados ds livros inseridos com sucesso!')
            
            print(f"\n🔹 Livro {i}")
            print(f"  Título: {titulo}")
            print(f"  Preco: {preco}")
            print(f"  Avaliação: {estrelas} estrelas")
            print(f"  Disponibilidade: {disponibilidade}")
    except Exception as e:
            print(f'erro ao subir os livros no banco de dados {e}')
        


    except Exception as e:
        print(f"❌ Erro ao coletar dados dos livros: {e}")


def menu():
    conn=sqlite3.connect('paises.db')
    cursor=conn.cursor()
    while True:
        print("\n=====================")
        print("📊 SISTEMA DE COLETA")
        print("=======================")
        print("1. Coletar dados de países")
        print("2. Coletar dados de livros")
        print("3. Apagar valores Banco de dados de Paises")
        print("4. Apagar valores Banco de dados de Livros")
        print("5. DELETA TUDO ")
        print("4. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            coletar_dados_paises()
        elif escolha == '2':
            coletar_dados_livros()
        elif escolha == '3':
            try:
                cursor.execute('DELETE FROM paises')
                conn.commit()  
                print(' Todos os dados da tabela "paises" foram deletados.')
            except Exception as e:
                print(f"❌ Erro ao deletar os dados: {e}")
        elif escolha == '4':
            try:
                cursor.execute('DELETE FROM livraria')
                conn.commit()  
                print(' Todos os dados da tabela "livraria" foram deletados.')
            except Exception as e:
                print(f"❌ Erro ao deletar os dados: {e}") 
        elif escolha == '5':
            try:
                cursor.execute('DROP TABLE IF EXISTS livraria')
                cursor.execute('DROP TABLE IF EXISTS paises')
                conn.commit()  
                print(' Todos os bancos de dados foram deletados.')
            except Exception as e:
                print(f"❌ Erro ao deletar os dados: {e}")        
                
        elif escolha==5:
            print('Saindo....')    
            break
        else:
            print("Opção inválida. Tente novamente.")


if _name_ == '_main_':
    menu()