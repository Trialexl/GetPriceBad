import requests
# import json
from bs4 import BeautifulSoup
from flask import Flask, request, jsonify, g

from config import UrlService, UrlLogin,UrlLogout,User,Password




app = Flask(__name__)

def GetPrice(Code,PHPSESSID):
    url = UrlService+Code

    payload = {}
    headers = {
    'Cookie': 'PHPSESSID='+ PHPSESSID
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    soup = BeautifulSoup(response.text, 'html.parser')   
    # products =soup.findAll(class_ = 'table')
    Price = 0
    tbody =soup.find('tbody')
    if tbody:
        raw_records = tbody.select("tbody > tr")
        
        for raw_record in raw_records:
            columns = raw_record.find_all("td")
            Price =  columns[1].text.replace('\n','')       
    return Price

def Login():
   
    PHPSESSID = '07fa7b08fb77b7087062a4d396a99269'
    
    payload = {'user': User,
    'pass': Password,
    'submit': 'enter'}
    files=[
    ]
    headers = {
        'Cookie': 'PHPSESSID='+ PHPSESSID
    
    }
    response = requests.request("POST", UrlLogin, headers=headers, data=payload, files=files)
    for cookie in response.cookies:
        if cookie.name == 'PHPSESSID':
            PHPSESSID = cookie.value    
    return PHPSESSID    
def Logout(PHPSESSID):
    payload = {
    }
    files=[
    ]
    headers = {
    'Cookie': 'PHPSESSID='+ PHPSESSID
    }

    response = requests.request("GET", UrlLogout, headers=headers, data=payload, files=files)          

@app.route('/GetPrice/', methods=['POST'])
def GetPriceWeb():
    
    data = request.get_json()
    if 'text' not in data:
        return jsonify({'code': 'Не был передан необходимый параметр'})
    
    Price = GetPrice(data['Code'], data['PHPSESSID'])
    
    
    return jsonify({'Price':Price })

    
@app.route('/Login/', methods=['POST'])
def LoginWeb():
    PHPSESSID = Login()
    return jsonify({'PHPSESSID':PHPSESSID })

@app.route('/Logout/', methods=['POST'])
def LogoutWeb():
    data = request.get_json()
    if 'PHPSESSID' not in data:
        return jsonify({'m': 'Не был передан необходимый параметр'})
    Logout(data['PHPSESSID'])
    return jsonify({'m':'bye'})


if __name__ == '__main__':
    app.run()