from pymongo import MongoClient
from bson.objectid import ObjectId
from flask import Flask, render_template, request, jsonify, session, redirect, url_for, flash
import re

client = MongoClient('mongodb+srv://sparta:test@cluster0.lzwl4ms.mongodb.net/?retryWrites=true&w=majority')

db = client.dbsparta
application = app = Flask(__name__)
app.secret_key = 'any random string'

 

# 홈화면
@app.route('/')
def home():
    if 'email' in session:
        email = session['email']
        logged_in = True
        return render_template('index2.html', email=email, logged_in=logged_in)
    else:
        return render_template('index.html')


# 조원소개
@app.route('/teamMember')
def teamMember():
    if 'email' in session:
        email = session['email']
        logged_in = True
        return render_template('teamMember.html', email=email, logged_in=logged_in)
    else:
        return render_template('teamMember2.html')


# 전체 글 목록 조회(index.html) 
@app.route("/bucket/list", methods=["GET"])
def bucket_list():
    all_buckets = list(db.bucket.find({}, {'_id': True, 'bucket': True, 'likeCount': True, 'dislikeCount': True}))
    result = []

    for item in all_buckets:
        item['_id'] = str(item['_id'])  # _id 값을 문자열로 변환하여 다시 할당
        result.append(item)

    return jsonify({'result': result})

# 좋아요, 싫어요 카운팅 업데이트
@app.route('/update', methods=['POST'])
def update_like_dislike():
    item_id = request.form['itemId']
    type = request.form['type']  # likeCount, dislikeCount로 전달됨
    new_count = int(request.form['count'])  # 계산할 카운트 값

    # MongoDB의 해당 아이템 업데이트
    # $inc 연산자를 사용하여 변경된 값을 기존 값에 더함
    db.bucket.update_one({'_id': ObjectId(item_id)}, {'$inc': {type: new_count}})

    return jsonify({'msg': '업데이트 완료!'})

# 내 방명록 쓰기 및 보기 페이지
@app.route('/writeAndMyview')
def write_and_myview():
    if 'email' in session:
        email = session['email']
        logged_in = True

        # 사용자의 방명록 데이터를 불러옴
        user_buckets = list(db.bucket.find({'email': email}))

        return render_template('writeAndMyview.html', email=email, logged_in=logged_in, user_buckets=user_buckets)
    else:
        return redirect(url_for('login'))


# 내 방명록 쓰기
@app.route("/bucket", methods=["POST"])
def bucket_post():
    bucket_receive = request.form['bucket_give']
    email = session['email']
    doc = {
        'bucket': bucket_receive,
        'done': False,
        'comments': [],
        'email': email,
        'likeCount' : 0,
        'dislikeCount': 0
    }

    db.bucket.insert_one(doc)

    return jsonify({'msg': '등록 완료!'})

# 수정
@app.route("/bucket/update_bucket", methods=["POST"])
def update_bucket():
    bucket_id = request.form['bucketId']
    new_bucket = request.form['newBucket']

    db.bucket.update_one({'_id': ObjectId(bucket_id)}, {'$set': {'bucket': new_bucket}})
    db.bucket.update_one({'_id': ObjectId(bucket_id)}, {'$set': {'done': False}})

    return jsonify({'msg': '수정 완료!'})

# 체크
@app.route("/bucket/done", methods=["POST"])
def bucket_done():
    id_receive = request.form['id_give']
    db.bucket.update_one({'_id': ObjectId(id_receive)}, {'$set': {'done': True}})
    return jsonify({})

# 완료
@app.route("/bucket/cancel", methods=["POST"])
def bucket_cancel():
    id_receive = request.form['id_give']
    db.bucket.update_one({'_id': ObjectId(id_receive)}, {'$set': {'done': False}})
    return jsonify({'msg': ''})

# 삭제
@app.route("/bucket/delete", methods=["POST"])
def bucket_delete():
    id_receive = request.form['id_give']
    db.bucket.delete_one({'_id': ObjectId(id_receive)})
    return jsonify({'msg': '삭제 완료!'})

# 조회
@app.route("/bucket", methods=["GET"])
def bucket_get():
    if 'email' in session:
        email = session['email']
        user_buckets = list(db.bucket.find({'email': email}))

        for i in range(len(user_buckets)):
            user_buckets[i]['_id'] = str(user_buckets[i]['_id'])

        return jsonify({'buckets': user_buckets})
    else:
        return jsonify({'msg': '로그인이 필요합니다.'})


# 회원가입
@app.route('/join', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        existing_user = db.users.find_one({'email': email})

        if not isValidEmail(email):
            flash('올바른 이메일 형식이 아닙니다')
            return render_template('join.html')

        if not isValidPassword(password):
            flash('올바른 암호 형식이 아닙니다.')
            return render_template('join.html')

        if existing_user:
            flash('이미 사용 중인 아이디 입니다')
            return render_template('join.html')

        new_user = {'email': email, 'password': password}
        db.users.insert_one(new_user)

        flash('회원가입 성공! 로그인해주세요')
        return redirect(url_for('login'))

    return render_template('join.html')

# 유효한 이메일인지 검사
def isValidEmail(email):
    emailRegex = re.compile(r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$')
    return emailRegex.match(email)

# 유효한 암호인지 검사
def isValidPassword(password):
    passwordRegex = re.compile(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$')
    return passwordRegex.match(password)

# 로그인
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = db.users.find_one({'email': email})

        if user and user['password'] == password:
            session['email'] = email
            return redirect(url_for('home'))
        else:
            flash('아이디 또는 비밀번호가 틀렸습니다')
            return redirect(url_for('login'))

    return render_template('login.html')

# 로그아웃
@app.route('/logout', methods=["GET"])
def logout():
    session.pop('email', None)
    return render_template('login.html')

if __name__ == '__main__':
    app.run()
