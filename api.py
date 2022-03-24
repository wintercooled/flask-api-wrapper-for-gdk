import flask
from flask import jsonify, request

from config import Config
from gdk_wrapper import GDKWrapper

app = flask.Flask(__name__)
app.config.from_object(Config)
app.config["DEBUG"] = True


################################
# HELPER FUNCTIONS
################################
# TODO - can get and can post are just examples, you can create different
#        permissions/roles as needed.
def can_get(headers):
    token = headers.get('Authorization', None)
    get_token = app.config['GET_TOKEN']
    if token and token == get_token:
        return True
    return False


def can_post(headers):
    token = headers.get('Authorization', None)
    post_token = app.config['POST_TOKEN']
    if token and token == post_token:
        return True
    return False


################################
# ROUTES
################################
@app.route('/', methods=['GET'])
def home():
    return '''<h1>Flask API for acessing GDK</h1>
<p>A prototype API for wrapping <a href='https://github.com/Blockstream/gdk'>GDK<a/></p>'''


@app.route('/api/v1/example', methods=['GET'])
@app.route('/api/v1/example_no_auth', methods=['GET'])
def api_example_no_auth():
    example = {
        'example_key': 'example_value'
    }

    return jsonify(example)


@app.route('/api/v1/example_auth', methods=['GET'])
def api_example_auth():
    if can_get(request.headers) or can_post(request.headers):
        example = {
            'example_key': 'example_value'
        }

        return jsonify(example)
    else:
        return {'error': 'Invalid or missing header Authorization token'}


@app.route('/api/v1/wallet/create', methods=['GET'])
def wallet_create():
    if can_get(request.headers):
        wallet = GDKWrapper.create_wallet(app.config['NETWORK_NAME'])
        gaid = wallet.gaid
        mnemonic = wallet.mnemonic

        wallet_json = {
            'gaid': gaid,
            'mnemonic': mnemonic,
        }
        return jsonify(wallet_json)
    else:
        return {'error': 'Invalid or missing header Authorization token'}


@app.route('/api/v1/wallet/balance', methods=['POST'])
def wallet_balance():
    if can_post(request.headers):
        data = request.get_json()
        errors = { 'errors': [] }

        # All required keys present?
        required_keys = {
            'mnemonic',
        }

        if not required_keys.issubset(set(data.keys())):
            errors['errors'].append({'error': 'mnemonic is required'})
            return jsonify(errors)

        mnemonic = data.get('mnemonic', None)

        balance = GDKWrapper.get_balance(mnemonic)
        return jsonify(balance)
    else:
        return {'error': 'Invalid or missing header Authorization token'}


@app.route('/api/v1/wallet/new-address', methods=['POST'])
def wallet_new_address():
    if can_post(request.headers):
        data = request.get_json()
        errors = { 'errors': [] }

        # TODO - make the mnemonic check into a function called from the other routes here.
        # All required keys present?
        required_keys = {
            'mnemonic',
        }

        if not required_keys.issubset(set(data.keys())):
            errors['errors'].append({'error': 'mnemonic is required'})
            return jsonify(errors)

        mnemonic = data.get('mnemonic', None)

        address = GDKWrapper.get_new_address(mnemonic)
        return jsonify(address)
    else:
        return {'error': 'Invalid or missing header Authorization token'}


app.run()
