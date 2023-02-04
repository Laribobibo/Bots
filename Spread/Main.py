'''
Prob 1 : Blankning ifall vi ej har råd.

prob 2 : ifall ci ej har råd med en aktie, skall den fortsätta springa

prob 3 : spara volym

prob 4 : Lös ticker för ava att känna av
'''
import hashlib
import time
import json
import pyotp
from avanza import Avanza, OrderType, TimePeriod
import datetime
from datetime import date
import yfinance as yf
import math
import time
#totp = pyotp.TOTP('ZTDMX4R7ZR7WVR5OZWKCQWZ7C4K7QVVD', digest=hashlib.sha1)
def login(): 
    global avanza
    avanza = Avanza({
        'username': 'Simmelari',
        'password': 'Lampshopen1',
        'totpSecret': 'ZTDMX4R7ZR7WVR5OZWKCQWZ7C4K7QVVD'
        })

SKFopenpos = False
SEBopenpos = False
VOLVopenpos = False
ENROopenpos = False
MSONopenpos = False
INVEopenpos = False
SHBopenpos = False
ERICopenpos = False
ATCOopenpos = False
CATopenpos = False
ELUXopenpos = False
EPIopenpos = False
ESSITYopenpos = False
KINVopenpos = False
SSABopenpos = False 
RATOopenpos = False
TEL2openpos = False
STEopenpos = False
HUSQopenpos = False
SCAopenpos = False
ORTIopenpos = False
INDUopenpos = False
SVOLopenpos = False
SKFtime = ""
SEBtime = ""
VOLVtime = ""
ENROtime = ""
MSONtime = ""
INVEtime = ""
SHBtime = ""
ERICtime = ""
ATCOtime = ""
CATtime = ""
ELUXtime = ""
EPItime = ""
ESSITYtime = ""
KINVtime = ""
SSABtime = "" 
RATOtime = ""
TEL2time = ""
STEtime = ""
HUSQtime = ""
SCAtime = ""
ORTItime = ""
INDUtime = ""
SVOLtime = ""

t = datetime.date.today()
s = datetime.timedelta(30)
selldate = (t+s) #implimentera detta så varje individuell ticker har ett sell date (detta bara för att veta) hur vi ska göra sen



def getinfo(ticker):
    report = avanza.get_account_overview(
    account_id='7855257') 
    abcde = json.dumps(report, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False)
    Acountdata = json.loads(abcde)
    Acountdata = Acountdata['currencyAccounts']
    acountdata = Acountdata[0]
    acountdata = acountdata['balance']


    global price
    global volume
    price = yf.Ticker(ticker)
    price = price.info['regularMarketPrice'] #lowkey lägga till en liten marginal så vi får aktien
    köpvolym = acountdata*0.2
    volume = köpvolym // price




def buyorder_A(ticker):
    if volume < 0:
        result = avanza.place_order(
            account_id='7855257',
            order_book_id=ticker,
            order_type=OrderType.BUY,
            price=price,
            valid_until=date.fromisoformat('2023-12-12'),
            volume=volume
)

def buyorder_B(ticker):
    if volume < 0: #### ska vi ha såhär
        result = avanza.place_order(
            account_id='7855257',
            order_book_id=ticker,
            order_type=OrderType.SELL,
            price=price,
            valid_until=date.fromisoformat('2023-12-12'),
            volume=volume
)
###############################################################
def sellorder_A(ticker):
    if volume < 0:
        result = avanza.place_order(
            account_id='7855257',
            order_book_id=ticker,
            order_type=OrderType.BUY,
            price=price,
            valid_until=date.fromisoformat('2023-12-12'),
            volume=volume
)


def sellorder_B(ticker):
    if volume < 0: ### stämmer detta
        result = avanza.place_order(
            account_id='7855257',
            order_book_id=ticker,
            order_type=OrderType.SELL,
            price=price,
            valid_until=date.fromisoformat('2023-12-12'),
            volume=volume
)


