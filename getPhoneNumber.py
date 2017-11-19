import requests
from bs4 import BeautifulSoup

def getPhoneNumber(company_list):
    search_url = "https://itp.ne.jp/result/"
    for company in company_list.strip().split("\n"):
        category, company_name = company.split("\t")
        payload = {"kw" : company_name.encode('shift-jis')}
        html = requests.get(search_url, payload)
        html.encoding = html.apparent_encoding
        tel = parse(html.text, company_name)
        print (category + "\t" + company_name + "\t" + tel)

def parse(html, ref_company_name):
    soup = BeautifulSoup(html, 'html.parser')
    div_list = soup.findAll('div', class_='normalResultsBox')
    for div_content in div_list:
        company_name = div_content.find('a', class_='blackText').getText()
        if company_name != ref_company_name:
            continue
        return div_content.find('b').getText()

company_list = open("resource/company_list.txt").read()
getPhoneNumber(company_list)
