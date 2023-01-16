from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
import certifi

ca = certifi.where()

client = MongoClient('mongodb+srv://idol_project:sparta@cluster0.cddqrid.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

import requests
from bs4 import BeautifulSoup

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
# }
# data = requests.get("https://namu.wiki/w/방탄소년단", headers=headers)
#
# soup = BeautifulSoup(data.text, 'html.parser')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}
data = requests.get("https://www.melon.com/artist/detail.htm?artistId=672375", headers=headers)
#conts > div.wrap_dtl_atist > div > div.wrap_atist_info > p

soup = BeautifulSoup(data.text, 'html.parser')
lists = soup.select('#conts')

for list in lists:
    name = list.select_one('div > div.wrap_atist_info > p')
    soup.find("태그", attrs={"p":"strong"}).decompose()
    if name is not None:
        print(name.text)
    else:
        print("no")

@app.route('/')
def home():
    return render_template('manager.html')
@app.route("/bucket", methods=["POST"])
def bucket_post():
    url_receive = request.form['url_give']
    name_receive = request.form['name_give']
    group_receive = request.form['group_give']
    image_receive = request.form['image_give']
    birth_receive = request.form['birth_give']
    #VIVXXZe6L > div.\37 1bc97e4 > div > div > div > div.t6-tWlbV > div:nth-child(5) > div > div > div:nth-child(5) > div > div > div > div > div > div:nth-child(9) > div > div > div:nth-child(1) > div > div:nth-child(15) > div.qYoqha5U.exOsYz9X > table > tbody
    #VIVXXZe6L > div.\37 1bc97e4 > div > div > div > div.t6-tWlbV > div:nth-child(5) > div > div > div:nth-child(5) > div > div > div > div > div > div:nth-child(9) > div > div > div:nth-child(1) > div > div:nth-child(15) > div.qYoqha5U.exOsYz9X > table > tbody > tr:nth-child(2) > td:nth-child(1) > div > div

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
    }
    data = requests.get(url_receive, headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    lists = soup.select('div.qYoqha5U.exOsYz9X > table > tbody')

    for list in lists:
        name = list.select_one('div > a > span > strong')
        if name is not None:
            print(name.text)
        else:
            print("no")


    doc = {
        'name': name_receive,
        'group': group_receive,
        'image': image_receive,
        'birth': birth_receive,
    }

    db.idols.insert_one(doc)

    return jsonify({'msg': '등록 완료!'})

# if __name__ == '__main__':
#     app.run('0.0.0.0', port=5000, debug=True)