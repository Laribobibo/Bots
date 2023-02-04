from trading_ig.config import config
from trading_ig import IGService

ig_service = IGService("carlkong","Tintin4351" ,"3d277e6ffa060d52e9a0d4ef4aef0060b488772d")
ig = ig_service.create_session()

results = ig_service.search_markets("gold")
results

print (ig)
