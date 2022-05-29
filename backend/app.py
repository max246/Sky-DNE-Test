import click
from flask import Flask
from lib import api
import os

app = Flask(__name__, instance_relative_config=True)


#@click.command()
#@click.argument('ip')
#@click.argument('port')
#@click.argument('user')
def create_app(test_config=None):
    if test_config is not None:
        app.config.update(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    print("add blueprint")
    app.register_blueprint(api.bp)
    return app
    #app.run(host='0.0.0.0', debug=True, port=5050)

#if __name__ == '__main__':
#    create_app()
