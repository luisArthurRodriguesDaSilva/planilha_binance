from binance.enums import SYMBOL_TYPE_SPOT
from chaves import *
import pandas as pd

arq="td/planilha.json"

#def existir_em_salvas(,postado):
#    with open(arq, "r") as f:
#        salvos = json.load(f)
#    resposta = False
#    for i in range (len(salvos)):
#        #print(f"(em existir) {salvos[i]['twet']}\n(tamanho) {len(salvos)}  i:{i}")
#        if salvos[i]['twet']==postado:
#            resposta=True
#            break
#    return resposta

def salvar_operacao(par,pnl):
    with open(arq, "r") as f:
        salvos = json.load(f)

    salvos.append({par:pnl})

    with open(arq, 'w') as f:
        json.dump(salvos, f,indent=4)


def json_correto(s):
  return json.dumps(s, indent=4, sort_keys=True)

import json
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
secret_key=chavess["secretKey"]
api_key=chavess['apiKey']

bin = Client(api_key,secret_key)

prices = bin.get_all_tickers()
conta=bin.get_account_status()
trades_futuros=json_correto(bin.futures_account_trades())
dinheiro_na_conta=bin.futures_account_balance()
VC=0

for trade in bin.futures_account_trades():
  if float(trade['realizedPnl'])!=0 and trade['time']>=1648860582400:
    print(f"{trade['realizedPnl']} ---------- {trade['time']} - {(trade['symbol'])} ")
    salvar_operacao(par=(trade['symbol']),pnl=trade['realizedPnl'])
    VC+=float(trade['realizedPnl'])
    print(f"{VC}\n\n")