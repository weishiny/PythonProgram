# Python and Anaconda (Opencv)

## Anaconda 是一個 all-in-one 的 Python 開發環境，對於初學者來說是個十分合適的開發環境包。Anaconda 具備了幾項特點：

```
- 便於安裝許多流行的科學、數學、工程、資料分析的 Python 模組  
- 免費並支援跨平台：Linux、Windows、Mac
- 內建 Spyder 編輯器和 Jupyter Notebook 環境 
- 方便建立不同的虛擬開發環境
```

記得安裝時要注意建議在安裝 anaconda 時勾選把環境變數加入（path environment variable），這樣在使用 cmder 時使用 conda 相關指令才不會出現錯誤，若一開始沒有勾選的話建議解除安裝後再重新安裝 anaconda 勾選加入環境變數。

## If you use Anaconda and are behind proxy, create .condarc file

**.condarc**

```

channels:
- defaults

# Show channel URLs when displaying what is going to be downloaded and
# in 'conda list'. The default is False.
show_channel_urls: True
allow_other_channels: True

proxy_servers:
    http: http://proxy.xxx.xxx.com:8080
    https: https://proxy.xxx.xxx.com:8080

ssl_verify: false

```

## Some useful command

```
顯示目前虛擬環境列表
conda info -e 
創建虛擬環境
conda create -n 套件名稱 python=3.6
進入虛擬環境（若是非 Windows cmder 環境加 source 於開頭） ，成功後提示字元變成：（套件名稱）$
activate 虛擬環境名稱
離開虛擬環境（若是非 Windows cmder 環境加 source 於開頭） 
deactivate
```

And then use the following to create virtual environment
接著要建立我們的專案虛擬環境，這樣在安裝操作套件時比較不容易被污染到 root 全域的環境（因為你可能會有很多專案，專案使用的套件不盡相同，正式上線時只要把相關套件資訊透過 pip freeze > requirements.txt 存起來，然後在正式上線的伺服器安裝 pip install -r requirements.txt 即可），啟動後會出現（套件名稱）的提示字元：


```
conda create -n python27 python=2.7
conda create -n python35 python=3.5
conda create -n python36 python=3.6
```

## 成功進入虛擬環境後（會出現小括號 python_examples_venv）代表已經進入虛擬環境，即可以在裡面執行 Python 程式並安裝相關套件於該虛擬環境下：

```
# 安裝 django web 框架套件
pip install django
# 執行 python 檔案
python hello.py
```

## Use the following script to check how many envs you have or just use Anaconda Navigator to check

```
conda info --envs
```

## switch to the environment you want

```
activate python27
```

## anaconda install package

```
anaconda search opencv

conda install -c https://conda.anaconda.org/menpo opencv
```

## execute python

```
1. type *jupyter notebook* in Terminal (cmd)
2. type *python abc.py* in Terminal (cmd)

```