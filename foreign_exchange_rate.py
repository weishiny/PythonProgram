# conda install pandas
# conda install lxml
# conda install html5lib
# conda install BeautifulSoup4

# You are behind proxy (https://docs.python.org/2/library/urllib2.html)
import pandas
import urllib2

url = 'http://rate.bot.com.tw/xrt?Lang=zh-TW'

# urllib2.ProxyHandler([proxies])
# Cause requests to go through a proxy. If proxies is given, it must be a dictionary mapping protocol names to URLs of proxies. The default is to read the list 
# of proxies from the environment variables <protocol>_proxy. If no proxy environment variables are set, then in a Windows environment proxy settings are obtained
# from the registry’s Internet Settings section, and in a Mac OS X environment proxy information is retrieved from the OS X System Configuration Framework.

# build_opener() provides many handlers by default, including a ProxyHandler. By default, ProxyHandler uses the environment variables named <scheme>_proxy, where
# <scheme> is the URL scheme involved. For example, the http_proxy environment variable is read to obtain the HTTP proxy’s URL.
# This example replaces the default ProxyHandler with one that uses programmatically-supplied proxy URLs, and adds proxy authorization support with ProxyBasicAuthHandler.

'''
proxy_handler = urllib2.ProxyHandler({'http': 'http://www.example.com:3128/'})
proxy_auth_handler = urllib2.ProxyBasicAuthHandler()
proxy_auth_handler.add_password('realm', 'host', 'username', 'password')

opener = urllib2.build_opener(proxy_handler, proxy_auth_handler)
# This time, rather than install the OpenerDirector, we use it directly:
opener.open('http://www.example.com/login.html')
'''
proxy_support = urllib2.ProxyHandler({'http':'http://proxy.tytw.micron.com:8080'})

# urllib2.build_opener([handler, ...])
# Return an OpenerDirector instance, which chains the handlers in the order given. handlers can be either instances of BaseHandler, or subclasses of BaseHandler
# Instances of the following classes will be in front of the handlers, unless the handlers contain them, instances of them or subclasses of them: ProxyHandler 
# (if proxy settings are detected), UnknownHandler, HTTPHandler, HTTPDefaultErrorHandler, HTTPRedirectHandler, FTPHandler, FileHandler, HTTPErrorProcessor.
opener = urllib2.build_opener(proxy_support)

# OpenerDirector.open(url[, data][, timeout])
# Open the given url (which can be a request object or a string), optionally passing the given data. Arguments, return values and exceptions raised are the same 
# as those of urlopen() (which simply calls the open() method on the currently installed global OpenerDirector). The optional timeout parameter specifies a 
# timeout in seconds for blocking operations like the connection attempt (if not specified, the global default timeout setting will be used). The timeout feature
# actually works only for HTTP, HTTPS and FTP connections).
response = opener.open(url)

dfs = pandas.read_html(response.read())
type(dfs)
len(dfs)

currency = dfs[0]
type(currency) # it's pandas.core.frame.DataFrame

# Get first five columns
# .ix is deprecated. Please use .loc for label based indexing or .iloc for positional indexing
'''
First, here's a recap of the three methods:

loc gets rows (or columns) with particular labels from the index.
iloc gets rows (or columns) at particular positions in the index (so it only takes integers).
ix usually tries to behave like loc but falls back to behaving like iloc if a label is not present in the index.
'''
# currency = currency.ix[:, 0:5] # 所有列都要, 只要前五欄
# currency = currency.loc[:, '遠期匯率'] # 所有列都要, 只要前五欄
currency = currency.iloc[:, 0:5] # 所有列都要, 只要前五欄 currency = currency.iloc[:, :5]

# change column name
# add 'u' before column name to solve encoding issue, transfer to unicode
currency.columns = [u'幣別', u'現金匯率-本行買入', u'現金匯率-本行賣出', u'即期匯率-本行買入', u'即期匯率-本行賣出']

# show currency table with name changed
currency

