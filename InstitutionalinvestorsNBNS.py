
# Request URL:http://www.twse.com.tw/fund/BFI82U?response=json&dayDate=20180212&weekDate=20180212&monthDate=20180212&type=day&_=1519194480209
# Request Method:GET

import requests
from bs4 import BeautifulSoup # for HTML parse
import json # for JSON parse

http_proxy  = "http://proxy.xxx.com:8080/"
https_proxy = "http://proxy.xxx.com:8080/"
proxyDict = { 
    "http":http_proxy, 
    "https":https_proxy              
}
rs = requests.session()
# res = rs.get('http://www.twse.com.tw/zh/page/trading/fund/BFI82U.html', stream=True, verify=False, proxies=proxyDict)
res = rs.get('http://www.twse.com.tw/fund/BFI82U?response=json&dayDate=20180212&weekDate=20180212&monthDate=20180212&type=day&_=1519194480209', stream=True, verify=False, proxies=proxyDict)

print(res.encoding)
# res.encoding = 'utf-8' # if the encoding is not 'utf-8'
print(res.text)

'''
soup = BeautifulSoup(res.text)
print(soup)
print(soup.select('#report-table'))
'''

def isjson_Func(jsonObjString):
  try:
    json_string = json.loads(jsonObjString)
    #json_object = json.load(jsonObj)
  except ValueError, e:
    return False
  return True

isJson = isjson_Func(res.text)
print(isJson)

