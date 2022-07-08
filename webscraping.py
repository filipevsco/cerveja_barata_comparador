from bs4 import BeautifulSoup
import requests

def guardar_dados(info):
    with open(f'data/{cerveja}.txt','w') as file :
        file.write(f'{info}')

def fazer_request(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'html.parser')
    return soup

def pegar_info(soup):
    info = soup.find('p',{'class':'textstyles__TextComponent-w4b5ef-0 ilCCve'}).text
    return info

def main():
    global cerveja
    cerveja = 'cerveja-heineken-garrafa-600ml'
    url=f'https://www.clubeextra.com.br/produto/105770/{cerveja}'
    guardar_dados(pegar_info(fazer_request(url)))

if __name__ == '__main__':
    main()