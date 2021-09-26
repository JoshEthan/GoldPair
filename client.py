import config
from binance import Client


client = Client(config.api_key, config.api_secret, tld='us')