if isJson:
    #https://docs.python.org/2/library/json.html
    '''
    json.load(fp[, encoding[, cls[, object_hook[, parse_float[, parse_int[, parse_constant[, object_pairs_hook[, **kw]]]]]]]])
        Deserialize fp (a .read()-supporting file-like object containing a JSON document) to a Python object using this conversion table.
    json.loads(s[, encoding[, cls[, object_hook[, parse_float[, parse_int[, parse_constant[, object_pairs_hook[, **kw]]]]]]]])
        Deserialize s (a str or unicode instance containing a JSON document) to a Python object using this conversion table.
    '''
    #ParsedData = json.load(res.text) # for JSON Object
    ParsedData = json.loads(res.text) # for JSON String
    
    print(ParsedData)
    print('****************')
    print(res.text)
    print('****************')
    print(ParsedData['data'][0])

    '''
    {u'stat': u'OK', u'title': u'107\u5e7402\u670812\u65e5 \u4e09\u5927\u6cd5\u4eba\u8cb7\u8ce3\u91d1\u984d\u7d71\u8a08\u8868', u'fields': [u'\u55ae\u4f4d\u540d\u7a31', u'\u8cb7\u9032\u91d1\u984d', u'\u8ce3\u51fa\u91d1\u984d', u'\u8cb7\u8ce3\u5dee\u984d'], u'notes': [u'\u81ea\u71df\u5546\u8868\u793a\u8b49\u5238\u81ea\u71df\u5546\u5c08\u6236\u3002', u'\u6295\u4fe1\u8868\u793a\u672c\u570b\u6295\u8cc7\u4fe1\u8a17\u57fa\u91d1\u3002', u'\u5916\u8cc7\u53ca\u9678\u8cc7\u8868\u793a\u4f9d\u300c\u83ef\u50d1\u53ca\u5916\u570b\u4eba\u6295\u8cc7\u8b49\u5238\u7ba1\u7406\u8fa6\u6cd5\u300d\u53ca\u300c\u5927\u9678\u5730\u5340\u6295\u8cc7\u4eba\u4f86\u81fa\u5f9e\u4e8b\u8b49\u5238\u6295\u8cc7\u53ca\u671f\u8ca8\u4ea4\u6613\u7ba1\u7406\u8fa6\u6cd5\u300d\u8fa6\u7406\u767b\u8a18\u7b49\u6295\u8cc7\u4eba\u3002', u'\u56e0\u5916\u8cc7\u81ea\u71df\u5546\u8cb7\u8ce3\u91d1\u984d\u5df2\u8a08\u5165\u81ea\u71df\u5546\u8cb7\u8ce3\u91d1\u984d\uff0c\u6545\u4e0d\u7d0d\u5165\u4e09\u5927\u6cd5\u4eba\u8cb7\u8ce3\u91d1\u984d\u4e4b\u5408\u8a08\u6578\u8a08\u7b97\u3002', u'\u672c\u7d71\u8a08\u8cc7\u8a0a\u542b\u4e00\u822c\u3001\u96f6\u80a1\u3001\u76e4\u5f8c\u5b9a\u50f9\u3001\u9245\u984d\uff0c\u4e0d\u542b\u62cd\u8ce3\u3001\u6a19\u8cfc\u3002', u'\u672c\u8cc7\u8a0a\u4ee5\u7576\u65e5\u539f\u59cb\u6210\u4ea4\u60c5\u5f62\u7d71\u8a08\uff0c\u4e0d\u4ee5\u8b49\u5238\u5546\u7533\u5831\u932f\u5e33\u3001\u66f4\u6b63\u5e33\u865f\u7b49\u8abf\u6574\u5f8c\u8cc7\u6599\u7d71\u8a08\u3002', u'\u5916\u5e63\u6210\u4ea4\u503c\u4fc2\u4ee5\u672c\u516c\u53f8\u7576\u65e5\u4e0b\u53483\u664230\u5206\u516c\u544a\u532f\u7387\u63db\u7b97\u5f8c\u52a0\u5165\u6210\u4ea4\u91d1\u984d\u3002<br>\u516c\u544a\u532f\u7387\u8acb\u53c3\u8003\u672c\u516c\u53f8\u9996\u9801>\u4ea4\u6613\u8cc7\u8a0a>\u96d9\u5e63ETF\u5c08\u5340>\u4ee3\u865f\u5c0d\u61c9\u53ca\u6bcf\u65e5\u516c\u544a\u532f\u7387\u3002'], u'params': {u'lang': u'zh', u'monthDate': u'20180212', u'format': None, u'dayDate': u'20180212', u'weekDate': u'20180212', u'controller': u'fund', u'action': u'BFI82U', u'type': u'day', u'_': u'1519194480209'}, u'date': u'20180212', u'data': [[u'\u81ea\u71df\u5546(\u81ea\u884c\u8cb7\u8ce3)', u'1,030,286,190', u'1,090,554,639', u'-60,268,449'], [u'\u81ea\u71df\u5546(\u907f\u96aa)', u'4,763,733,298', u'5,485,427,494', u'-721,694,196'], [u'\u6295\u4fe1', u'1,042,671,150', u'748,972,868', u'293,698,282'], [u'\u5916\u8cc7\u53ca\u9678\u8cc7(\u4e0d\u542b\u5916\u8cc7\u81ea\u71df\u5546)', u'26,840,656,025', u'46,217,674,659', u'-19,377,018,634'], [u'\u5916\u8cc7\u81ea\u71df\u5546', u'28,184,410', u'9,262,460', u'18,921,950'], [u'\u5408\u8a08', u'33,677,346,663', u'53,542,629,660', u'-19,865,282,997']]}
    ****************
    {"stat":"OK","title":"107年02月12日 三大法人買賣金額統計表","fields":["單位名稱","買進金額","賣出金額","買賣差額"],"date":"20180212","data":[["自營商(自行買賣)","1,030,286,190","1,090,554,639","-60,268,449"],["自營商(避險)","4,763,733,298","5,485,427,494","-721,694,196"],["投信","1,042,671,150","748,972,868","293,698,282"],["外資及陸資(不含外資自營商)","26,840,656,025","46,217,674,659","-19,377,018,634"],["外資自營商","28,184,410","9,262,460","18,921,950"],["合計","33,677,346,663","53,542,629,660","-19,865,282,997"]],"params":{"dayDate":"20180212","weekDate":"20180212","monthDate":"20180212","type":"day","_":"1519194480209","controller":"fund","format":null,"action":"BFI82U","lang":"zh"},"notes":["自營商表示證券自營商專戶。","投信表示本國投資信託基金。","外資及陸資表示依「華僑及外國人投資證券管理辦法」及「大陸地區投資人來臺從事證券投資及期貨交易管理辦法」辦理登記等投資人。","因外資自營商買賣金額已計入自營商買賣金額，故不納入三大法人買賣金額之合計數計算。","本統計資訊含一般、零股、盤後定價、鉅額，不含拍賣、標購。","本資訊以當日原始成交情形統計，不以證券商申報錯帳、更正帳號等調整後資料統計。","外幣成交值係以本公司當日下午3時30分公告匯率換算後加入成交金額。<br>公告匯率請參考本公司首頁>交易資訊>雙幣ETF專區>代號對應及每日公告匯率。"]}
    ****************
    [u'\u81ea\u71df\u5546(\u81ea\u884c\u8cb7\u8ce3)', u'1,030,286,190', u'1,090,554,639', u'-60,268,449']
    '''

    # handle Chinese gibberish (改用json.dumps or json.dump)
    
    # json.dumps預設狀況下，對於非ascii字元生成的是相對應的字元編碼，而非原始字元
    '''
    現場狀況是這樣的，在 json 編碼中，文字部份一定要 utf-8，大家都很清楚了，如果想搞別的編碼，就自己 escape，這種作法算偷吃步。在 python 的 json 模組裡面，
    算是很貼心(還是很雞婆？)，預設就是幫大家把文字都 escape 了。當然使用 ascii 的人都不會有感覺(我想大家也很無奈)。
    在 json.dump 裡面，有預設一個 ensure_ascii=True，就是強迫文字 escape 的選項。如果沒去動他的話，以下是出現的結果：
    "\u53f0\u6ce5"
    如果你確定你的文字是 utf-8，可設定成 ensure_ascii=False，像是：
    id_name[stockid].decode('cp950').encode('utf8')
    那結果就會是：
    "台泥"
    '''
    #use dumps' s ensure_ascii = False to solve Chinese gibberish issue
    #dumps the json object into an element
    DumpParsedData = json.dumps(res.text, ensure_ascii = False)
    #print(DumpParsedData) #to see chinese

    #load the json to a string
    respJsonStr = json.loads(DumpParsedData)
    print(respJsonStr['data'][0])
    # Output: "TypeError: string indices must be integers" while parsing JSON using Python?
    # Answer: Try replacing j = json.loads(json.dumps(jsonStr)) with j = json.loads(jsonStr).
    #         OR If jsonStr is a string representing an object in JSON, then json.dumps(jsonStr) is a string representing (a string representing an object in JSON)
    #         in JSON. That's perfectly valid, but when you loads it, you get back a string representing an object in JSON; you'd have to loads it twice to get back
    #         the original object.
    
    #load the json twice to a json object
    respJsonObj = json.loads(respJsonStr)
    print(respJsonObj['data'][0])
    # Output: [u'\u81ea\u71df\u5546(\u81ea\u884c\u8cb7\u8ce3)', u'1,030,286,190', u'1,090,554,639', u'-60,268,449']
    print(respJsonObj['data'][0][0])
    # Output: 自營商(自行買賣)

    type(respJsonObj['data']) #List

    for TotalList in respJsonObj['data']:
        print(TotalList)
        print('******')
        for eachList in TotalList:
            print(eachList)
        print('======')
    '''
    Output:
        [u'\u81ea\u71df\u5546(\u81ea\u884c\u8cb7\u8ce3)', u'1,030,286,190', u'1,090,554,639', u'-60,268,449']
        ******
        自營商(自行買賣)
        1,030,286,190
        1,090,554,639
        -60,268,449
        ======
        [u'\u81ea\u71df\u5546(\u907f\u96aa)', u'4,763,733,298', u'5,485,427,494', u'-721,694,196']
        ******
        自營商(避險)
        4,763,733,298
        5,485,427,494
        -721,694,196
        ======
        [u'\u6295\u4fe1', u'1,042,671,150', u'748,972,868', u'293,698,282']
        ******
        投信
        1,042,671,150
        748,972,868
        293,698,282
        ======
        [u'\u5916\u8cc7\u53ca\u9678\u8cc7(\u4e0d\u542b\u5916\u8cc7\u81ea\u71df\u5546)', u'26,840,656,025', u'46,217,674,659', u'-19,377,018,634']
        ******
        外資及陸資(不含外資自營商)
        26,840,656,025
        46,217,674,659
        -19,377,018,634
        ======
        [u'\u5916\u8cc7\u81ea\u71df\u5546', u'28,184,410', u'9,262,460', u'18,921,950']
        ******
        外資自營商
        28,184,410
        9,262,460
        18,921,950
        ======
        [u'\u5408\u8a08', u'33,677,346,663', u'53,542,629,660', u'-19,865,282,997']
        ******
        合計
        33,677,346,663
        53,542,629,660
        -19,865,282,997
        ======
    '''

    result = ''
    for TotalList in respJsonObj['data']:
        print(TotalList)
        print('******')
        for eachList in TotalList:
            result += eachList.join('| ')
        print(result)        
        print('======')
    '''
    Output:
        [u'\u81ea\u71df\u5546(\u81ea\u884c\u8cb7\u8ce3)', u'1,030,286,190', u'1,090,554,639', u'-60,268,449']
        ******
        |自營商(自行買賣) |1,030,286,190 |1,090,554,639 |-60,268,449 
        ======
        [u'\u81ea\u71df\u5546(\u907f\u96aa)', u'4,763,733,298', u'5,485,427,494', u'-721,694,196']
        ******
        |自營商(自行買賣) |1,030,286,190 |1,090,554,639 |-60,268,449 |自營商(避險) |4,763,733,298 |5,485,427,494 |-721,694,196 
        ======
        [u'\u6295\u4fe1', u'1,042,671,150', u'748,972,868', u'293,698,282']
        ******
        |自營商(自行買賣) |1,030,286,190 |1,090,554,639 |-60,268,449 |自營商(避險) |4,763,733,298 |5,485,427,494 |-721,694,196 |投信 |1,042,671,150 |748,972,868 |293,698,282 
        ======
        [u'\u5916\u8cc7\u53ca\u9678\u8cc7(\u4e0d\u542b\u5916\u8cc7\u81ea\u71df\u5546)', u'26,840,656,025', u'46,217,674,659', u'-19,377,018,634']
        ******
        |自營商(自行買賣) |1,030,286,190 |1,090,554,639 |-60,268,449 |自營商(避險) |4,763,733,298 |5,485,427,494 |-721,694,196 |投信 |1,042,671,150 |748,972,868 |293,698,282 |外資及陸資(不含外資自營商) |26,840,656,025 |46,217,674,659 |-19,377,018,634 
        ======
        [u'\u5916\u8cc7\u81ea\u71df\u5546', u'28,184,410', u'9,262,460', u'18,921,950']
        ******
        |自營商(自行買賣) |1,030,286,190 |1,090,554,639 |-60,268,449 |自營商(避險) |4,763,733,298 |5,485,427,494 |-721,694,196 |投信 |1,042,671,150 |748,972,868 |293,698,282 |外資及陸資(不含外資自營商) |26,840,656,025 |46,217,674,659 |-19,377,018,634 |外資自營商 |28,184,410 |9,262,460 |18,921,950 
        ======
        [u'\u5408\u8a08', u'33,677,346,663', u'53,542,629,660', u'-19,865,282,997']
        ******
        |自營商(自行買賣) |1,030,286,190 |1,090,554,639 |-60,268,449 |自營商(避險) |4,763,733,298 |5,485,427,494 |-721,694,196 |投信 |1,042,671,150 |748,972,868 |293,698,282 |外資及陸資(不含外資自營商) |26,840,656,025 |46,217,674,659 |-19,377,018,634 |外資自營商 |28,184,410 |9,262,460 |18,921,950 |合計 |33,677,346,663 |53,542,629,660 |-19,865,282,997 
        ======
    '''

    result = ''
    for TotalList in respJsonObj['data']:
        print(TotalList)
        print('******')
        for eachList in TotalList:
            result += eachList.join('| ')
        print(result)
        result = ''
        print('======')
    '''
    Output:
        [u'\u81ea\u71df\u5546(\u81ea\u884c\u8cb7\u8ce3)', u'1,030,286,190', u'1,090,554,639', u'-60,268,449']
        ******
        |自營商(自行買賣) |1,030,286,190 |1,090,554,639 |-60,268,449 
        ======
        [u'\u81ea\u71df\u5546(\u907f\u96aa)', u'4,763,733,298', u'5,485,427,494', u'-721,694,196']
        ******
        |自營商(避險) |4,763,733,298 |5,485,427,494 |-721,694,196 
        ======
        [u'\u6295\u4fe1', u'1,042,671,150', u'748,972,868', u'293,698,282']
        ******
        |投信 |1,042,671,150 |748,972,868 |293,698,282 
        ======
        [u'\u5916\u8cc7\u53ca\u9678\u8cc7(\u4e0d\u542b\u5916\u8cc7\u81ea\u71df\u5546)', u'26,840,656,025', u'46,217,674,659', u'-19,377,018,634']
        ******
        |外資及陸資(不含外資自營商) |26,840,656,025 |46,217,674,659 |-19,377,018,634 
        ======
        [u'\u5916\u8cc7\u81ea\u71df\u5546', u'28,184,410', u'9,262,460', u'18,921,950']
        ******
        |外資自營商 |28,184,410 |9,262,460 |18,921,950 
        ======
        [u'\u5408\u8a08', u'33,677,346,663', u'53,542,629,660', u'-19,865,282,997']
        ******
        |合計 |33,677,346,663 |53,542,629,660 |-19,865,282,997 
        ======
    '''
