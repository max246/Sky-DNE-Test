from flask import Blueprint, request,abort,jsonify
from lib.vsr1000 import *

bp = Blueprint('api', __name__)
router = VSR1000("host", "port", "user", "pass")


@bp.route('/',methods=['GET'])
def list_loopback():
    #router.list_loopback()
    return jsonify({"result": "ok", "message": "list loopback"})

@bp.route('/loopback/add',methods=['POST'])
def add_loopback():
    data = request.get_json()
    if "id" in data and "ip" in data:
        id = data['id']
        ip = data['ip']
        router.add_loopback(id, ip)
        return jsonify({"result": "ok", "message":"add loopback"})
    else:
        abort(500)

@bp.route('/loopback/del',methods=['POST'])
def del_loopback():
    data = request.get_json()
    if "id" in data and "ip" in data:
        id = data['id']
        ip = data['ip']
        router.del_loopback(id, ip)
        return jsonify({"result":"ok", "message": "del loopback"})
    else:
        abort(500)