##################################
def standardavikelse(A,B):
    aktie_A = yf.download(f'{A}', '2015-1-1','2022-11-07')
    aktie_B = yf.download(f'{B}', '2015-1-1','2022-11-07')
    pris_A = aktie_A['Close']
    pris_B = aktie_B['Close']
    pris_skillnad = []
    for k in range(len(pris_A)):
        diff = abs(pris_A[k]-pris_B[k])
        pris_skillnad.append(diff)
    import numpy as np
    standard_avk = np.std(pris_skillnad, ddof=1)
    return standard_avk

def main_long_B_short_A(ta, tb):
    getinfo(ta)
    sellorder_A(ta)
    getinfo(tb)
    buyorder_B(tb)


def main_long_A_short_B(ta, tb):
    global SKFselldate
    getinfo(ta)
    buyorder_A(ta)
    getinfo(tb)
    sellorder_B(tb)

    
def main_sell(ta, tb):
    getinfo(ta) 
    sellorder_A(ta)
    getinfo(tb)
    sellorder_B(tb)

def main(ta,tb):
    global SKFopenpos
    global SEBopenpos
    global VOLVopenpos
    global ENROopenpos
    global MSONopenpos
    global INVEopenpos
    global SHBopenpos
    global ERICopenpos
    global ATCOopenpos
    global CATopenpos
    global ELUXopenpos
    global EPIopenpos
    global ESSITYopenpos
    global KINVopenpos
    global SSABopenpos 
    global RATOopenpos
    global TEL2openpos
    global STEopenpos
    global HUSQopenpos
    global SCAopenpos
    global ORTIopenpos
    global INDUopenpos
    global SVOLopenpos
    global SKFtime
    global SEBtime
    global VOLVtime
    global ENROtime
    global MSONtime
    global INVEtime
    global SHBtime
    global ERICtime
    global ATCOtime
    global CATtime
    global ELUXtime
    global EPItime
    global ESSITYtime
    global KINVtime
    global SSABtime 
    global RATOtime
    global TEL2time
    global STEtime
    global HUSQtime
    global SCAtime
    global ORTItime
    global INDUtime
    global SVOLtime
    
    Aktie_A = yf.Ticker(ta)
    Aktie_B = yf.Ticker(tb)
    
    if ta == "SKF-A":
            Aktie_pris_A = Aktie_A.info['regularMarketPrice']
            Aktie_pris_B = Aktie_B.info['regularMarketPrice'] 
            if abs(Aktie_pris_A-Aktie_pris_B)>(standardavikelse(ta,tb))*1.35 and SKFopenpos  == False: 
                if Aktie_pris_A > Aktie_pris_B:
                    main_long_B_short_A(ta, tb)
                    SKFopenpos = True
                    SKFtime = selldate ########### lägga till alla på detta
                else:
                    main_long_A_short_B(ta, tb)
                    SKFopenpos = True
                    SKFtime = selldate ################ detta 
            if  abs(Aktie_pris_A-Aktie_pris_B)<(standardavikelse(ta,tb)) and SKFopenpos == True:
                main_sell(ta, tb)
            if SKFtime == t: ################### och denna
                main_sell(ta, tb)
    elif ta == "VOLV-A":
            Aktie_pris_A = Aktie_A.info['regularMarketPrice']
            Aktie_pris_B = Aktie_B.info['regularMarketPrice'] 
            if abs(Aktie_pris_A-Aktie_pris_B)>(standardavikelse(ta,tb))*1.35 and VOLVopenpos  == False: 
                if Aktie_pris_A > Aktie_pris_B:
                    main_long_B_short_A(ta, tb)
                    VOLVopenpos  = True
                    VOLVtime = selldate
                else:
                    main_long_A_short_B(ta, tb)
                    VOLVopenpos  = True
                    VOLVtime = selldate
            if  abs(Aktie_pris_A-Aktie_pris_B)<(standardavikelse(ta,tb)) and VOLVopenpos == True:
                main_sell(ta, tb)
            if VOLVtime == t:
                main_sell(ta, tb)
    elif ta == "ENRO-PREF-A":
            Aktie_pris_A = Aktie_A.info['regularMarketPrice']
            Aktie_pris_B = Aktie_B.info['regularMarketPrice'] 
            if abs(Aktie_pris_A-Aktie_pris_B)>(standardavikelse(ta,tb))*1.35 and ENROopenpos  == False: 
                if Aktie_pris_A > Aktie_pris_B:
                    main_long_B_short_A(ta, tb)
                    ENROopenpos  = True
                    ENROtime = selldate
                else:
                    main_long_A_short_B(ta, tb)
                    ENROopenpos  = True
                    ENROtime = selldate

            if  abs(Aktie_pris_A-Aktie_pris_B)<(standardavikelse(ta,tb)) and ENROopenpos == True:
                main_sell(ta, tb)
            if ENROtime == t:
                main_sell(ta, tb)
    elif ta == "MSON-A":
            Aktie_pris_A = Aktie_A.info['regularMarketPrice']
            Aktie_pris_B = Aktie_B.info['regularMarketPrice'] 
            if abs(Aktie_pris_A-Aktie_pris_B)>(standardavikelse(ta,tb))*1.35 and MSONopenpos  == False: 
                if Aktie_pris_A > Aktie_pris_B:
                    main_long_B_short_A(ta, tb)
                    MSONopenpos  = True
                    MSONtime = selldate
                else:
                    main_long_A_short_B(ta, tb)
                    MSONopenpos  = True
                    MSONtime = selldate

            if  abs(Aktie_pris_A-Aktie_pris_B)<(standardavikelse(ta,tb)) and MSONopenpos == True:
                main_sell(ta, tb)
            if MSONtime == t:
                main_sell(ta, tb)
    elif ta == "INVE-A":
            Aktie_pris_A = Aktie_A.info['regularMarketPrice']
            Aktie_pris_B = Aktie_B.info['regularMarketPrice'] 
            if abs(Aktie_pris_A-Aktie_pris_B)>(standardavikelse(ta,tb))*1.35 and INVEopenpos  == False: 
                if Aktie_pris_A > Aktie_pris_B:
                    main_long_B_short_A(ta, tb)
                    INVEopenpos  = True
                    INVEtime = selldate
                else:
                    main_long_A_short_B(ta, tb)
                    INVEopenpos  = True
                    INVEtime = selldate
                    
            if  abs(Aktie_pris_A-Aktie_pris_B)<(standardavikelse(ta,tb)) and INVEopenpos == True:
                main_sell(ta, tb)
            if INVEtime == t:
                main_sell(ta, tb)
    elif ta == "SEB-A":
            Aktie_pris_A = Aktie_A.info['regularMarketPrice']
            Aktie_pris_B = Aktie_B.info['regularMarketPrice'] 
            if abs(Aktie_pris_A-Aktie_pris_B)>(standardavikelse(ta,tb))*1.35 and SEBopenpos  == False: 
                if Aktie_pris_A > Aktie_pris_B:
                    main_long_B_short_A(ta, tb)
                    SEBopenpos  = True
                    SEBtime = selldate
                else:
                    main_long_A_short_B(ta, tb)
                    SEBopenpos  = True
                    SEBtime = selldate

            if  abs(Aktie_pris_A-Aktie_pris_B)<(standardavikelse(ta,tb)) and SEBopenpos == True:
                main_sell(ta, tb)
            if SEBtime == t:
                main_sell(ta, tb)
    elif ta == "SHB-A":
            Aktie_pris_A = Aktie_A.info['regularMarketPrice']
            Aktie_pris_B = Aktie_B.info['regularMarketPrice'] 
            if abs(Aktie_pris_A-Aktie_pris_B)>(standardavikelse(ta,tb))*1.35 and SHBopenpos  == False: 
                if Aktie_pris_A > Aktie_pris_B:
                    main_long_B_short_A(ta, tb)
                    SHBopenpos = True
                    SHBtime = selldate
                else:
                    main_long_A_short_B(ta, tb)
                    SHBopenpos = True
                    SHBtime = selldate
                    
            if  abs(Aktie_pris_A-Aktie_pris_B)<(standardavikelse(ta,tb)) and SHBopenpos == True:
                main_sell(ta, tb)
            if SHBtime == t:
                main_sell(ta, tb)
    elif ta == "ERIC-A":
            Aktie_pris_A = Aktie_A.info['regularMarketPrice']
            Aktie_pris_B = Aktie_B.info['regularMarketPrice'] 
            if abs(Aktie_pris_A-Aktie_pris_B)>(standardavikelse(ta,tb))*1.35 and ERICopenpos  == False: 
                if Aktie_pris_A > Aktie_pris_B:
                    main_long_B_short_A(ta, tb)
                    ERICopenpos  = True
                    ERICtime = selldate
                else:
                    main_long_A_short_B(ta, tb)
                    ERICopenpos  = True
                    ERICtime = selldate

            if  abs(Aktie_pris_A-Aktie_pris_B)<(standardavikelse(ta,tb)) and ERICopenpos == True:
                main_sell(ta, tb)
            if ERICtime == t:
                main_sell(ta, tb)
    elif ta == "ATCO-A":
            Aktie_pris_A = Aktie_A.info['regularMarketPrice']
            Aktie_pris_B = Aktie_B.info['regularMarketPrice'] 
            if abs(Aktie_pris_A-Aktie_pris_B)>(standardavikelse(ta,tb))*1.35 and ATCOopenpos  == False: 
                if Aktie_pris_A > Aktie_pris_B:
                    main_long_B_short_A(ta, tb)
                    ATCOopenpos  = True
                    ATCOtime = selldate
                else:
                    main_long_A_short_B(ta, tb)
                    ATCOopenpos  = True
                    ATCOtime = selldate
                    
            if  abs(Aktie_pris_A-Aktie_pris_B)<(standardavikelse(ta,tb)) and ATCOopenpos == True:
                main_sell(ta, tb)
            if ATCOtime == t:
                main_sell(ta, tb)
    elif ta == "CAT-A":
            Aktie_pris_A = Aktie_A.info['regularMarketPrice']
            Aktie_pris_B = Aktie_B.info['regularMarketPrice'] 
            if abs(Aktie_pris_A-Aktie_pris_B)>(standardavikelse(ta,tb))*1.35 and CATopenpos  == False: 
                if Aktie_pris_A > Aktie_pris_B:
                    main_long_B_short_A(ta, tb)
                    CATopenpos  = True
                    CATtime = selldate
                else:
                    main_long_A_short_B(ta, tb)
                    CATopenpos  = True
                    CATtime = selldate
                    
            if  abs(Aktie_pris_A-Aktie_pris_B)<(standardavikelse(ta,tb)) and CATopenpos == True:
                main_sell(ta, tb)
            if CATtime == t:
                main_sell(ta, tb)
    elif ta == "ELUX-A":
            Aktie_pris_A = Aktie_A.info['regularMarketPrice']
            Aktie_pris_B = Aktie_B.info['regularMarketPrice'] 
            if abs(Aktie_pris_A-Aktie_pris_B)>(standardavikelse(ta,tb))*1.35 and ELUXopenpos  == False: 
                if Aktie_pris_A > Aktie_pris_B:
                    main_long_B_short_A(ta, tb)
                    ELUXopenpos  = True
                    ELUXtime = selldate
                else:
                    main_long_A_short_B(ta, tb)
                    ELUXopenpos  = True
                    ELUXtime = selldate
            if  abs(Aktie_pris_A-Aktie_pris_B)<(standardavikelse(ta,tb)) and ELUXopenpos == True:
                main_sell(ta, tb)
            if ELUXtime == t:
                main_sell(ta, tb)
    elif ta == "EPI-A":
            Aktie_pris_A = Aktie_A.info['regularMarketPrice']
            Aktie_pris_B = Aktie_B.info['regularMarketPrice'] 
            if abs(Aktie_pris_A-Aktie_pris_B)>(standardavikelse(ta,tb))*1.35 and EPIopenpos  == False: 
                if Aktie_pris_A > Aktie_pris_B:
                    main_long_B_short_A(ta, tb)
                    EPIopenpos  = True
                    EPItime = selldate
                else:
                    main_long_A_short_B(ta, tb)
                    EPIopenpos  = True
                    EPItime = selldate
            if  abs(Aktie_pris_A-Aktie_pris_B)<(standardavikelse(ta,tb)) and EPIopenpos == True:
                main_sell(ta, tb)
            if EPItime == t:
                main_sell(ta, tb)
    elif ta == "ESSITY-A":
            Aktie_pris_A = Aktie_A.info['regularMarketPrice']
            Aktie_pris_B = Aktie_B.info['regularMarketPrice'] 
            if abs(Aktie_pris_A-Aktie_pris_B)>(standardavikelse(ta,tb))*1.35 and ESSITYopenpos  == False: 
                if Aktie_pris_A > Aktie_pris_B:
                    main_long_B_short_A(ta, tb)
                    ESSITYopenpos  = True
                    ESSITYtime = selldate
                else:
                    main_long_A_short_B(ta, tb)
                    ESSITYopenpos  = True
                    ESSITYtime = selldate
            if  abs(Aktie_pris_A-Aktie_pris_B)<(standardavikelse(ta,tb)) and ESSITYopenpos == True:
                main_sell(ta, tb)
            if ESSITYtime == t:
                main_sell(ta, tb)
    elif ta == "KINV-A":
            Aktie_pris_A = Aktie_A.info['regularMarketPrice']
            Aktie_pris_B = Aktie_B.info['regularMarketPrice'] 
            if abs(Aktie_pris_A-Aktie_pris_B)>(standardavikelse(ta,tb))*1.35 and KINVopenpos  == False: 
                if Aktie_pris_A > Aktie_pris_B:
                    main_long_B_short_A(ta, tb)
                    KINVopenpos  = True
                    KINVtime = selldate
                else:
                    main_long_A_short_B(ta, tb)
                    KINVopenpos  = True
                    KINVtime = selldate
            if  abs(Aktie_pris_A-Aktie_pris_B)<(standardavikelse(ta,tb)) and KINVopenpos == True:
                main_sell(ta, tb)
            if KINVtime == t:
                main_sell(ta, tb)
    elif ta == "SSAB-A":
            Aktie_pris_A = Aktie_A.info['regularMarketPrice']
            Aktie_pris_B = Aktie_B.info['regularMarketPrice'] 
            if abs(Aktie_pris_A-Aktie_pris_B)>(standardavikelse(ta,tb))*1.35 and SSABopenpos  == False: 
                if Aktie_pris_A > Aktie_pris_B:
                    main_long_B_short_A(ta, tb)
                    SSABopenpos  = True
                    SSABtime = selldate
                else:
                    main_long_A_short_B(ta, tb)
                    SSABopenpos  = True
                    SSABtime = selldate
            if  abs(Aktie_pris_A-Aktie_pris_B)<(standardavikelse(ta,tb)) and SSABopenpos == True:
                main_sell(ta, tb)
            if SSABtime == t:
                main_sell(ta, tb)
    elif ta == "RATO-A":
            Aktie_pris_A = Aktie_A.info['regularMarketPrice']
            Aktie_pris_B = Aktie_B.info['regularMarketPrice'] 
            if abs(Aktie_pris_A-Aktie_pris_B)>(standardavikelse(ta,tb))*1.35 and RATOopenpos  == False: 
                if Aktie_pris_A > Aktie_pris_B:
                    main_long_B_short_A(ta, tb)
                    RATOopenpos  = True
                    RATOtime = selldate
                else:
                    main_long_A_short_B(ta, tb)
                    RATOopenpos  = True
                    RATOtime = selldate
            if  abs(Aktie_pris_A-Aktie_pris_B)<(standardavikelse(ta,tb)) and RATOopenpos == True:
                main_sell(ta, tb)
            if RATOtime == t:
                main_sell(ta, tb)
    elif ta == "TEL2-A":
            Aktie_pris_A = Aktie_A.info['regularMarketPrice']
            Aktie_pris_B = Aktie_B.info['regularMarketPrice'] 
            if abs(Aktie_pris_A-Aktie_pris_B)>(standardavikelse(ta,tb))*1.35 and TEL2openpos  == False: 
                if Aktie_pris_A > Aktie_pris_B:
                    main_long_B_short_A(ta, tb)
                    TEL2openpos  = True
                    TEL2time = selldate
                else:
                    main_long_A_short_B(ta, tb)
                    TEL2openpos  = True
                    TEL2time = selldate
            if  abs(Aktie_pris_A-Aktie_pris_B)<(standardavikelse(ta,tb)) and TEL2openpos == True:
                main_sell(ta, tb)
            if TEL2time == t:
                main_sell(ta, tb)
    elif ta == "STE-A":
            Aktie_pris_A = Aktie_A.info['regularMarketPrice']
            Aktie_pris_B = Aktie_B.info['regularMarketPrice'] 
            if abs(Aktie_pris_A-Aktie_pris_B)>(standardavikelse(ta,tb))*1.35 and STEopenpos  == False: 
                if Aktie_pris_A > Aktie_pris_B:
                    main_long_B_short_A(ta, tb)
                    STEopenpos  = True
                    STEtime = selldate
                else:
                    main_long_A_short_B(ta, tb)
                    STEopenpos  = True
                    STEtime = selldate
            if  abs(Aktie_pris_A-Aktie_pris_B)<(standardavikelse(ta,tb)) and STEopenpos == True:
                main_sell(ta, tb)
            if STEtime == t:
                main_sell(ta, tb)
    elif ta == "HUSQ-A":
            Aktie_pris_A = Aktie_A.info['regularMarketPrice']
            Aktie_pris_B = Aktie_B.info['regularMarketPrice'] 
            if abs(Aktie_pris_A-Aktie_pris_B)>(standardavikelse(ta,tb))*1.35 and HUSQopenpos  == False: 
                if Aktie_pris_A > Aktie_pris_B:
                    main_long_B_short_A(ta, tb)
                    HUSQopenpos  = True
                    HUSQtime = selldate
                else:
                    main_long_A_short_B(ta, tb)
                    HUSQopenpos  = True
                    HUSQtime = selldate
            if  abs(Aktie_pris_A-Aktie_pris_B)<(standardavikelse(ta,tb)) and HUSQopenpos == True:
                main_sell(ta, tb)
            if HUSQtime == t:
                main_sell(ta, tb)
    elif ta == "SCA-A":
            Aktie_pris_A = Aktie_A.info['regularMarketPrice']
            Aktie_pris_B = Aktie_B.info['regularMarketPrice'] 
            if abs(Aktie_pris_A-Aktie_pris_B)>(standardavikelse(ta,tb))*1.35 and SCAopenpos  == False: 
                if Aktie_pris_A > Aktie_pris_B:
                    main_long_B_short_A(ta, tb)
                    SCAopenpos  = True
                    SCAtime = selldate
                else:
                    main_long_A_short_B(ta, tb)
                    SCAopenpos  = True
                    SCAtime = selldate
            if  abs(Aktie_pris_A-Aktie_pris_B)<(standardavikelse(ta,tb)) and SCAopenpos == True:
                main_sell(ta, tb)
            if SCAtime == t:
                main_sell(ta, tb)
    elif ta == "ORTI-A":
            Aktie_pris_A = Aktie_A.info['regularMarketPrice']
            Aktie_pris_B = Aktie_B.info['regularMarketPrice'] 
            if abs(Aktie_pris_A-Aktie_pris_B)>(standardavikelse(ta,tb))*1.35 and ORTIopenpos  == False: 
                if Aktie_pris_A > Aktie_pris_B:
                    main_long_B_short_A(ta, tb)
                    ORTIopenpos  = True
                    ORTItime = selldate
                else:
                    main_long_A_short_B(ta, tb)
                    ORTIopenpos  = True
                    ORTItime = selldate
            if  abs(Aktie_pris_A-Aktie_pris_B)<(standardavikelse(ta,tb)) and ORTIopenpos == True:
                main_sell(ta, tb)
            if ORTItime == t:
                main_sell(ta, tb)   
    elif ta == "INDU-A":
            Aktie_pris_A = Aktie_A.info['regularMarketPrice']
            Aktie_pris_B = Aktie_B.info['regularMarketPrice'] 
            if abs(Aktie_pris_A-Aktie_pris_B)>(standardavikelse(ta,tb))*1.35 and INDUopenpos  == False: 
                if Aktie_pris_A > Aktie_pris_B:
                    main_long_B_short_A(ta, tb)
                    INDUopenpos  = True
                    INDUtime = selldate
                else:
                    main_long_A_short_B(ta, tb)
                    INDUopenpos  = True
                    INDUtime = selldate
            if  abs(Aktie_pris_A-Aktie_pris_B)<(standardavikelse(ta,tb)) and INDUopenpos == True:
                main_sell(ta, tb)
            if INDUtime == t:
                main_sell(ta, tb)
                    
    elif ta == "SVOL-A":
            Aktie_pris_A = Aktie_A.info['regularMarketPrice']
            Aktie_pris_B = Aktie_B.info['regularMarketPrice'] 
            if abs(Aktie_pris_A-Aktie_pris_B)>(standardavikelse(ta,tb))*1.35 and SVOLopenpos  == False: 
                if Aktie_pris_A > Aktie_pris_B:
                    main_long_B_short_A(ta, tb)
                    SVOLopenpos  = True
                    SVOLtime = selldate
                else:
                    main_long_A_short_B(ta, tb)
                    SVOLopenpos  = True
                    SVOLtime = selldate
            if  abs(Aktie_pris_A-Aktie_pris_B)<(standardavikelse(ta,tb)) and SVOLopenpos == True:
                main_sell(ta, tb)
            if SVOLtime == t:
                main_sell(ta, tb)
    

