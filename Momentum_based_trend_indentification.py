Equity_last_hope.py


from datetime import datetime, timedelta
from kiteconnect import KiteConnect
from kiteconnect import KiteTicker
import pdb
import pandas as pd 
import matplotlib.pyplot as plt 
import xlwings as xw
import time
import os
import pprint
from array import*
import time
import datetime
import json
from urllib.request import urlopen
import numpy as np
from pywintypes import com_error


kite="";
api_k="";
api_s="";

def get_login(api_k,api_s):
	global kws,kite;
	kite = KiteConnect(api_key=api_k)
	print("[*] Generate access Token : ",kite.login_url())
	request_tkn = input("[*] Enter Your Request Token Here : ");
	data = kite.generate_session(request_tkn, api_secret=api_s)
	kite.set_access_token(data["access_token"])
	kws = KiteTicker(api_k, data["access_token"])


get_login(api_k,api_s);



sec = int(round(time.time()))
ab=(sec/300)

J=0
K= 0
arr_1d = []
arr_positive = []
arr_negative = []



cumul_vol_cumsum = []
vwap_cal = []


one_time={'first':''}




global trd_portfolio

			



	
def on_ticks(ws, ticks):
	
	arr_1d = []
	arr_positive = []
	arr_negative = []

	cumul_vol_cumsum = []
	vwap_cal = []



	while True:
		abc = datetime.datetime.now()
		if ((int(abc.strftime("%H"))>=9) and (((((int(abc.strftime("%M"))))==5) or (((int(abc.strftime("%M"))))==10) or (((int(abc.strftime("%M"))))==15) or (((int(abc.strftime("%M"))))==20) or (((int(abc.strftime("%M"))))==25) or (((int(abc.strftime("%M"))))==30) or (((int(abc.strftime("%M"))))==35) or (((int(abc.strftime("%M"))))==40) or (((int(abc.strftime("%M"))))==45) or (((int(abc.strftime("%M"))))==50) or (((int(abc.strftime("%M"))))==55) or (((int(abc.strftime("%M"))))==00)))) :
		
		
		#if int(abc.strftime("%H"))>=9 :
			if ("time" not in one_time.values())==True:
				one_time['first']="time"
			#	time.sleep(900)
				print("yo")
			

			time.sleep(4)
			global trd_portfolio
			
			trd_portfolio={

				'HDFC':{'token':340481,'name':'HDFC','status':'','order_buy_SLM':'','order_buy_LIMIT':'','order_sell_SLM':'','order_sell_LIMIT':'','BACKTEST':'','first':'','skipping':''},				

				'M&M':{'token':519937,'name':'M&M','status':'','order_buy_SLM':'','order_buy_LIMIT':'','order_sell_SLM':'','order_sell_LIMIT':'','BACKTEST':'','first':'','skipping':''},				

				'RELIANCE':{'token':738561,'name':'RELIANCE','status':'','order_buy_SLM':'','order_buy_LIMIT':'','order_sell_SLM':'','order_sell_LIMIT':'','BACKTEST':'','first':'','skipping':''},				
				
			#	'AXISBANK':{'token':1510401,'name':'AXISBANK','status':'','order_buy_SLM':'','order_buy_LIMIT':'','order_sell_SLM':'','order_sell_LIMIT':'','BACKTEST':'','first':'','skipping':''},				

				'HINDUNILVR':{'token':356865,'name':'HINDUNILVR','status':'','order_buy_SLM':'','order_buy_LIMIT':'','order_sell_SLM':'','order_sell_LIMIT':'','BACKTEST':'','first':'','skipping':''},				

				'BAJFINANCE':{'token':81153,'name':'BAJFINANCE','status':'','order_buy_SLM':'','order_buy_LIMIT':'','order_sell_SLM':'','order_sell_LIMIT':'','BACKTEST':'','first':'','skipping':''},				

			#	'TCS':{'token':2953217,'name':'TCS','status':'','order_buy_SLM':'','order_buy_LIMIT':'','order_sell_SLM':'','order_sell_LIMIT':'','BACKTEST':'','first':'','skipping':''},				

				'MARUTI':{'token':2815745,'name':'MARUTI','status':'','order_buy_SLM':'','order_buy_LIMIT':'','order_sell_SLM':'','order_sell_LIMIT':'','BACKTEST':'','first':'','skipping':''},				

				'LT':{'token':2939649,'name':'LT','status':'','order_buy_SLM':'','order_buy_LIMIT':'','order_sell_SLM':'','order_sell_LIMIT':'','BACKTEST':'','first':'','skipping':''},				

				'BAJAJ-AUTO':{'token':4267265,'name':'BAJAJ-AUTO','status':'','order_buy_SLM':'','order_buy_LIMIT':'','order_sell_SLM':'','order_sell_LIMIT':'','BACKTEST':'','first':'','skipping':''},				

				'TORNTPHARM':{'token':900609,'name':'TORNTPHARM','status':'','order_buy_SLM':'','order_buy_LIMIT':'','order_sell_SLM':'','order_sell_LIMIT':'','BACKTEST':'','first':'','skipping':''},				

				'COLPAL':{'token':128212484,'name':'COLPAL','status':'','order_buy_SLM':'','order_buy_LIMIT':'','order_sell_SLM':'','order_sell_LIMIT':'','BACKTEST':'','first':'','skipping':''},				

				'DABUR':{'token':197633,'name':'DABUR','status':'','order_buy_SLM':'','order_buy_LIMIT':'','order_sell_SLM':'','order_sell_LIMIT':'','BACKTEST':'','first':'','skipping':''},				

				'SUNPHARMA':{'token':857857,'name':'SUNPHARMA','status':'','order_buy_SLM':'','order_buy_LIMIT':'','order_sell_SLM':'','order_sell_LIMIT':'','BACKTEST':'','first':'','skipping':''},				

				'AUROPHARMA':{'token':70401,'name':'AUROPHARMA','status':'','order_buy_SLM':'','order_buy_LIMIT':'','order_sell_SLM':'','order_sell_LIMIT':'','BACKTEST':'','first':'','skipping':''},				

				'DMART':{'token':5097729,'name':'DMART','status':'','order_buy_SLM':'','order_buy_LIMIT':'','order_sell_SLM':'','order_sell_LIMIT':'','BACKTEST':'','first':'','skipping':''},				

				}
	#		for company_data in ticks:	
			


			for name in trd_portfolio.copy():				
			
				token = int(trd_portfolio[name]['token'])
				name = str(trd_portfolio[name]['name'])
							
				print("NAME OF THE STOCK__________________",name)			
				from_date1='2020-05-25'
				to_date1= datetime.datetime.now()	
				interval1="day"
				records_pivot = kite.historical_data(token, from_date1, to_date1, interval1)
				df1 = pd.DataFrame(records_pivot)
				date1=pd.to_datetime(df1['date'])				
			#####				
			#print("ckhskjdsskjvbbsvhhguuebufjegbsihfahfbfgbajhfsdbfjbsjjfhaekjdbkncjskddjcbjnkcdkjkbkjdkdbcckddjcjbcdkcdc")				
			######				
				from_date2='2020-05-25'
				to_date2=datetime.datetime.now()	
				interval2="5minute"
				records = kite.historical_data(token, from_date2, to_date2, interval2)
				df = pd.DataFrame(records)
				date2=pd.to_datetime(df['date'])					
				
		
				from_date3='2020-05-25'				
				to_date3=datetime.datetime.now()	
				interval3="15minute"
				records3 = kite.historical_data(token, from_date3, to_date3, interval3)
				df3 = pd.DataFrame(records3)
				date3=pd.to_datetime(df3['date'])




				
				high1 = df1['high'].iloc[-2]
				low1 = df1['low'].iloc[-2]
				close1 = df1['close'].iloc[-2]	
								
						
				###########################					
				df['9_period_high']=df['high'].rolling(9).max()	 # PRE-REQUISIT CALCULATIONS
				df['9_period_low']=df['low'].rolling(9).min()	# PRE-REQUISIT CALCULATIONS
								
				df['26_period_high']=df['high'].rolling(26).max()	# PRE-REQUISIT CALCULATIONS
				df['26_period_low']=df['low'].rolling(26).min()	# PRE-REQUISIT CALCULATIONS
								
				df['52_period_high(present)']=df['high'].rolling(52).max()	# PRE-REQUISIT CALCULATIONS
				df['52_period_low(present)']=df['low'].rolling(52).min()	# PRE-REQUISIT CALCULATIONS
								
				df['kijun'] =((df['26_period_high']+df['26_period_low'])/2)	 # PRE-REQUISIT CALCULATIONS
				df['tenken'] =((df['9_period_high']+df['9_period_low'])/2)		# PRE-REQUISIT CALCULATIONS
									
				# 52 period high					
				n = 26
				df['(78-26)_period_high']=df['high'].rolling(78).max()  # PRE-REQUISIT CALCULATIONS
				df['52_period_high_future'] = df['(78-26)_period_high'][n:]	# PRE-REQUISIT CALCULATIONS				
				# 52 period low
				n = 26
				df['(78-26)_period_low']=df['low'].rolling(78).min()   # PRE-REQUISIT CALCULATIONS
				df['52_period_low_future']=df['(78-26)_period_low'][n:]	 # PRE-REQUISIT CALCULATIONS
				
								
				#26 peiod high
				n=26
				df['(52-26)_period_high']=df['high'].rolling(52).max() # PRE-REQUISIT CALCULATIONS
				df['26_period_high_future']=df['(52-26)_period_high'][n:]	 # PRE-REQUISIT CALCULATIONS				
				# 26 period low
				n=26
				df['(52-26)_period_low']=df['low'].rolling(52).min() # PRE-REQUISIT CALCULATIONS
				df['26_period_low_future']=df['(52-26)_period_low'][n:]	 # PRE-REQUISIT CALCULATIONS
				
								
				# 9 period high
				n=26
				df['(35-26)_period_high']=df['high'].rolling(35).max() # PRE-REQUISIT CALCULATIONS
				df['9_period_high_future']=df['(35-26)_period_high'][n:]	 # PRE-REQUISIT CALCULATIONS
								
				# 9 period low
				n=26
				df['(35-26)_period_low']=df['low'].rolling(35).min() # PRE-REQUISIT CALCULATIONS
				df['9_period_low_future']=df['(35-26)_period_low'][n:]	 # PRE-REQUISIT CALCULATIONS
								
				df['furure_kijun']= ((df['(52-26)_period_high']+df['(52-26)_period_low'])/2)	# PRE-REQUISIT CALCULATIONS
				df['future_tenken']= ((df['(35-26)_period_high']+df['(35-26)_period_low'])/2)	# PRE-REQUISIT CALCULATIONS
								
				df['present_span_a'] = ((df['furure_kijun']+ df['future_tenken'])/2)	# REQUIRED
				df['present_span_b'] =((df['52_period_high(present)'] + df['52_period_low(present)'])/2)	# REQUIRED
								
				df['future_span_a'] =((df['kijun']+ df['tenken'])/2)	  # REQUIRED
				df['future_span_b'] =((df['52_period_high_future'] + df['52_period_low_future'])/2)	# REQUIRED	










				df3['9_period_high']=df3['high'].rolling(9).max()	 # PRE-REQUISIT CALCULATIONS
				df3['9_period_low']=df3['low'].rolling(9).min()	# PRE-REQUISIT CALCULATIONS
					
				df3['26_period_high']=df3['high'].rolling(26).max()	# PRE-REQUISIT CALCULATIONS
				df3['26_period_low']=df3['low'].rolling(26).min()	# PRE-REQUISIT CALCULATIONS
					
				df3['52_period_high(present)']=df3['high'].rolling(52).max()	# PRE-REQUISIT CALCULATIONS
				df3['52_period_low(present)']=df3['low'].rolling(52).min()	# PRE-REQUISIT CALCULATIONS
					
				df3['kijun'] =((df3['26_period_high']+df3['26_period_low'])/2)	 # PRE-REQUISIT CALCULATIONS
				df3['tenken'] =((df3['9_period_high']+df3['9_period_low'])/2)		# PRE-REQUISIT CALCULATIONS
						
				# 52 period high		
				n = 26
				df3['(78-26)_period_high']=df3['high'].rolling(78).max()  # PRE-REQUISIT CALCULATIONS
				df3['52_period_high_future'] = df3['(78-26)_period_high'][n:]	# PRE-REQUISIT CALCULATIONS	
				# 52 period low
				n = 26
				df3['(78-26)_period_low']=df3['low'].rolling(78).min()   # PRE-REQUISIT CALCULATIONS
				df3['52_period_low_future']=df3['(78-26)_period_low'][n:]	 # PRE-REQUISIT CALCULATIONS
				
					
				#26 peiod high
				n=26
				df3['(52-26)_period_high']=df3['high'].rolling(52).max() # PRE-REQUISIT CALCULATIONS
				df3['26_period_high_future']=df3['(52-26)_period_high'][n:]	 # PRE-REQUISIT CALCULATIONS	
				# 26 period low
				n=26
				df3['(52-26)_period_low']=df3['low'].rolling(52).min() # PRE-REQUISIT CALCULATIONS
				df3['26_period_low_future']=df3['(52-26)_period_low'][n:]	 # PRE-REQUISIT CALCULATIONS
				
					
				# 9 period high
				n=26
				df3['(35-26)_period_high']=df3['high'].rolling(35).max() # PRE-REQUISIT CALCULATIONS
				df3['9_period_high_future']=df3['(35-26)_period_high'][n:]	 # PRE-REQUISIT CALCULATIONS
					
				# 9 period low
				n=26
				df3['(35-26)_period_low']=df3['low'].rolling(35).min() # PRE-REQUISIT CALCULATIONS
				df3['9_period_low_future']=df3['(35-26)_period_low'][n:]	 # PRE-REQUISIT CALCULATIONS
					
				df3['furure_kijun']= ((df3['(52-26)_period_high']+df3['(52-26)_period_low'])/2)	# PRE-REQUISIT CALCULATIONS
				df3['future_tenken']= ((df3['(35-26)_period_high']+df3['(35-26)_period_low'])/2)	# PRE-REQUISIT CALCULATIONS
					
				df3['present_span_a'] = ((df3['furure_kijun']+ df3['future_tenken'])/2)	# REQUIRED
				df3['present_span_b'] =((df3['52_period_high(present)'] + df3['52_period_low(present)'])/2)	# REQUIRED
					
				df3['future_span_a'] =((df3['kijun']+ df3['tenken'])/2)	  # REQUIRED
				df3['future_span_b'] =((df3['52_period_high_future'] + df3['52_period_low_future'])/2)	# REQUIRED	







			
			

				df['volume_100_period'] = df['volume'].rolling(100).mean()			
			
			

				period1 = 100
				alpha=False			

				con = pd.concat([df[:period1]['close'].rolling(window=period1).mean(), df[period1:]['close']])			

				if (alpha == True):
					# (1 - alpha) * previous_val + alpha * current_val where alpha = 1 / period
					df['EMA_100'] = con.ewm(alpha=1 / period1, adjust=False).mean()
				else:
					# ((current_val - previous_val) * coeff) + previous_val where coeff = 2 / (period + 1)
					df['EMA_100'] = con.ewm(span=period1, adjust=False).mean()
				
				df['EMA_100'].fillna(0, inplace=True)			
			
			
			
			
			

				period = 50
				alpha=False			

				con = pd.concat([df[:period]['close'].rolling(window=period).mean(), df[period:]['close']])			

				if (alpha == True):
					# (1 - alpha) * previous_val + alpha * current_val where alpha = 1 / period
					df['EMA_50'] = con.ewm(alpha=1 / period, adjust=False).mean()
				else:
					# ((current_val - previous_val) * coeff) + previous_val where coeff = 2 / (period + 1)
					df['EMA_50'] = con.ewm(span=period, adjust=False).mean()
				
				df['EMA_50'].fillna(0, inplace=True)			
			
			
			

				period2 = 150
				alpha=False			

				con = pd.concat([df[:period2]['close'].rolling(window=period2).mean(), df[period2:]['close']])			

				if (alpha == True):
					# (1 - alpha) * previous_val + alpha * current_val where alpha = 1 / period
					df['EMA_150'] = con.ewm(alpha=1 / period2, adjust=False).mean()
				else:
					# ((current_val - previous_val) * coeff) + previous_val where coeff = 2 / (period + 1)
					df['EMA_150'] = con.ewm(span=period2, adjust=False).mean()
				
				df['EMA_150'].fillna(0, inplace=True)			
			
			
			
			
			
			
			

				df['9_period_high']=df['high'].rolling(9).max()
				df['9_period_low']=df['low'].rolling(9).min()			
				

				xx = 0
				px = 1
				w = 0

				while (w) <=  len(df):

					if df['date'].iloc[w].date() == df1['date'].iloc[-1].date() :#
						xx = xx + 1#

					
						typica_sum = (df['high'].iloc[w] + df['low'].iloc[w] + df['close'].iloc[w])/ 3  
						typica_sum_vol = ( (typica_sum)*(df['volume'].iloc[w]) )					

						vwap_cal.append(typica_sum_vol)					

						typical_cumsum = np.cumsum(vwap_cal)			
					
								

						cumul_vol = df['volume'].iloc[w]					

						cumul_vol_cumsum.append(cumul_vol)					

						vol_cumsum = np.cumsum(cumul_vol_cumsum)					

						vwap = typical_cumsum/vol_cumsum

						
						if  (df['date'].iloc[w].time() ==  df['date'].iloc[-1].time() ):
							break

						print(df['date'].iloc[w])



					w = w + 1
							############
			# previous candel open, close
				open_perv_T = df['open'].iloc[-3]
				close_perv_T = df['close'].iloc[-3]					
			# candles
				open_perv=float(open_perv_T)
				close_perv=float(close_perv_T)				
				previous_candel = open_perv-close_perv				
				previous_candel_a =(previous_candel)**2
				previous_candel_length =(previous_candel_a)**0.5	 # Mod of length	
			
						
			# current candel open, close
				
				close_T =df['close'].iloc[-2]	
				open_T  =  df['open'].iloc[-2]
				open=float(open_T)
				close=float(close_T)
				
				current_candel= open-close				
			# comparing body length of both candel
				current_candel_a =(current_candel)**2
				current_candel_length =(current_candel_a)**0.5	 # Mod of length	
		
				current_candel_length_percentage = (current_candel_length/close)*100


			#### to check pivot range   ###
				open_for_pivot_a=open*100
				open_for_pivot=int(open_for_pivot_a)				
				close_for_pivot_a=close*100
				close_for_pivot=int(close_for_pivot_a)
			#############		
			
		#		pdb.set_trace()	
			###############
				# BUY
				if ("bought" not in trd_portfolio[name].values())==True:
				
					if (df['volume'].iloc[-2] > df['volume_100_period'].iloc[-2]) and (close >vwap[-1]): 
				
						if (close>df['present_span_b'].iloc[-2-26]) and (df['date'].iloc[-1].time() != df['date'].iloc[69].time()) and (df['date'].iloc[-1].time() != df['date'].iloc[70].time() and (df['date'].iloc[-1].time() != df['date'].iloc[71].time()) and (df['date'].iloc[-1].time() != df['date'].iloc[72].time()) and (df['date'].iloc[-1].time() != df['date'].iloc[73].time()) and (df['date'].iloc[-1].time() != df['date'].iloc[74].time())): #ABOVE CLOUD
				
							if close>df['future_span_a'].iloc[-2-26]: #ABOVE CLOUD						
				
								if df['present_span_b'].iloc[-2]<df['future_span_a'].iloc[-2]: #FUTURE SPAN GREEN
				
									if (df3['close'].iloc[-2] > df3['present_span_b'].iloc[-2-26]) and (df3['close'].iloc[-2]  > df3['future_span_a'].iloc[-2-26]) :
				
										if (close > df['kijun'].iloc[-2]) and (close > df['close'].iloc[-2-26]) :
				
											if (close > df['tenken'].iloc[-2]) and (df['close'].iloc[-2] > df['9_period_high'].iloc[-2-1])  :	

												if  (close > df['EMA_150'].iloc[-2] ) and   (close > df['EMA_100'].iloc[-2] ) and  (close > df['EMA_50'].iloc[-2] ) and ( df['EMA_50'].iloc[-2]  >  df['EMA_100'].iloc[-2] > df['EMA_150'].iloc[-2]) :
											
													
													print("NAME OF THE STOCK__________________",name)
													print(df['date'].iloc[-2])
													print("BUY")


													print("breakout")
													trade_initiation_ltp = close

													stoploss_buy_a = vwap[-1]
													print("stoploss_buy:", stoploss_buy_a)
														
													Target_buy_a =  trade_initiation_ltp +  2*(trade_initiation_ltp - stoploss_buy_a)	
													print("Target_buy:", Target_buy_a)



													i= int( (stoploss_buy_a)*100 )  # for converting into least count
													
													while (i/5) != int(i/5):
														i = i-1							
													
													stoploss_buy = i/100


												
													o = int( (Target_buy_a)*100 )  # for converting into least count
													
													while (o/5) != int(o/5):
														o = o-1							
													
													Target_buy = o/100






													with urlopen("https://api.kite.trade/margins/equity") as response:
														source = response.read()														

													data = json.loads(source)														

													# print(json.dumps(data, indent=2))																										

													for item in data:
														name_margin = item['tradingsymbol']
														mis_multiplier = item['mis_multiplier']	
														
														if name == name_margin:
															mis_leverage = mis_multiplier
															stock_name_of_leverage = name_margin		

															break

													qnt = 200/(trade_initiation_ltp - stoploss_buy)

													fund_balance = kite.margins()['equity']['net']
													print( kite.margins()['equity']['net'])
													print(stock_name_of_leverage,mis_leverage)

													while (qnt)*(trade_initiation_ltp/mis_leverage) > fund_balance :

														qnt =  qnt-1



											

														
													trd_portfolio[name]['status']="bought"    # for checking condition
														
													trd_portfolio[name]['order_buy_SLM']="not_exicuted_buy_SLM" # for removing  slm trade
													
													trd_portfolio[name]['order_buy_LIMIT']="not_exicuted_buy_LIMIT"	# for removing limit trade
													
													trd_portfolio[name]['BACKTEST']="order_triggered_buy" # for aknowlwging that trade is intiated	

													trd_portfolio[name]['skipping'] = "yes_one_time"	
													

													qnt_place = int(qnt-1)
													qnt_place = 1

													order_id_main_buy = kite.place_order(tradingsymbol=name,  # MAIN ORDER
														variety=kite.VARIETY_REGULAR,
														exchange=kite.EXCHANGE_NSE,
														transaction_type=kite.TRANSACTION_TYPE_BUY,
														quantity=qnt_place,
														order_type=kite.ORDER_TYPE_MARKET,
														product=kite.PRODUCT_MIS)
													print("111111111111111")
		
												
													order_id_stoploss_buy = kite.place_order(tradingsymbol=name,    # STOPLOSS
															variety=kite.VARIETY_REGULAR,
															exchange=kite.EXCHANGE_NSE,
															trigger_price=stoploss_buy-0.1,
															transaction_type=kite.TRANSACTION_TYPE_SELL,
															quantity=qnt_place,
															order_type=kite.ORDER_TYPE_SLM,
															product=kite.PRODUCT_MIS)
													print("22222222222222222")


													order_id_target_buy = kite.place_order(tradingsymbol=name,  # TAKE PROFIT
															variety=kite.VARIETY_REGULAR,
															exchange=kite.EXCHANGE_NSE,
															price=Target_buy,
															transaction_type=kite.TRANSACTION_TYPE_SELL,
															quantity=qnt_place,
															order_type=kite.ORDER_TYPE_LIMIT,
															product=kite.PRODUCT_MIS)
													print("AMANDEEP_1")

													trd_portfolio[name]['order_id_main_buy'] = order_id_main_buy
													trd_portfolio[name]['order_id_stoploss_buy'] = order_id_stoploss_buy
													trd_portfolio[name]['order_id_target_buy'] = order_id_target_buy


										



				
				if df['date'].iloc[-1].time() == df['date'].iloc[69].time() :       #square off at 15:00
				
					if ("order_triggered_buy" in trd_portfolio[name].values())==True:	

						order_id_main_buy = trd_portfolio[name]['order_id_main_buy'] 
						order_id_stoploss_buy = trd_portfolio[name]['order_id_stoploss_buy'] 
						order_id_target_buy = trd_portfolio[name]['order_id_target_buy'] 
						print("AMANDEEP_2")



						cancel_order(variety=kite.VARIETY_REGULAR ,
									 order_id = order_id_main_buy)

						cancel_order(variety=kite.VARIETY_REGULAR ,
									 order_id = order_id_stoploss_buy)

						cancel_order(variety=kite.VARIETY_REGULAR ,
									 order_id = order_id_target_buy)


						trd_portfolio[name]['status']="not_bought"    # for checking condition
											
						trd_portfolio[name]['order_buy_SLM']="exicuted_buy_SLM" # for removing  slm trade
											
						trd_portfolio[name]['order_buy_LIMIT']="exicuted_buy_LIMIT"	# for removing limit trade
											
						trd_portfolio[name]['BACKTEST']="order_not_triggered_buy" # for aknowlwging that trade is intiated	

						print("AMANDEEP_3")	

		#		#		

			

				if ("order_triggered_buy" in trd_portfolio[name].values())==True:	

					if ("no" in trd_portfolio[name].values())==True:

						order_id_stoploss_buy = trd_portfolio[name]['order_id_stoploss_buy'] 
						order_id_target_buy = trd_portfolio[name]['order_id_target_buy']

					#	print("ff")
				#		print("just checking that is the reduction problem reaching here")

			#			if int(Date.strftime("%H"))!=15 :
					
						if (df['low'].iloc[-2])<=(stoploss_buy):   # AGAR AKK BARR BHI CLOSE KIJUN SA NICHE AYA TO MODIFY ORDER RUN NAHI HOGA

							print("AMANDEEP_4")
		
							print("stoploss hitted")
							
							cancel_order(variety=kite.VARIETY_REGULAR ,
										 order_id = order_id_target_buy)
						
							print("AMANDEEP_5")
							
							trd_portfolio[name]['order_buy_LIMIT']="exicuted_buy_LIMIT"
							trd_portfolio[name]['status']="not_bought"				# CLOSING CONDITIONS LAGA DENA ACCORDINGLY		
							trd_portfolio[name]['BACKTEST']="order_not_triggered_buy"	#

					

						if (df['high'].iloc[-2])>=(Target_buy):                             # AGAR stoploss_buy HIT HOGAYA TO Target_buy WALA CANCEL HO JAYEGA  BUT CODE SAHI KARNA PADEGA VARNA ORDER LAGTA HI CANCEL HO JAYEGA
						#	print("here toooooo")
							print("AMANDEEP_6")



							cancel_order(variety=kite.VARIETY_REGULAR ,
										 order_id = order_id_stoploss_buy)
				
							trd_portfolio[name]['order_buy_SLM']="exicuted_buy_SLM"     		
							trd_portfolio[name]['status']="not_bought"								
							trd_portfolio[name]['BACKTEST']="order_not_triggered_buy"#							

							print("target hitted")

				# SELL
			#	if hh<50 and ff >= 50:
				if ("bought" not in trd_portfolio[name].values())==True:
				
					if (df['volume'].iloc[-2] > df['volume_100_period'].iloc[-2]) and (close < vwap[-1]): 
				
						if (close < df['present_span_b'].iloc[-2-26]) and (df['date'].iloc[-1].time() != df['date'].iloc[69].time()) and (df['date'].iloc[-1].time() != df['date'].iloc[70].time() and (df['date'].iloc[-1].time() != df['date'].iloc[71].time()) and (df['date'].iloc[-1].time() != df['date'].iloc[72].time()) and (df['date'].iloc[-1].time() != df['date'].iloc[73].time()) and (df['date'].iloc[-1].time() != df['date'].iloc[74].time())): #ABOVE CLOUD
				
							if close < df['future_span_a'].iloc[-2-26]: #ABOVE CLOUD						
				
								if df['present_span_b'].iloc[-2] > df['future_span_a'].iloc[-2]: #FUTURE SPAN GREEN
				
									if (df3['close'].iloc[-2]  < df3['present_span_b'].iloc[-2-26]) and (df3['close'].iloc[-2]  < df3['future_span_a'].iloc[-2-26]) :
				
										if (close < df['kijun'].iloc[-2]) and (close < df['close'].iloc[-2-26]) :
				
											if (close < df['tenken'].iloc[-2]) and (df['close'].iloc[-2] < df['9_period_low'].iloc[-2-1])  :	

												if  (close < df['EMA_150'].iloc[-2] ) and   (close < df['EMA_100'].iloc[-2] ) and  (close < df['EMA_50'].iloc[-2] ) and ( df['EMA_50'].iloc[-2]  <  df['EMA_100'].iloc[-2] < df['EMA_150'].iloc[-2]) :
													
													print('Sell')
													print("date",df['date'].iloc[-2])				

											
													print("NAME OF THE STOCK__________________",name)

													trade_initiation_ltp = close


													stoploss_sell_a = vwap[-1]
													print("stoploss_sell:", stoploss_sell_a)														
													

													Target_sell_a =  trade_initiation_ltp -  2*( stoploss_sell_a - trade_initiation_ltp)	   # retriving value of pivot in least counr
													print("Target_sell:", Target_sell_a)



													print("AMANDEEP_7")



													i= int( (stoploss_sell_a)*100 )  # for converting into least count
													
													while (i/5) != int(i/5):
														i = i+1							
													
													stoploss_sell = i/100


												
													o = int( (Target_sell_a)*100 )  # for converting into least count
													
													while (o/5) != int(o/5):
														o = o+1							
													
													Target_sell = o/100









													with urlopen("https://api.kite.trade/margins/equity") as response:
														source = response.read()														

													data = json.loads(source)														

													# print(json.dumps(data, indent=2))																										

													for item in data:
														name_margin = item['tradingsymbol']
														mis_multiplier = item['mis_multiplier']	
														
														if name == name_margin:
															mis_leverage = mis_multiplier
															stock_name_of_leverage = name_margin		

															break

													qnt = 200/( stoploss_sell - trade_initiation_ltp)

													fund_balance = kite.margins()['equity']['net']

													while (qnt)*(trade_initiation_ltp/mis_leverage) > fund_balance :

														qnt =  qnt-1

													qnt = 1

													trd_portfolio[name]['skipping'] = "yes_one_time"	
												
													trd_portfolio[name]['status']="bought"    # for checking condition
												
													trd_portfolio[name]['order_sell_SLM']="not_exicuted_sell_SLM" # for removing  slm trade
													
													trd_portfolio[name]['order_sell_LIMIT']="not_exicuted_sell_LIMIT"	# for removing limit trade
													
													trd_portfolio[name]['BACKTEST']="order_triggered_sell" # for aknowlwging that trade is intiated

													qnt_place = int(qnt-1)
													qnt_place = 1
														
													order_id_main_sell = kite.place_order(tradingsymbol=name,  # MAIN ORDER
															variety=kite.VARIETY_REGULAR,
															exchange=kite.EXCHANGE_NSE,
															transaction_type=kite.TRANSACTION_TYPE_SELL,
															quantity=qnt_place,
															order_type=kite.ORDER_TYPE_MARKET,
															product=kite.PRODUCT_MIS)
													print("66666666666666")
		
												
													order_id_stoploss_sell = kite.place_order(tradingsymbol=name,    # STOPLOSS
																variety=kite.VARIETY_REGULAR,
																exchange=kite.EXCHANGE_NSE,
																trigger_price=stoploss_sell+0.1,
																transaction_type=kite.TRANSACTION_TYPE_BUY,
																quantity=qnt_place,
																order_type=kite.ORDER_TYPE_SLM,
																product=kite.PRODUCT_MIS)
													print("7777777777777")


													order_id_target_sell = kite.place_order(tradingsymbol=name,  # TAKE PROFIT
																variety=kite.VARIETY_REGULAR,
																exchange=kite.EXCHANGE_NSE,
																price=Target_sell,
																transaction_type=kite.TRANSACTION_TYPE_BUY,
																quantity=qnt_place,
																order_type=kite.ORDER_TYPE_LIMIT,
																product=kite.PRODUCT_MIS)
													print("AMANDEEP_8")


													trd_portfolio[name]['order_id_main_sell'] = order_id_main_sell
													trd_portfolio[name]['order_id_stoploss_sell'] = order_id_stoploss_sell
													trd_portfolio[name]['order_id_target_sell'] = order_id_target_sell







				if df['date'].iloc[-1].time() == df['date'].iloc[69].time() : 
				#	print(df['date'].iloc[K])		

					if ("order_triggered_sell" in trd_portfolio[name].values())==True:	

						order_id_main_sell = trd_portfolio[name]['order_id_main_sell'] 
						order_id_stoploss_sell = trd_portfolio[name]['order_id_stoploss_sell'] 
						order_id_target_sell = trd_portfolio[name]['order_id_target_sell'] 
						print("AMANDEEP_9")





						cancel_order(variety=kite.VARIETY_REGULAR ,
									 order_id = order_id_main_sell)

						cancel_order(variety=kite.VARIETY_REGULAR ,
									 order_id = order_id_stoploss_sell)

						cancel_order(variety=kite.VARIETY_REGULAR ,
									 order_id = order_id_target_sell)





						trd_portfolio[name]['status']="not_bought"    # for checking condition
											
						trd_portfolio[name]['order_sell_SLM']="exicuted_sell_SLM" # for removing  slm trade
											
						trd_portfolio[name]['order_sell_LIMIT']="exicuted_sell_LIMIT"	# for removing limit trade
											
						trd_portfolio[name]['BACKTEST']="order_not_triggered_sell" # for aknowlwging that trade is intiated	
						print("AMANDEEP_10")	
		

				if ("order_triggered_sell" in trd_portfolio[name].values())==True:	
					if ("no" in trd_portfolio[name].values())==True:	

						order_id_stoploss_sell = trd_portfolio[name]['order_id_stoploss_sell'] 
						order_id_target_sell = trd_portfolio[name]['order_id_target_sell'] 
				
						if (df['high'].iloc[-2])>=(stoploss_sell):   # AGAR AKK BARR BHI CLOSE KIJUN SA NICHE AYA TO MODIFY ORDER RUN NAHI HOGA

							print("AMANDEEP_11")	#
				
							cancel_order(variety=kite.VARIETY_REGULAR ,
										order_id = order_id_target_sell)	
						
							print("AMANDEEP_12")		

							trd_portfolio[name]['order_sell_LIMIT']="exicuted_sell_LIMIT"
							trd_portfolio[name]['status']="not_bought"				# CLOSING CONDITIONS LAGA DENA ACCORDINGLY		
							trd_portfolio[name]['BACKTEST']="order_not_triggered_sell"					


						if (df['low'].iloc[-2])<=(Target_sell):  
							print("AMANDEEP_13")                           # AGAR stoploss_buy HIT HOGAYA TO Target_buy WALA CANCEL HO JAYEGA  BUT CODE SAHI KARNA PADEGA VARNA ORDER LAGTA HI CANCEL HO JAYEGA
					#		print("here toooooo")
							

				
							print("target hitted")
							
							cancel_order(variety=kite.VARIETY_REGULAR ,
									 	order_id = order_id_stoploss_sell)

						
							trd_portfolio[name]['order_sell_SLM']="exicuted_sell_SLM"     		
							trd_portfolio[name]['status']="not_bought"			# CLOSING CONDITIONS LAGA DENA ACCORDINGLY						
							trd_portfolio[name]['BACKTEST']="order_not_triggered_sell"#							


							print("AMANDEEP_14")

			###############				
				arr_1d = []
				arr_positive = []
				arr_negative = []


				cumul_vol_cumsum = []
				vwap_cal = []


				trd_portfolio[name]['skipping'] = "no"
				
	

def on_connect(ws, response):
	ws.subscribe([6401,3861249,325121,60417,1510401,1195009,2714625,134657,
		2029825,2763265,175361,177665,5215745,3771393,173057,1207553,315393,
		1850625,340481,341249,128112644,359937,7712001,1346049,7458561,408065,
		415745,424961,3001089,2939649,519937,4879617,2977281,633601,2730497,
		3834113,738561,779521,1102337,857857,884737,3465729,897537,2170625,
		2889473,784129,969473,975873])
	

	ws.set_mode(ws.MODE_FULL,[6401,3861249,325121,60417,1510401,1195009,2714625,134657,
		2029825,2763265,175361,177665,5215745,3771393,173057,1207553,315393,
		1850625,340481,341249,128112644,359937,7712001,1346049,7458561,408065,
		415745,424961,3001089,2939649,519937,4879617,2977281,633601,2730497,
		3834113,738561,779521,1102337,857857,884737,3465729,897537,2170625,
		2889473,784129,969473,975873])
	


kws.on_ticks = on_ticks
kws.on_connect = on_connect
kws.connect()	



#print("\n")#
#

#date1a = datetime.datetime(date1)
#date2a = datetime.datetime(date2)#

#if date2a == date1a:
#	print("they are equal now",date)