else:
    print('response is not a JSON Object')


from datetime import date, timedelta
today = date.today()

for i in range(1, 10):
    today = today + timedelta(days = -1) # last 10 days from today
    print(today) #西元年 2018-02-22
    print(str(today).split('-')) #民國年:變成字串後用split, 2018-02-22用中間'-', 將元素存在list裡 => ['2018', '02', '22']
    dayarray = str(today).split('-') #把元素丟到dayarray裡
    print([str(int(dayarray[0]) - 1911), dayarray[1], dayarray[2]]) #把dayarray裡的年份值轉成整數型態後減去1911即為民國年,最後再轉成string成為list中的其中一個元素 => ['107', '02', '22']
    print('-'.join([str(int(dayarray[0]) - 1911), dayarray[1], dayarray[2]])) #最後把list轉成string, 利用 '-'.join() 去將所有元素用 '-' 串起來 => 107-02-22

print(date.today() + timedelta(days = -1)) #yesterday
print(date.today() + timedelta(days = 1)) #tomorrow




'''
[交易系統] 如何抓取多天期的三大法人交易資訊?
在瞭解如何產生不同天期的資訊後，我們便可以利用這個資訊抓取多天期的三大法人交易資訊。
我們只要簡單的利用def將重複地抓取動作包裝在Python 的函式中，再加上簡單的迴圈，就可以成功完成多天期的抓取！
'''

