from flask import Flask, render_template, jsonify, request, redirect, url_for

app = Flask(__name__)

from pymongo import MongoClient
import certifi

ca = certifi.where()

client = MongoClient(
    'mongodb+srv://idol_project:sparta@cluster0.cddqrid.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

SECRET_KEY = 'SPARTA'

import jwt
import datetime
import hashlib


@app.route('/')
def home():
    token_receive = request.cookies.get('mytoken')

    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = payload['id']
        return render_template('index.html', user_info=user_info)
    except jwt.ExpiredSignatureError:
        return redirect(url_for("login", msg="로그인 시간 만료"))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("login", msg="로그아웃 완료"))


@app.route('/login')
def login():
    msg = request.args.get("msg")
    return render_template('login.html', msg=msg)


@app.route('/register')
def register():
    return render_template('register.html')


# API
# 회원가입
@app.route('/api/register', methods=['POST'])
def api_register():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']
    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()
    user = db.user.find_one({'id': id_receive})
    if user is None:
        db.user.insert_one({'id': id_receive, 'pw': pw_hash})
        check = 1
    else:
        check = 0
    return jsonify({'result': 'success', 'check': check})


@app.route('/api/double', methods=['GET'])
def doubleCheck():
    user = list(db.user.find({}, {'_id': False}))
    return jsonify({'user': user})


# 로그인
@app.route('/api/login', methods=['POST'])
def api_login():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']

    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()

    result = db.user.find_one({'id': id_receive, 'pw': pw_hash})

    if result is not None:
        payload = {
            'id': id_receive,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=5 * 60)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

        return jsonify({'result': 'success', 'token': token})
    else:
        return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})


@app.route('/api/post', methods=['GET'])
def show_group():
    token_receive = request.cookies.get('mytoken')
    payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
    id = payload['id']

    group_list = list(db.idol_groups.find({}, {'_id': False}))
    like_list = db.like.find_one({"id": id}, {'_id': False})
    result_list = []
    left = []
    right = []

    for i in group_list:
        num = i["group_num"]
        if like_list is not None:
            if num in like_list["group_num"]:
                left.append(i)
            else:
                right.append(i)
        else:
            result_list.append(i)

    if len(result_list) == 0:
        result_list = left + right

    return jsonify({"group_list": result_list, "like_list": like_list})


@app.route('/api/like', methods=['POST'])
def like():
    num_receive = int(request.form["num_give"])
    token_receive = request.cookies.get('mytoken')
    payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
    id = payload['id']

    like_list = db.like.find_one({"id": id}, {'_id': False})
    like_now = db.idol_groups.find_one({"group_num": num_receive})["like"]
    if like_list is not None:
        like_list["group_num"].append(num_receive)
        db.like.update_one({"id": id}, {'$set': {'group_num': like_list["group_num"]}})

    else:
        doc = {
            "id": id,
            "group_num": [num_receive]
        }
        db.like.insert_one(doc)

    db.idol_groups.update_one({"group_num": num_receive}, {'$set': {'like': like_now + 1}})
    return jsonify({"msg": "좋아요 성공"})


@app.route('/api/like/cancel', methods=['POST'])
def like_cancel():
    num_receive = request.form["num_give"]
    token_receive = request.cookies.get('mytoken')
    payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
    id = payload['id']

    like_list = db.like.find_one({"id": id}, {'_id': False})
    like_list["group_num"].remove(num_receive)
    db.like.update_one({"id": id}, {'$set': {'group_num': like_list["group_num"]}})

    return jsonify({"msg": "좋아요 취소"})


@app.route('/api/deep', methods=["GET"])
def deep_post():
    num_receive = int(request.args.get("num"))
    group_db = db.idol_groups.find_one({"group_num": num_receive}, {"_id": False})
    group_name = group_db["group_name"]

    idol_list = list(db.idols.find({}, {"_id": False}))
    result = []
    for i in idol_list:
        if i["group"] == group_name:
            result.append(i)
    return render_template('index2.html', idol_list=idol_list, group=group_db)


@app.route("/comment", methods=["POST"])
def comment_post():
    token_receive = request.cookies.get('mytoken')
    payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
    id = payload['id']
    comment_receive = request.form['comment_give']

    doc = {
        'id': id,
        'comments': comment_receive
    }
    db.comments.insert_one(doc)
    return jsonify({'msg': '응원완료'})


@app.route("/comment", methods=["GET"])
def comment_get():
    comment_list = list(db.comments.find({}, {'_id': False}))

    return jsonify({'comments': comment_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
