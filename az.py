#!/usr/bin/python

from urllib.request import urlopen, URLError
from time import sleep
import re, os, logging, requests, json
from aiogram import Bot, Dispatcher, executor, types
from threading import Thread

#-----------------------------TELEGRAM BOT---------------------------------------------------------------------------------------
API_TOKEN = '6316587556:AAEb4hDUBQhsBS0lrj3jO-7PM9VPHoDVNsQ'
#user_id : 5179150440 , user name : Moh tom
#user_id : 1978300128 , user name : 369 963
user_ids = ["6300297216"]
TV_alert = ["", ""]
k='binance_acc_key'
s='binance_acc_secret'

#-----------------------------------------------------------------------------------------------------------------------------------

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

keyboard_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
btns_text = ('Start','Reboot_vps')
keyboard_markup.row(*(types.KeyboardButton(text) for text in btns_text))
btns_text = ('Close_all','TV_Hook')
keyboard_markup.row(*(types.KeyboardButton(text) for text in btns_text))

user_id = None
user_name = ''
user_name_recorded = False

@dp.message_handler(regexp='(^Start[s]?$|start|/start)')
async def send_welcome(message: types.Message):
     user_id = str(message.chat.id)
     user_name = message.from_user.full_name
     #print (user_id, user_name)
     keyboard_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
     btns_text = ('Start','Reboot_vps')
     keyboard_markup.row(*(types.KeyboardButton(text) for text in btns_text))
     btns_text = ('Close_all','TV_Hook')
     keyboard_markup.row(*(types.KeyboardButton(text) for text in btns_text))
     await message.reply(' Bot Already Started ! , Good Start ' + ' ' + user_id
     + ' ' + message.from_user.full_name, reply_markup=keyboard_markup)

@dp.message_handler(regexp='(^Close_all[s]?$|close_all|/close_all)')
async def Close_all(message: types.Message):
     close_all_open_UMFutures_market_price()
     close_all_open_CMFutures_market_price()
     await message.reply(' Close All Orders ' + message.from_user.full_name, reply_markup=keyboard_markup)

@dp.message_handler(regexp='(^Reboot_vps[s]?$|reboot_vps|/reboot_vps)')
async def Close_all(message: types.Message):
     await message.reply(' Reboot VPS ' + message.from_user.full_name, reply_markup=keyboard_markup)
     os.system('reboot')

xdone = False
@dp.message_handler(regexp='(^TV_Hook[s]?$|tv_hook|/tv_hook)')
async def tv_hook(message: types.Message):
     keyboard_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
     btns_text = ('USD_M' ,'COIN_M')
     keyboard_markup.row(*(types.KeyboardButton(text) for text in btns_text))
     await message.reply(' Use on your own responsibility, constructing TRADINGVIEW Alert  Step One \n\n' , reply_markup=keyboard_markup)

xxstr0 = ("USD_M", "COIN_M")
xxstr1 = ("LIMIT", "MARKET", "STOP", "STOP_MARKET", "TAKE_PROFIT", "TAKE_PROFIT_MARKET")
xxstr2 = ("USD", "CONTRACTS", "RISK")
xxstr3 = ("LONG", "SHORT")
TV_alert_xstr = ["", "", ""]