# http://www.twse.com.tw/fund/BFI82U?response=json&dayDate=20180223&weekDate=20180221&monthDate=20180222&type=day&_=1519371031215
'''
response:json
dayDate:20180223 =>日報表日期
weekDate:20180221 =>周報表日期
monthDate:20180222 =>月報表日期
type:day =>是用哪種方式(日周月)進行查詢
_:1519371031215
'''
url = 'http://www.twse.com.tw/fund/BFI82U?response=json&dayDate={0}&weekDate=20180221&monthDate=20180222&type=day&_=1519371031215'

def getTradeValue(dt):
    http_proxy  = "http://proxy.xxx.com:8080/"
    https_proxy = "http://proxy.xxx.com:8080/"
    proxyDict = { 
        "http":http_proxy, 
        "https":https_proxy              
    }
    rs = requests.session()
    #res = rs.get('http://www.twse.com.tw/fund/BFI82U?response=json&dayDate=20180212&weekDate=20180212&monthDate=20180212&type=day&_=1519194480209', stream=True, verify=False, proxies=proxyDict)
    res = rs.get(url.format(dt), stream=True, verify=False, proxies=proxyDict)

    isJson = isjson_Func(res.text)
    if isJson:
        DumpParsedData = json.dumps(res.text, ensure_ascii = False)
        respJsonStr = json.loads(DumpParsedData)
        respJsonObj = json.loads(respJsonStr)
        #print(DumpParsedData)

        '''
        If there is this kind of data (holiday), we should cope with this error which don't have 'data' key (for TotalList in respJsonObj['data'])
        "{\"stat\":\"很抱歉，沒有符合條件的資料!\"}"
        '''

        # Check if key exists or not
        # h = {'a': 1}
        # 'b' in h #returns False
        '''
        if 'data' not in respJsonObj:
            raise ValueError("No target key in given data")
        '''
        '''
        Output:

            "{\"stat\":\"查詢日期小於093年03月31日，請重新查詢!\"}"
            ---------------------------------------------------------------------------
            ValueError                                Traceback (most recent call last)
            <ipython-input-114-f4db66f8bdc1> in <module>()
                2     today = today + timedelta(days = -1) # last 10 days from today => 2018-02-22
                3     todayData = str(today).replace('-','') # 20180222
            ----> 4     getTradeValue(todayData)

            <ipython-input-113-ff51f5637e92> in getTradeValue(dt)
                36         print(DumpParsedData)
                37         if 'data' not in respJsonObj:
            ---> 38             raise ValueError("No target key in given data")
                39         
                40         result = ''

            ValueError: No target key in given data
        '''

        if 'data' not in respJsonObj:
            print(dt + ' no data')
            return False

        result = ''        
        for TotalList in respJsonObj['data']:            
            #print(TotalList)
            #print('******')
            for eachList in TotalList:
                result += eachList.join('| ')                
            print(result)
            result = ''
            #print('======')
    else:
        print('response is not a JSON Object')