while True:
    e = datetime.datetime.today()
    b = e.weekday()
    a = e.hour
    c = str(e)
    reddays = ["2022-12-24","2022-12-25","2022-12-26","2022-12-27","2022-12-28","2022-12-29","2022-12-30","2022-12-31","2022-12-31","2022-12-29","2022-12-30","2022-12-31","2022-12-31"]
    if b <= 4 and a < 17 and a > 9 and not c in reddays: # Får ej gå över
        login()
        main("SKF-A.st", "SKF-B.st")
        main("SEB-A.st", "SEB-C.st")
        main('VOLV-A.st','VOLV-B.st')
        main('ENRO-PREF-A.st','ENRO-PREF-B.st')
        main('MSON-A.st','MSON-B.st')
        main('INVE-A.st','INVE-B.st')
        main('SHB-A.st','SHB-B.st')
        main('ERIC-A.st','ERIC-B.st')
        main('ATCO-A.st','ATCO-B.st')
        main('CAT-A.st','CAT-B.st')
        main('ELUX-A.st','ELUX-B.st')
        main('EPI-A.st', 'EPI-B.st')
        main('ESSITY-A.st','ESSITY-B.st')
        main('KINV-A.st', 'KINV-B.st')
        main('SSAB-A.st', 'SSAB-B.st')
        main('RATO-A.st','RATO-B.st')
        main('TEL2-A.st','TEL2-B.st')
        main('STE-A.st','STE-R.st')
        main('HUSQ-A.st','HUSQ-B.st')
        main('SCA-A.st','SCA-B.st')
        main('ORTI-A.st','ORTI-B.st')
        main('INDU-A.st','INDU-C.st')
        main('SVOL-A.st','SVOL-B.st')
    elif b  == 5:
        time.sleep(172800)
    elif b == 6:
        time.sleep(86400)
    elif a > 17:
        time.sleep(57600)
    elif c in reddays:
        time.sleep(86400)
