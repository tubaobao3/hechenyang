#coding:utf8
'''
@author:hechenyang
'''
import json,urllib2
import requests
from conf import my_conf
import traceback

def main(tester):

    textmod = {"product":"shoubai","uid":904769025
        ,"pd":"newspage","cuid":"7EFCA913DFC8B443CBF7C2F60115CA553C6100891FRICNHGQFH",
        "ua":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
        ,"device":'{"device_vendor": "vivo", "device_model": "vivo+X6Plus+D"}',"nid":9729339301958416748,"ip":"10.232.231.50","fork_type":"recard","location":'{"lat": "12944356","lng":"4845259","type":"bd09mc"}'}
    print(textmod)
    url = my_conf.url+'rest/2.0/wanxiang/v1/api/cardsrelate'
    try:
        res = requests.post(url=url,data=textmod)
        print(res.text)
        res = res.json()
        if res['errno'] != 0 and res['data'] == '':
            res = requests.post(url=url,data=textmod)
            print(res.text)
            res = res.json()
    except:
        print "异常信息如下:\n%s" % traceback.format_exc() 
    tester.assert_true(res['data'][0]['result'] != '')    
    tester.assert_true(res['errno'] == 0)