# get english symbol (透過pandas取出幣別資訊, 將小括號中的英文代碼抽出來, 利用正規表達式, 要抽取的資料用小括號包起來, w+代表英文字出現多個以上)
'''
'+' : 匹配至少一次
'\w' : 匹配任何字母數字字符；它相當於類 [a-zA-Z0-9_]
'\' : 使用限制字元 => \( 代表可出現括號 '('
'''
currency[u'幣別'] = currency[u'幣別'].str.extract('\((\w+)\)')

# show currency table with name changed
currency

currency.to_excel('currency.xlsx')
currency.to_csv('currency.csv')

# You are not behind proxy
'''
import pandas
dfs = pandas.read_html('http://rate.bot.com.tw/xrt?Lang=zh-TW')
type(dfs)
len(dfs)

currency = dfs[0]
type(currency)

pandas.core.frame.DataFrame
currency = currency.ix[:,0:5]

currency.columns = [u'幣別', u'現金匯率-本行買入', u'現金匯率-本行賣出', u'即期匯率-本行買入', u'即期匯率-本行賣出' ]
currency[u'幣別'] = currency[u'幣別'].str.extract('\((\w+)\)')
currency.to_excel('currency.xlsx')
'''


# draw chart
df = pandas.read_csv('ExchangeRate@201802141305.csv')
df.head()

# 再做資料繪圖前須先了解資料型態
df.info()

# 所以為整數型態, 20180214是整數而不是日期, 所以需要轉成日期形態
'''
<class 'pandas.core.frame.DataFrame'>
Int64Index: 129 entries, 20180214 to 20170815
Data columns (total 22 columns):
資料日期        129 non-null object
幣別          129 non-null object
匯率          129 non-null float64
現金          129 non-null float64
即期          129 non-null float64
遠期10天       129 non-null float64
遠期30天       129 non-null float64
遠期60天       129 non-null float64
遠期90天       129 non-null float64
遠期120天      129 non-null float64
遠期150天      129 non-null float64
遠期180天      129 non-null object
匯率.1        129 non-null float64
現金.1        129 non-null float64
即期.1        129 non-null float64
遠期10天.1     129 non-null float64
遠期30天.1     129 non-null float64
遠期60天.1     129 non-null float64
遠期90天.1     129 non-null float64
遠期120天.1    129 non-null float64
遠期150天.1    129 non-null float64
遠期180天.1    0 non-null float64
dtypes: float64(19), object(3)
memory usage: 23.2+ KB
'''

?pandas.to_datetime # show documentation for help
df.index = pandas.to_datetime(df.index, format = '%Y%m%d') #將index從整數轉換成時間
'''
DatetimeIndex(['2018-02-14', '2018-02-13', '2018-02-12', '2018-02-09',
               '2018-02-08', '2018-02-07', '2018-02-06', '2018-02-05',
               '2018-02-02', '2018-02-01',
               ...
               '2017-08-28', '2017-08-25', '2017-08-24', '2017-08-23',
               '2017-08-22', '2017-08-21', '2017-08-18', '2017-08-17',
               '2017-08-16', '2017-08-15'],
              dtype='datetime64[ns]', length=129, freq=None)
'''


df.info()
'''
<class 'pandas.core.frame.DataFrame'>
DatetimeIndex: 129 entries, 2018-02-14 to 2017-08-15
Data columns (total 22 columns):
資料日期        129 non-null object
幣別          129 non-null object
匯率          129 non-null float64
現金          129 non-null float64
即期          129 non-null float64
遠期10天       129 non-null float64
遠期30天       129 non-null float64
遠期60天       129 non-null float64
遠期90天       129 non-null float64
遠期120天      129 non-null float64
遠期150天      129 non-null float64
遠期180天      129 non-null object
匯率.1        129 non-null float64
現金.1        129 non-null float64
即期.1        129 non-null float64
遠期10天.1     129 non-null float64
遠期30天.1     129 non-null float64
遠期60天.1     129 non-null float64
遠期90天.1     129 non-null float64
遠期120天.1    129 non-null float64
遠期150天.1    129 non-null float64
遠期180天.1    0 non-null float64
dtypes: float64(19), object(3)
memory usage: 23.2+ KB
'''

# %pylab inline : jupyter notebook magic => 可讓資料繪在jupyter notebook中
# Populating the interactive namespace from numpy and matplotlib
%pylab inline
df.plot(kind = 'line', y = ['匯率', '現金'])