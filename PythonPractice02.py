import requests
import shutil

http_proxy  = "http://proxy.tatw.micron.com:8080/"
https_proxy = "http://proxy.tatw.micron.com:8080/"
proxyDict = { 
    "http":http_proxy, 
    "https":https_proxy              
}
rs = requests.session()
res = rs.get('https://fbfh.trade.gov.tw/rich/text/common/code_98/CheckImageCode.aspx', stream=True, verify=False, proxies=proxyDict)
f=open('check.jpg', 'wb')
shutil.copyfileobj(res.raw, f)
f.close()

# import IPython.display
# IPython.display.Image('check.png')
from IPython.display import Image
Image('check.jpg')


# The following block is for:
# Parse command line arguments.
# (Attempts to) load an image from disk.
# Prints the width, height, and depth of the image to the terminal.
# Displays the image to our screen.

import cv2
import numpy as np
import os
import argparse # Parser for command-line options, arguments and sub-commands

# install OpenCV3
# 執行 opencv3.exe ，安裝完以後，到 OpenCV 的安裝目錄中找到以下路徑：
# 「build」→「python」→「2.7」 接著看 Windows 的系統是 x64 或是 x86 來開啟資料夾，將裡面的 OpenCV 模組檔案「cv2.pyd」複製到 Python 的安裝目錄裡的「Lib」→「site-packages」目錄中。

print(cv2.__version__)
image_path= './check.jpg'
print(os.path.exists(image_path))

# construct the argument parse and parse the arguments
# type "python PythonPractice02.py -h" in terminal to provide useful help messages
ap = argparse.ArgumentParser(description='Process some images.')
ap.add_argument('-i', '--image', required=True,	help='path to the image file')
args = vars(ap.parse_args())

# load the image from disk and display the width, height, and depth
# image = cv2.imread(args["image"])
image = cv2.imread('check.jpg')
print(image)
(h, w, d) = image.shape
print("w: {}, h: {}, d: {}".format(w, h, d))

# cv2.imread always return NoneType: 
# let’s say you have a .JPEG file on disk and you knew you had the correct path to it. You then try to load the JPEG file via cv2.imread 
# and notice a NoneType or AssertionError. How can this be? The file exists!
# In this case, you likely forgot to compile OpenCV with JPEG file support enabled.

# show the image
if not image.empty() :
    cv2.imshow('imageShow', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#in terminal type: "python PythonPractice02.py --image check.jpg"