from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:starta@cluster0.yu3o2z7.mongodb.net/cluster0?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('오픈박스_html')

@app.route("/comments", methods=["POST"])
def comment_post():
    comment_receive = request.form['comment_give']

    doc = {
        'comment': comment_receive,
    }
    db.comments.insert_one(doc)
    return jsonify({'msg': '응원완료'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
