import requests

from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.in/Bajaj-Flora-3-Litre-Instant-Heater/dp/B009P2LG0C/ref=sr_1_3?keywords=geyser&qid=1572411621&sr=8-3'

headers = {"User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}

def check_price():

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id = "productTitle").get_text()

    a = soup.find(id = "priceblock_ourprice").get_text()

    r1 = len(a)
    s = ''
    for i in range(0,r1-1):
        if(a[i]=='1' or a[i]=='2'or a[i]=='3' or a[i]=='4' or a[i]=='5' or a[i]=='6' or a[i]=='7' or a[i]=='8' or a[i]=='9' or a[i]=='0'):
            s = s + a[i]
        if(a[i] == '.'):
            break

    converted_price = float(s)

    if( converted_price < 2000.0):
        send_mail()

    print(title.strip())
    print(converted_price)

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('apratimdas18@gmail.com', 'bwdaobdpugwmimbp')
    subject = "Price Fell Down!"
    body = 'https://www.amazon.in/Bajaj-Flora-3-Litre-Instant-Heater/dp/B009P2LG0C/ref=sr_1_3?keywords=geyser&qid=1572411621&sr=8-3'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'apratimdas18@gmail.com',
        'arpan.stemcelltherapy.das@gmail.com',
        msg
    )
    print('Hey email has been sent!!')

    server.quit()


check_price()
