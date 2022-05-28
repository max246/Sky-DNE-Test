import click
from flask import Flask
from lib.api import *

app = Flask(__name__)
app.register_blueprint(api)

@click.command()
@click.argument('ip')
@click.argument('port')
@click.argument('user')
def main(ip, port, user):
    app.run(host='0.0.0.0', debug=False, port=5050)

if __name__ == '__main__':
    main()
