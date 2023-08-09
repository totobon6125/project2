from pymongo import MongoClient
from bson.objectid import ObjectId
from flask import Flask, render_template, request, jsonify, session

client = MongoClient('mongodb+srv://sparta:test@cluster0.a0mnxnt.mongodb.net/?retryWrites=true&w=majority')

db = client.dbsparta
application = app = Flask(__name__)
app.secret_key = 'any random string'

 

# 홈화면
@app.route('/')
def home():
    id= session.get('id',None)
    return render_template('index.html',id=id)

# 전체글 목록조회(list) 
@app.route("/bucket", methods=["GET"])
def bucket_get():
    all_buckets = list(db.bucket.find({}, {'_id': False}))
    return jsonify({'result': all_buckets})

# 좋아요, 싫어요 카운팅-미완성
@app.route('/update', methods=['POST'])
def update_like_dislike():
    data = request.json
    item_id = data['id']
    like_count = data['likeCount']
    dislike_count = data['dislikeCount']

    # MongoDB의 해당 아이템 업데이트
    db.bucket.update_one({'_id': ObjectId(item_id)}, {'$set': {'likeCount': like_count, 'dislikeCount': dislike_count}})

    return jsonify({'msg': '업데이트 완료!'})




# 내 방명록 쓰기 및 보기페이지
@app.route('/writeAndMyview')
def write():
    return render_template('writeAndMyview.html')
    # if 'id' in session:
    #     id= session.get('id',None)
    #     return render_template('writeAndMyview.html',id=id)
    # return render_template('login.html')


# 내 방명록 쓰기, 보기-id별 식별 필요함
@app.route("/bucket", methods=["POST"])
def bucket_post():
    bucket_receive = request.form['bucket_give']
    like_receive = int(request.form['likeCount'])
    dislike_receive = int(request.form['dislikeCount'])
    doc = {
        'bucket' : bucket_receive,
        'likeCount' : like_receive,
        'dislikeCount': dislike_receive
    }
    db.bucket.insert_one(doc)
    return jsonify({'msg': '저장 완료!'})



# 회원가입
@app.route('/join')
def join():
    #코드기입
    return render_template('join.html')



# 로그인
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        session['id'] = request.form['id']
        id= session.get('id',None)
        return render_template('index.html',id=id)
    return render_template('login.html')


# 로그아웃 - 코드 수정 안해도 됨
@app.route('/logout', methods=["GET"])
def logout():
    session.pop('id', None)
    return render_template('index.html')



if __name__ == '__main__':
    app.run()
