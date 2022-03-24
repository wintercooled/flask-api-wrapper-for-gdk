# flask-api-wrapper-for-gdk
A Flask based API that wraps some GDK calls so it can be used by other
languages.

## NOTE ON THIS VERSION OF THE API

This exampel is currently just intended to enable the user to check they have
the environment set up correctly. If you can run the app and view the example
API then later version of this code will also work.

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
https://github.com/Blockstream/gdk
https://gdk.readthedocs.io/en/latest/

```
pip install greenaddress-0.0.50-cp39-cp39-linux_x86_64.whl
pip install -r requirements.txt
```

To run:

```
python api.py
```

API (debug mode) for our example API call is available if you visit:

http://127.0.0.1:5000/api/v1/example

Visiting the web page above makes an API call to the `api/v1/example` route,
which calls GDK and creates a new wallet and returns the GAID as JSON.

The API should be callable via NodeJS etc by making the API call.

You can protect the API by requiring an authorization token in any request's
header. A later version of this code will show how that can be done, as well
as implementing all the API calls needed to manage an AMP wallet over an API
using GDK.
