import os

class Config(object):
    # TODO: You can set environment variables before going live if needed.
    # You can set them here if you have not set them as environment variables
    # If environment variables are set they will override the values below.

    # TODO - use liquid for live Liquid network/live AMP assets
    NETWORK_NAME = os.environ.get('NETWORK_NAME') or 'testnet-liquid'

    # TODO - generate your own keys and replace the ones below!
    GET_TOKEN = os.environ.get('READ_TOKEN') or '9becbfcf-7eca-4d58-baa1-855c3034dbfe'

    # TODO - generate your own keys and replace the ones below!
    POST_TOKEN = os.environ.get('WRITE_TOKEN') or 'f056f7dd-6bab-4808-399e-cac4477148f9'

    DEBUG = os.environ.get('DEBUG') or True

    API_VERSION = os.environ.get('READ_TOKEN') or '0.1.0'
