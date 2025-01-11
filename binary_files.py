import requests

url_pdf = 'https://chtyvo.org.ua/authors/Falkovych_Hryhorii/Smyk-tyndyk.pdf'

response = requests.get(url_pdf)
pdf_content = response.content

with open('smyk_tyndyk.pdf', mode='bw') as story:
    story.write(pdf_content)
