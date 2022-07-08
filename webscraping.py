from bs4 import BeautifulSoup
import requests

def fazer_request(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'html.parser')
    return soup

def pegar_info(soup):
    info = soup.find('p',{'class':'textstyles__TextComponent-w4b5ef-0 ilCCve'}).text
    print(info)

def main():
    url='https://www.clubeextra.com.br/produto/105770/cerveja-heineken-garrafa-600ml'
    pegar_info(fazer_request(url))

if __name__ == '__main__':
    main()