todayDate = date.today()
tomorrowDate = todayDate + timedelta(days = 1)
for i in range(1, 10):
    # no including today
    todayDate = todayDate + timedelta(days = -1) # last 10 days from today (2018-02-23) => 2018-02-22 start
    todayDateData = str(todayDate).replace('-','') # 20180222
    print('******' + todayDateData + '******')
    getTradeValue(todayDateData)

    # including today
    tomorrowDate = tomorrowDate + timedelta(days = -1) # last 10 days from tomorrow (2018-02-24) => 2018-02-23 start
    tomorrowDateData = str(tomorrowDate).replace('-','') # 20180223
    print('******' + tomorrowDateData + '******')
    getTradeValue(tomorrowDateData)

# no including today
'''
******20180222******
|自營商(自行買賣) |1,500,809,390 |1,008,802,447 |492,006,943 
|自營商(避險) |5,126,937,860 |6,009,291,069 |-882,353,209 
|投信 |1,143,036,000 |1,126,134,252 |16,901,748 
|外資及陸資(不含外資自營商) |43,223,382,225 |50,106,568,089 |-6,883,185,864 
|外資自營商 |247,992,940 |156,228,450 |91,764,490 
|合計 |50,994,165,475 |58,250,795,857 |-7,256,630,382 
******20180221******
|自營商(自行買賣) |2,084,686,690 |2,001,708,610 |82,978,080 
|自營商(避險) |7,258,058,083 |5,629,989,660 |1,628,068,423 
|投信 |1,437,368,500 |1,030,476,902 |406,891,598 
|外資及陸資(不含外資自營商) |72,233,013,946 |63,019,389,834 |9,213,624,112 
|外資自營商 |28,540,090 |265,362,920 |-236,822,830 
|合計 |83,013,127,219 |71,681,565,006 |11,331,562,213 
******20180220******
20180220 no data
******20180219******
20180219 no data
******20180218******
20180218 no data
******20180217******
20180217 no data
******20180216******
20180216 no data
******20180215******
20180215 no data
******20180214******
20180214 no data
'''
    