@dp.message_handler()
async def echo(message: types.Message):
     #print ('echo no regexp' + str())
     if message.text in xxstr0:
         TV_alert_xstr[0] = message.text
         keyboard_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
         btns_text = ("LIMIT", "MARKET")
         keyboard_markup.row(*(types.KeyboardButton(text) for text in btns_text))
         btns_text = ("STOP", "STOP_MARKET")
         keyboard_markup.row(*(types.KeyboardButton(text) for text in btns_text))
         btns_text = ("TAKE_PROFIT", "TAKE_PROFIT_MARKET")
         keyboard_markup.row(*(types.KeyboardButton(text) for text in btns_text))
         await message.reply('constructing TRADINGVIEW Alert  Step Two \n\n' , reply_markup=keyboard_markup)
     elif message.text in xxstr1:
         TV_alert_xstr[1] = message.text
         keyboard_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
         btns_text = ('USD' ,'CONTRACTS', 'RISK')
         keyboard_markup.row(*(types.KeyboardButton(text) for text in btns_text))
         await message.reply('constructing TRADINGVIEW Alert  Step Three \n\n' , reply_markup=keyboard_markup)
     elif message.text in xxstr2:
         TV_alert_xstr[2] = message.text
         keyboard_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
         btns_text = ('LONG', 'SHORT')
         keyboard_markup.row(*(types.KeyboardButton(text) for text in btns_text))
         await message.reply('constructing TRADINGVIEW Alert  Step Four \n\n' , reply_markup=keyboard_markup)
     elif message.text in xxstr3:
         xmsg = '{\n'
         xmsg = xmsg + '"passphrase":"up2youttradingbot",\n'
         xmsg = xmsg + '"type":"' + TV_alert_xstr[1] + '",\n'
         xmsg = xmsg + '"order":"{{strategy.order.action}}",\n'
         xmsg = xmsg + '"time":"{{timenow}}",\n'
         xmsg = xmsg + '"symbol":"{{ticker}}",\n'
         xmsg = xmsg + '"FuturesType":"' + TV_alert_xstr[0] +'",\n'
         xmsg = xmsg + '"s_type":"' + TV_alert_xstr[2] + '",\n'
         xmsg = xmsg + '"size":"{{strategy.order.contracts}}",\n'
         xmsg = xmsg + '"s_t":"0%",\n'
         xmsg = xmsg + '"leverage":"1",\n'
         xmsg = xmsg + '"margin":"CROSSED",\n'
         xmsg = xmsg + '"positionSide":"' + message.text + '"\n'
         xmsg = xmsg + '}'
         keyboard_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
         btns_text = ('Start','Reboot_vps')
         keyboard_markup.row(*(types.KeyboardButton(text) for text in btns_text))
         btns_text = ('Close_all','TV_Hook')
         keyboard_markup.row(*(types.KeyboardButton(text) for text in btns_text))
         await message.reply(' TRADINGVIEW web hook \n\n http://153.92.209.208/zhook/  \n\n and the TRADINGVIEW Alert is \n\n' + xmsg , reply_markup=keyboard_markup)
     else:
         xmsg = '{\n'
         xmsg = xmsg + '"passphrase":"up2youttradingbot",\n'
         xmsg = xmsg + '"type":"LIMIT , MARKET, STOP, STOP_MARKET, TAKE_PROFIT, TAKE_PROFIT_MARKET or the rest . . .",\n'
         xmsg = xmsg + '"order":"{{strategy.order.action}}",\n'
         xmsg = xmsg + '"time":"{{timenow}}",\n'
         xmsg = xmsg + '"symbol":"{{ticker}}",\n'
         xmsg = xmsg + '"FuturesType":"USD_M or COIN_M",\n'
         xmsg = xmsg + '"s_type":"usd, contracts or risk",\n'
         xmsg = xmsg + '"size":"{{strategy.order.contracts}}",\n'
         xmsg = xmsg + '"s_t":"0%",\n'
         xmsg = xmsg + '"leverage":"1",\n'
         xmsg = xmsg + '"margin":"CROSSED",\n'
         xmsg = xmsg + '"positionSide":"L, S or H"\n'
         xmsg = xmsg + '}'
         keyboard_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
         btns_text = ('Start','Reboot_vps')
         keyboard_markup.row(*(types.KeyboardButton(text) for text in btns_text))
         btns_text = ('Close_all','TV_Hook')
         keyboard_markup.row(*(types.KeyboardButton(text) for text in btns_text))
         await message.reply(' TRADINGVIEW web hook \n\n http://153.92.209.208/zhook/  \n\n and the TRADINGVIEW Alert is \n\n' + xmsg , reply_markup=keyboard_markup)    


def binance_msg_tele(**kwargs):
     message = kwargs.get('message', {})
     try:
         message = json.loads(message.decode('utf-8'))
         print (message)
     except:
         pass

     for id in user_ids:
         requests.get("https://api.telegram.org/bot" + API_TOKEN + "/sendMessage?chat_id=" + str(id) + "&text=<b><i>" + str(message) + "</i></b>&parse_mode=HTML&reply_markup=" + str(keyboard_markup))




from datetime import *
from binance.um_futures import UMFutures
from binance.cm_futures import CMFutures
from binance.lib.utils import config_logging
from binance.error import ClientError

