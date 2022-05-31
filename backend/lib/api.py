from flask import Blueprint, request,abort,jsonify
from lib.vsr1000 import *

api = Blueprint('api', __name__)
router = VSR1000("host", "port", "user", "pass")

@api.route('/',methods=['GET'])
def list_loopback():
    result = router.list_loopback()
    return jsonify({"result": "ok", "message": "list loopback"})

@api.route('/loopback/add',methods=['POST'])
def add_loopback():
    data = request.get_json()
    if "id" in data and "ip" in data:
        id = data['id']
        ip = data['ip']
        result = router.add_loopback(id, ip)
        if result is None:
            abort(400)
        else:
            return jsonify({"result": "ok", "message":"add loopback"})
    else:
        abort(500)

@api.route('/loopback/del',methods=['POST'])
def del_loopback():
    data = request.get_json()
    if "id" in data and "ip" in data:
        id = data['id']
        ip = data['ip']
        result = router.del_loopback(id, ip)
        if result is None:
            abort(400)
        else:
            return jsonify({"result":"ok", "message": "del loopback"})
    else:
        abort(500)
