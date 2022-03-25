# flask-api-wrapper-for-gdk
A Flask based API that wraps some GDK calls so it can be used by other
languages.

## NOTE ON THIS VERSION OF THE API

The current API includes the endpoints below:

```
/api/v1/wallet/create
/api/v1/wallet/balance
/api/v1/wallet/new-address
/api/v1/wallet/transactions
/api/v1/wallet/send-to-address
/api/v1/block-height
```

There are also a few test endpoints for permissions:

```
/api/v1/example and /api/v1/example_no_auth
/api/v1/example_auth
```

You can add more endpoints by wrapping the functions in the `gdk_wallet` class
within the GDKWallet class and making those callable from the API routes
provided through `api.py`.

If the method does not exist in `gdk_wallet` class and is available through the
GDK code you will need to add it yourself first. GDK README and reference
documentation:

[https://github.com/Blockstream/gdk](https://github.com/Blockstream/gdk)

[https://gdk.readthedocs.io/en/latest/](https://gdk.readthedocs.io/en/latest/)


## Installation and dependancies

For this we'll use a virtual environment, although this is not required.

We'll specify the version of Python to use, Python 3.9 in this case as it
matches the latest GDK Python wheel. If you cannot get GDK to work with your
installed version of Python you can try installing Python version 3.9 or you
can use the `venv` folder in this repository as it has Python 3.9.1
installed.

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
https://github.com/Blockstream/gdk/releases
The 'cp' number refers to the python version you have.
For example, to install GDK on Linux with Python 3.9.*, download and pip install the .whl file:
pip install greenaddress-0.0.50-cp39-cp39-linux_x86_64.whl
GDK README and reference documentation:

[https://github.com/Blockstream/gdk](https://github.com/Blockstream/gdk)

[https://gdk.readthedocs.io/en/latest/](https://gdk.readthedocs.io/en/latest/)


```
pip install greenaddress-0.0.50-cp39-cp39-linux_x86_64.whl
pip install -r requirements.txt
```

To run:

```
python api.py
```

To check the API is running (debug mode) for our example API visit:

http://127.0.0.1:5000/api/v1/example_no_auth

Visiting the web page above makes an API call to the `api/v1/example_no_auth`
route, and returns JSON:

```
{
    'example_key': 'example_value'
}
```

The API should be callable via NodeJS etc by making http requests (GET, POST).

Permission to cal the API is protected by the API requiring an authorization
token in the request's header. Set these within `config.py` and add more
permission roles in `api.py` if nedded and include the token in `config.py`.
Only get and post permissions are included here by way of example.

## Configuration for Liquid environment

In config.py, edit the NETWORK_NAME variable's value to switch between test
(`'testnet-liquid'`) and live (`'liquid'`) Liquid networks.

## Testing

You can run the API and separately call the `tester.py` file from the command
line:

```
python tester.py
```

The test file will sign into a wallet that has already been created using its
mnemonic and:

1. Get the wallet's balance.

2. Get a new deposit address and show what data needs persisting.

3. Get some network info (block height).

4. Get incoming and outgoing transactions and flag an example deposit.

5. Send 1 sat of L-BTC to an address.

The example also shows how to create a new wallet.