def new_order(**kwargs):
     result = kwargs.get('result', {})

     # FuturesType USD_M or COIN_M
     _answer = Futures_Type(result["FuturesType"], result["symbol"], result["leverage"], result["margin"])
     client = _answer[0]
     instrument = _answer[1]
     #quantity
     if (result["s_type"] == "USD") or (result["s_type"] == "CONTRACTS"):
         quantity = round(float(result["size"].replace("%","")), 2)
     if (result["s_type"] == "RISK"):
         MarktPrice = client.mark_price(instrument)
         MarktPrice = float(MarktPrice["markPrice"])
         acc_balance = client.balance()
         for check_balance in acc_balance:
             if check_balance["asset"] == "USDT":
                  USDT_balance = float(check_balance["balance"])
                  quantity = float("{:.3f}".format(((USDT_balance * 0.9) / MarktPrice) * float(result["leverage"])))
                  quantity = (quantity * float(result["size"].replace("%",""))) / 100
                  change_leverage(client, instrument, result["leverage"])
                  if result["FuturesType"] == "COIN_M": change_margin_type(client, instrument, result["margin"])
                  break
             if check_balance["asset"] == "BUSD":
                  BUSD_balance = check_balance["balance"]
                  quantity = float("{:.3f}".format(((BUSD_balance * 0.9) / MarktPrice) * float(result["leverage"])))
                  quantity = (quantity * float(result["size"].replace("%",""))) / 100
                  change_leverage(client, instrument, result["leverage"])
                  if result["FuturesType"] == "COIN_M": change_margin_type(client, instrument, result["margin"])
                  break

     #print (str(quantity))

     #Get price and quantity precision (digits and decimals)
     exchInfo = client.exchange_info()
     for exchInfo_symbol in exchInfo['symbols']:
         if exchInfo_symbol['symbol'] == instrument:
              decimals = exchInfo_symbol['pricePrecision']
              digits = exchInfo_symbol['quantityPrecision']
              #print ("price and quantity precision " , decimals, digits)


     # Reduce Position
     try:
         if (result["reducePosition"].replace("%","")) != '0':
              all_open_positions = client.get_position_risk(recvWindow=6000)
              for position in all_open_positions:
                  position_quantity = float(position["positionAmt"])
                  reducePositionQty = round(position_quantity * float(reducePosition) / 100, digits)
                  if position_quantity < 0.0:
                     client.new_order(symbol=position["symbol"], side="BUY", quantity=abs(reducePositionQty), type=result["M.TYPE"], positionSide=position["positionSide"])
                     binance_msg_tele('Closed a SELL order!')
                  elif position_quantity > 0.0:
                     client.new_order(symbol=position["symbol"], side="SELL", quantity=abs(reducePositionQty), type=result["M.TYPE"], positionSide=position["positionSide"])
                     binance_msg_tele('Closed a BUY order!')
     except:
         pass




     if result["type"].upper() == "LIMIT":
         if result["positionSide"].upper() != 'H':
              msgx = limit_order(client, instrument, result["order"].upper(), result["type"].upper(), abs(round(quantity, digits)), MarktPrice, result["positionSide"].upper())
              t = Thread(target=binance_msg_tele, kwargs={'message': msgx})
              t.start()
         else:
              limit_order(client, instrument, result["order"].upper(), result["type"].upper(), abs(round(quantity, decimals)), MarktPrice, 'LONG')
              limit_order(client, instrument, result["order"].upper(), result["type"].upper(), abs(round(quantity, decimals)), MarktPrice, 'SHORT')
     elif result["type"].upper() == "MARKET":
         if result["positionSide"].upper() !='H':
              msgx = market_order(client, instrument, result["order"].upper(), result["type"].upper(), abs(round(quantity, digits)), result["positionSide"].upper())
              t = Thread(target=binance_msg_tele, kwargs={'message': msgx})
              t.start()
         else:
              market_order(client, instrument, result["order"].upper(), result["type"].upper(), abs(round(quantity, decimals)), "LONG")
              market_order(client, instrument, result["order"].upper(), result["type"].upper(), abs(round(quantity, decimals)), "SHORT")

     elif result["type"].upper() == "STOP" or result["type"].upper() == "STOP_MARKET":
         if result["positionSide"].upper() == 'LONG':
              if result["order"].upper() == "BUY": stopPrice = abs(round(MarktPrice - MarktPrice * float(result["s_t"].replace('%', '')) / 100, decimals))
              if result["order"].upper() == "SELL": stopPrice = abs(round(MarktPrice + MarktPrice * float(result["s_t"].replace('%', '')) / 100, decimals))
              stoploss_order(client, instrument, result["type"].upper(), result["order"].upper(), abs(round(quantity, decimals)), "LONG", MarktPrice, stopPrice)
         if result["positionSide"].upper() == 'SHORT':
              if result["order"].upper() == "BUY": stopPrice = abs(round(MarktPrice + MarktPrice * float(result["s_t"].replace('%', '')) / 100, decimals))
              if result["order"].upper() == "SELL": stopPrice = abs(round(MarktPrice - MarktPrice * float(result["s_t"].replace('%', '')) / 100, decimals))
              stoploss_order(client, instrument, result["type"].upper(), result["order"].upper(), abs(round(quantity, decimals)), "SHORT", MarktPrice, stopPrice)

     elif result["type"].upper() == "TAKE_PROFIT" or result["type"].upper() == "TAKE_PROFIT_MARKET":
         if result["positionSide"].upper() == 'LONG':
              if result["order"].upper() == "BUY": stopPrice = abs(round(MarktPrice + MarktPrice * float(result["s_t"].replace('%', '')) / 100, decimals))
              if result["order"].upper() == "SELL": stopPrice = abs(round(MarktPrice - MarktPrice * float(result["s_t"].replace('%', '')) / 100, decimals))
              takeProfit_order(client, instrument, result["type"].upper(), result["order"].upper(), abs(round(quantity, decimals)), "LONG", MarktPrice, stopPrice)
         if result["positionSide"].upper() == 'SHORT':
              if result["order"].upper() == "BUY": stopPrice = abs(round(MarktPrice - MarktPrice * float(result["s_t"].replace('%', '')) / 100, decimals))
              if result["order"].upper() == "SELL": stopPrice = abs(round(MarktPrice + MarktPrice * float(result["s_t"].replace('%', '')) / 100, decimals))
              takeProfit_order(client, instrument, result["type"].upper(), result["order"].upper(), abs(round(quantity, decimals)), "SHORT", MarktPrice, stopPrice)




