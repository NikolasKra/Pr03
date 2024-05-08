import json
import requests 
from congig import slovar
class APIException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def  get_price(quote:str, base:str,amount:str):
        

        try:
            quote_tiker = slovar[quote]
        except KeyError:
            raise APIException(f"неудалось обрабоать валюту {quote}")
        try:
            base_tiker = slovar[base]
        except KeyError:
            raise APIException(f"неудалось обрабоать валюту {base}")
        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f"неудалось обрабоать количество {amount}")
        
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_tiker}&tsyms={base_tiker}')
        total_base = json.loads(r.content)[slovar[base]]
        return total_base  