# including today
'''
******20180223******
|自營商(自行買賣) |1,184,750,550 |1,205,139,327 |-20,388,777 
|自營商(避險) |6,206,346,170 |5,609,218,935 |597,127,235 
|投信 |1,438,453,760 |715,541,572 |722,912,188 
|外資及陸資(不含外資自營商) |30,568,680,887 |28,444,584,432 |2,124,096,455 
|外資自營商 |159,366,610 |194,880,740 |-35,514,130 
|合計 |39,398,231,367 |35,974,484,266 |3,423,747,101 
******20180222******
|自營商(自行買賣) |1,500,809,390 |1,008,802,447 |492,006,943 
|自營商(避險) |5,126,937,860 |6,009,291,069 |-882,353,209 
|投信 |1,143,036,000 |1,126,134,252 |16,901,748 
|外資及陸資(不含外資自營商) |43,223,382,225 |50,106,568,089 |-6,883,185,864 
|外資自營商 |247,992,940 |156,228,450 |91,764,490 
|合計 |50,994,165,475 |58,250,795,857 |-7,256,630,382 
******20180221******
|自營商(自行買賣) |2,084,686,690 |2,001,708,610 |82,978,080 
|自營商(避險) |7,258,058,083 |5,629,989,660 |1,628,068,423 
|投信 |1,437,368,500 |1,030,476,902 |406,891,598 
|外資及陸資(不含外資自營商) |72,233,013,946 |63,019,389,834 |9,213,624,112 
|外資自營商 |28,540,090 |265,362,920 |-236,822,830 
|合計 |83,013,127,219 |71,681,565,006 |11,331,562,213 
******20180220******
20180220 no data
******20180219******
20180219 no data
******20180218******
20180218 no data
******20180217******
20180217 no data
******20180216******
20180216 no data
******20180215******
20180215 no data
'''