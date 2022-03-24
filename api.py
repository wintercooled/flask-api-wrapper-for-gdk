import flask
from flask import jsonify, request

from gdk_wrapper import GDKWrapper

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Flask API for acessing GDK</h1>
<p>A prototype API for wrapping <a href='https://github.com/Blockstream/gdk'>GDK<a/></p>'''


@app.route('/api/v1/example', methods=['GET'])
def api_example():
    wallet = GDKWrapper.create_wallet()
    gaid = wallet.gaid

    example = {
        'wallet_gaid': gaid
    }
    return jsonify(example)

app.run()
