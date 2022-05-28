from flask import Blueprint
from lib.vsr1000 import *

api = Blueprint('api', __name__)

@api.route('/')
def index():
    return "hello"