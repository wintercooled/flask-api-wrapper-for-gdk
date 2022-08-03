# flask-api-wrapper-for-gdk

[GDK](https://github.com/Blockstream/gdk) itself cannot be compiled to run in a web browser.

This Flask API wraps GDK function calls so it can be used by other languages. By running the API you can indirectly call GDK functions from the web (e.g. JavaScript) using http requests.

A `Node.js` example showing how to make client calls to the API is provided in `example_client_nodejs.js`.

`JavaScript` examples can be created using the above as a reference. It shows how to set headers, how to call the API and how to handle responses.

A `Python` example showing how to make client calls to the API is provided in `example_client_python.py`.

GDK README and reference documentation:

[https://github.com/Blockstream/gdk](https://github.com/Blockstream/gdk)

[https://gdk.readthedocs.io/en/latest/](https://gdk.readthedocs.io/en/latest/)

## WARNING

Rememeber than you must amend the authorization tokens in config.py so nobody else
knows what they are! Then amend them in the `example_client_*` files so that they match.


## NOTE ON THIS VERSION OF THE API

The current API includes the following endpoints:

```
/api/v1/wallet/create
/api/v1/wallet/balance
/api/v1/wallet/new-address
/api/v1/wallet/transactions
/api/v1/wallet/send-to-address
/api/v1/block-height
```

You can add more endpoints by simply wrapping the functions in the `gdk_wallet` class
within the GDKWallet class and making those callable from the API routes
provided through `api.py`.

There are also a few test endpoints for permissions:

```
/api/v1/example and /api/v1/example_no_auth
/api/v1/example_auth
```

GDK README and reference documentation:

[https://github.com/Blockstream/gdk](https://github.com/Blockstream/gdk)

[https://gdk.readthedocs.io/en/latest/](https://gdk.readthedocs.io/en/latest/)


## Installation and set up

For this we'll use a virtual environment, although this is not required.

We'll specify the version of Python to use, Python 3.9 in this case, as it
matches the latest GDK Python wheel. You can build GDK to target a different
version of Python, if needed, by following the instructions [here](https://github.com/Blockstream/gdk#java-and-python-wrappers).


If you cannot get GDK to work with your installed version of Python you can try
installing Python version 3.9 or you can use the `venv` folder in this
repository as it has Python 3.9.1 already installed.

To create a new virtual environment:

```
virtualenv -p /usr/bin/python3.9 venv
source venv/bin/activate
```

Check the Python version:

```
python --version
```

Which, in our example, prints:

```
Python 3.9.10
```

To install GDK, download the GDK python wheel from:

[https://github.com/Blockstream/gdk/releases](https://github.com/Blockstream/gdk/releases)

The 'cp' number refers to the python version you have.
For example, to install GDK on Linux with Python 3.9.*, download and pip install
the .whl file:

```
pip install greenaddress-0.0.50-cp39-cp39-linux_x86_64.whl
```

To install dependancies run:

```
pip install -r requirements.txt
```

To run the API:

```
python api.py
```

To check the API is running (debug mode) for our example API visit:

[http://127.0.0.1:5000/api/v1/example_no_auth](http://127.0.0.1:5000/api/v1/example_no_auth)

Visiting the web page above makes an API call to the `api/v1/example_no_auth`
route, and returns JSON:

```
{
    'example_key': 'example_value'
}
```

The API should be callable via `Node.js` and `JavaScript` etc by making http requests (GET, POST).

Permission to call the API is protected by the API requiring an authorization
token in the request's header. Set these within `config.py`. You can add more
permission roles in `api.py` if nedded and then include the token in `config.py`.

WARNING: Remember than you must amend the authorization tokens in config.py so nobody else
knows what they are!

Only get and post permissions are included here by way of example.

## Configuration for Liquid environment

In config.py, edit the NETWORK_NAME variable's value to switch between test
(`'testnet-liquid'`) and live (`'liquid'`) Liquid networks.

## Testing

Make sure the API is running and then, from another terminal window, call the
`example_client_python.py` file from the command line:

```
python example_client_python.py
```

The test file will sign into a wallet that has already been created using its
mnemonic and:

1. Get the wallet's balance.

2. Get a new deposit address and show what data needs persisting.

3. Get some network info (block height).

4. Get incoming and outgoing transactions and flag an example deposit.

5. Send 1 sat of L-BTC to an address.

The example also shows how to create a new wallet if you do not want to use the
example one, which you probably dont. You can get testnet L-BTC and a testnet
issued asset from this [Liquid testnet faucet site](https://liquidtestnet.com/faucet)
which will help with your testing and development.

