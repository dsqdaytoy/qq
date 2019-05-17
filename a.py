from flask import Flask, jsonify, request
#flask:库/包；Flask:类（类：大写开头，需要实例化才能使用）
from flask_jwt_extended import JWTManager, create_access_token
#方法：可以直接使用 例：create_access_token
import test
#执行必须
# extened:扩张
class User(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password
app = Flask(__name__)
# 对象（字典dic）
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!
jwt = JWTManager(app)
users = {}
# signup:注册；login:登陆。   先注册再登陆
@app.route('/signup', methods=['POST'])
def signup():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if not username:
        return jsonify({"msg": "Missing username parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400
    if not username:
        return jsonify({"msg": "This username have used!"}), 201
    users[username] = User(username, password)
    return jsonify({"msg": "Signup success!"}), 200

@app.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON is request"}), 400
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if (not username) or (not password):
        return jsonify({"msg": "Missing username or password parameter"}), 400
    loginuser = users.get(username, None)
    # 如果用户名中有名字，把它返回给登陆端loginuser
    if not loginuser:
        return jsonify({"msg": "User not exists"}), 401
    elif loginuser.password == password:
        return jsonify(access_token=create_access_token(identity=username)), 200
    #access_token:对象
    else:
        return jsonify({"msg": "Password is incorrect!"}), 401

    @app.route('/test',methods=['POST'])
    def test():
        return "hello test"
    #自己写的

app.register_blueprint(test.blueprint_shi)
#执行必须
if __name__ == '__main__':
    app.run(debug=True,port=5010)
