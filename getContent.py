from bs4 import BeautifulSoup

def getContents(html):
    soup = BeautifulSoup(html, 'html.parser')
    ul_list = soup.findAll('span', itemprop='title')
    category = ul_list[1].getText()
    company = soup.find('div', class_='company').getText()
    print(category + '\t' + company)

html = open("resource/en_detail.html").read()
company_names = getContents(html)