def Futures_Type(FuturesType, symbol, leverage, marginType):
     try:
         if FuturesType == "USD_M":
              client = UMFutures(key=k, secret=s)
              instrument = symbol.replace(".P","")
              #change_leverage(client, instrument, leverage)
         elif FuturesType == "COIN_M":
              client = CMFutures(key=k, secret=s)
              instrument = symbol#.replace(".P","")
              #change_leverage(client, instrument, leverage)
              #change_margin_type(client, instrument, marginType)
         return client, instrument
     except Exception as e:
         print("Futures Type error - {}".format(e))
         #bot.error_message(symbol, quantity, str(e))

     #return client, instrument

def change_leverage(client, instrument, _leverage):
     try:
         msg=client.change_leverage(symbol=instrument, leverage=_leverage, recvWindow=59999)
     except Exception as e:
         print("change leverage error - {}".format(e))
         #bot.error_message(symbol, quantity, str(e))
         return False

     return msg

def change_margin_type(client, instrument, margin):
     try:
         msg=client.change_margin_type(symbol=instrument, marginType=margin, recvWindow=59999)
     except Exception as e:
         print("change margin type error - {}".format(e))
         #bot.error_message(symbol, quantity, str(e))
         return False

     return msg


def market_order(client, instrument, side, order_type, quantity, positionSide):
     try:
         msg=client.new_order(symbol=instrument, side=side.upper(), quantity=quantity, type=order_type.upper(), positionSide=positionSide.upper())
     except Exception as e:
         print("market order error - {}".format(e))
         #bot.error_message(symbol, quantity, str(e))
         return False

     return msg

def limit_order(client, instrument, side, order_type, quantity, price, positionSide):
     try:
         msg=client.new_order(symbol=instrument, side=side.upper(), quantity=quantity, type=order_type.upper(), timeInForce="GTC", price=price, positionSide=positionSide.upper())
     except Exception as e:
         print("limit order error - {}".format(e))
         #bot.error_message(symbol, quantity, str(e))
         return False

     return msg




def get_local_timestamp():
     return um_futures_client.time()#datetime.now().timestamp())

def close_all_open_UMFutures_market_price():
     client =UMFutures(key=k, secret=s)
     all_open_positions = client.get_position_risk(recvWindow=6000)
     for position in all_open_positions:
         position_quantity = float(position["positionAmt"])
         if position_quantity > 0.0:
              client.new_order(symbol=position["symbol"], side="SELL", quantity=abs(position_quantity), type="MARKET", positionSide=position["positionSide"])
         elif position_quantity < 0.0:
              client.new_order(symbol=position["symbol"], side="BUY", quantity=abs(position_quantity), type="MARKET", positionSide=position["positionSide"])

def close_all_open_CMFutures_market_price():
     client =CMFutures(key=k, secret=s)
     all_open_positions = client.get_position_risk(recvWindow=6000)
     for position in all_open_positions:
         position_quantity = float(position["positionAmt"])
         if position_quantity > 0.0:
              client.new_order(symbol=position["symbol"], side="SELL", quantity=abs(position_quantity), type="MARKET", positionSide=position["positionSide"])
         elif position_quantity < 0.0:
              client.new_order(symbol=position["symbol"], side="BUY", quantity=abs(position_quantity), type="MARKET", positionSide=position["positionSide"])


#-------------------------------------Main Start--------------------------------------
if __name__ == '__main__':
     t = Thread(target=binance_msg_tele, kwargs={'message': "Bot Initialized"})
     t.start()
     executor.start_polling(dp, skip_updates=True)
