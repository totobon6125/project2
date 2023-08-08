from pymongo import MongoClient
from flask import Flask, render_template, request, jsonify, session
app = Flask(__name__)

client = MongoClient('내 mongoDB주소')
db = client.dbsparta
application = app = Flask(__name__)
app.secret_key = 'any random string'

# 웹사이트 접속시 바로 로그인페이지 이동
@app.route('/')
def home():
    # if 'id' in session:
        # return render_template('index.html')  #로그인 없을때 로그인페이지로 이동
    # return render_template('login.html')  # 로그인시 메인페이지 이동
 return render_template('index.html') 


# 로그인
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        session['id'] = request.form['id']
        return render_template('index.html')
    return render_template('login.html')



@app.route("/bucket", methods=["POST"])
def bucket_post():
    bucket_receive = request.form['bucket_give']
    doc = {
        'bucket' : bucket_receive
    }
    db.bucket.insert_one(doc)
    return jsonify({'msg': '저장 완료!'})


    
@app.route("/bucket", methods=["GET"])
def bucket_get():
    all_buckets = list(db.bucket.find({}, {'_id': False}))
    return jsonify({'result': all_buckets})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)