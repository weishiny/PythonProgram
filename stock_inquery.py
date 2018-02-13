import numpy as np
import matplotlib.pyplot as plt
import cv2

image = cv2.imread('CaptchaImage.jpg')
plt.imshow(image)
plt.show()

# 去掉圖形白線及白點
'''
# numpy.ones: Return a new array of given shape and type, filled with ones.
# Parameters:	
# shape : int or sequence of ints ; Shape of the new array, e.g., (2, 3) or 2.
# dtype : data-type, optional ; The desired data-type for the array, e.g., numpy.int8. Default is numpy.float64.
# order : {‘C’, ‘F’}, optional ; Whether to store multidimensional data in C- or Fortran-contiguous (row- or column-wise) order in memory.
# Returns: out : ndarray ; Array of ones with the given shape, dtype, and order.
'''
kernel = np.ones((4, 4), np.uint8) # 設定一個4 x 4的橡皮擦,橡皮擦周邊沒有資料(沒有顏色)的話,自動把周圍的地方歸位成沒有顏色的, 透過erode可以把線做擦掉的動作

# OpenCV侵蝕
'''
# erode(const Mat &src, Mat &dst, Mat kernel, Point anchor=Point(-1,-1), int iterations=1)
# src：輸入圖，可以多通道，深度可為CV_8U、CV_16U、CV_16S、CV_32F或CV_64F。
# dst：輸出圖，和輸入圖尺寸、型態相同。
# kernel：結構元素，如果kernel=Mat()則為預設的3×3矩形，越大侵蝕效果越明顯。
# anchor：原點位置，預設為結構元素的中央。
# iterations：執行次數，預設為1次，執行越多次侵蝕效果越明顯。
'''
erosion = cv2.erode(image, kernel, iterations = 1) # 做削減動作把線拿掉
# show what erosion looks like
# plt.imshow(erosion)
# plt.show()

# Gaussian Blurring
'''
# In this, instead of box filter, gaussian kernel is used. It is done with the function, cv2.GaussianBlur(). We should specify the width and height of kernel 
# which should be positive and odd. We also should specify the standard deviation in X and Y direction, sigmaX and sigmaY respectively. If only sigmaX is 
# specified, sigmaY is taken as same as sigmaX. If both are given as zeros, they are calculated from kernel size. Gaussian blurring is highly effective in 
# removing gaussian noise from the image.
# If you want, you can create a Gaussian kernel with the function, cv2.getGaussianKernel(). The above code can be modified for Gaussian blurring:
'''
blurred = cv2.GaussianBlur(erosion, (5, 5), 0) # 把旁邊的點作淡化的動作

edged = cv2.Canny(blurred, 30, 150) # 偵測字的邊界
# show what edged looks like
# plt.imshow(edged)
# plt.show()

# OpenCV膨脹
'''
# dilate(const Mat &src, Mat &dst, Mat kernel, Point anchor=Point(-1,-1), int iterations=1)
# src：輸入圖，可以多通道，深度可為CV_8U、CV_16U、CV_16S、CV_32F或CV_64F。
# dst：輸出圖，和輸入圖尺寸、型態相同。
# kernel：結構元素，如果kernel=Mat()則為預設的3×3矩形，越大膨脹效果越明顯。
# anchor：原點位置，預設為結構元素的中央。
# iterations：執行次數，預設為1次，執行越多次膨脹效果越明顯。
'''
dilation = cv2.dilate(edged, kernel, iterations = 1) # 先前做削減動作把線拿掉,可能把字的連結拿掉了, 所以利用膨脹把連結補回去
# show what dilation looks like
# plt.imshow(dilation)
# plt.show()

# OpenCV找輪廓
'''
# void findContours(InputOutputArray image, OutputArrayOfArrays contours, OutputArray hierarchy, int mode, int method, Pointoffset=Point())
# void findContours(InputOutputArray image, OutputArrayOfArrays contours, int mode, int method, Point offset=Point())
# image：輸入圖，使用八位元單通道圖，所有非零的像素都會列入考慮，通常為二極化後的圖。
# contours：包含所有輪廓的容器(vector)，每個輪廓都是儲存點的容器(vector)，所以contours的資料結構為vector< vector>。
# hierarchy：可有可無的輸出向量，以階層的方式記錄所有輪廓。
# mode：取得輪廓的模式。
# method：儲存輪廓點的方法。

# mode：取得輪廓的模式，有以下幾種可選擇：
# CV_RETR_EXTERNAL：只取最外層的輪廓。
# CV_RETR_LIST：取得所有輪廓，不建立階層(hierarchy)。
# CV_RETR_CCOMP：取得所有輪廓，儲存成兩層的階層，首階層為物件外圍，第二階層為內部空心部分的輪廓，如果更內部有其餘物件，包含於首階層。
# CV_RETR_TREE：取得所有輪廓，以全階層的方式儲存。

# method：儲存輪廓點的方法，有以下幾種可選擇：
# CV_CHAIN_APPROX_NONE：儲存所有輪廓點。
# CV_CHAIN_APPROX_SIMPLE：對水平、垂直、對角線留下頭尾點，所以假如輪廓為一矩形，只儲存對角的四個頂點。
'''
# image, contours, hierarchy = cv2.findContours(dilation.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# ValueError: need more than 2 values to unpack
# In OpenCV 2, findContours returns just two values, contours and hierarchy. The error occurs when python tries to assign those two values 
# to the three names given on left in this statement:
contours, hierarchy = cv2.findContours(dilation.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 排序是用程式處理資料中最常用到功能，python提供了很方便的sort函式, lambda是簡易型函式，只能回傳一個值, 因此如果需要兩個值以上的排列順序，會用attrgetter
'''
student_objects=[]
student_objects.append( Student('john', 'B', 15) )
student_objects.append( Student('dave', 'A', 12) )
student_objects.append( Student('jane', 'A', 10) )

student_objects.sort(key=lambda i: i.grade) 
for i in student_objects:
    print i.name,i.grade,i.age 
print

from operator import attrgetter 

student_objects.sort(key=attrgetter('grade', 'age'),reverse=True)  
for i in student_objects:
    print i.name,i.grade,i.age 
print


Output:
dave A 12
jane A 10
john B 15

john B 15
dave A 12
jane A 10
'''

# 在Python中, 我們很輕易就可以得到一個排序過的list: 使用sorted(). sorted()會傳回一個新的list, 並不會改動到原來的list.
'''
colors = ['red', 'green', 'blue', 'yellow']
for color in sorted(colors):
    print(color)
'''
# 如果要做自訂的排序規則, 例如用字串的長度來排序
# 使用key, 它會將list的項目用key的函式來計算出值(在此例是len()), 再依此值來排序. 又快又簡單.
'''
print(sorted(colors, key=len))
'''
# 可以用lambda運算式來定義函式，執行運算式時將會產生函式物件
# lambda中不能有區塊，這表示一些小的運算任務你可以使用lambda，而較複雜的邏輯你可以使用def來定義
'''
def max(m, n):
    return m if m > n else n
print(max(10, 3))  # 顯示 10

# "m if m > n else n"
# we could use ternary operator "?:" to do "test ? expression1 : expression2" in another language but in Python don't have this kind of syntax
# def foo(logging):
#    if logging:
#        level = 1
#    else:
#        level = 0
# => we are used to using this syntax in Python because Python don't have ternary operator "?:"
# def foo(logging):
#    level = (1 if logging else 0)

=>

max = lambda m, n: m if m > n else n
print(max(10, 3))  # 顯示 10
'''
# x is list from [(c, cv2.boundingRect(c)[0]) for c in contours]
# x[0] is c, x[1] is cv2.boundingRect(c)[0]
# 用 x[1] => cv2.boundingRect(c)[0] 去排序
cnts = sorted([(c, cv2.boundingRect(c)[0]) for c in contours], key = lambda x: x[1])

'''
def my_function(x,y):
    return x-10,y+10
x,y = my_function(10,20)
print x,y


Output:
0 30
'''
ary = []
for (c, _) in cnts:
    (x, y, w, h) = cv2.boundingRect(c)
    # 我們可以使用變數取出tuple中的元素，稱作unpacking(開箱)
    '''
    t = (1, 2, 3)
    a, b, c= t
    print('a=', a, ',b=', b, ',c=', c)

    Output: a= 1 ,b= 2 ,c= 3    
    '''
    # 第一個是 tuple packing ，等號右邊被打包成 tuple ，第二個是 tuple unpacking ，就是反過來
    '''
    t = 12345, 54321, 'hello!'
    x, y, z = t
    '''
    # print(x, y, w, h)
    # 字型都有一定的大小, 所以寬高大於15的才放入
    if w > 15 and h > 15:
        ary.append((x, y, w, h))

# 分割成不同的單一個字圖檔

fig = plt.figure()
# 在Python中, 我們可以使用enumerate(), 它會傳回一個次序及值成組tuple的疊代:
'''
for i, color in enumerate(colors):
    print(i, '-->', color)
'''
for id, (x, y, w, h) in enumerate(ary):
    roi = dilation[y: y + h, x: x + w]
    # Image ROI (https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_core/py_basic_ops/py_basic_ops.html)
    # Region of Image (ROI)
    # Sometimes, you will have to play with certain region of images. For eye detection in images, first face detection is done all over the image 
    # and when face is obtained, we select the face region alone and search for eyes inside it instead of searching whole image. It improves accuracy 
    # (because eyes are always on faces :D ) and performance (because we search for a small area)
    # ROI is again obtained using Numpy indexing. Here I am selecting the ball and copying it to another region in the image:    
    '''
    ball = img[280:340, 330:390]
    img[273:333, 100:160] = ball
    Output: Check the results (roi.jpg)
    '''
    thresh = roi.copy()
    a = fig.add_subplot(1, len(ary), id + 1) 
    # 1個figure分成多個小子圖(plot)
    # Either a 3-digit integer or three separate integers describing the position of the subplot. 
    # add_subplot(nrows, ncols, index)
    # 前兩位號碼是用來分別指定上下、左右 各要畫幾張圖，而最後一位數就是接下來的圖是第幾號圖
    '''
    畫圖1的時候:
    subplot(231)
    plt.plot(x1,y1)
    
    畫圖2的時候:
    subplot(232)
    plot.plot(x2,y2)
    '''

    '''
    fig.add_subplot(111)

    # equivalent but more general
    fig.add_subplot(1, 1, 1)

    # add subplot with red background
    fig.add_subplot(212, facecolor='r')

    # add a polar subplot
    fig.add_subplot(111, projection='polar')

    # add Subplot instance sub
    fig.add_subplot(sub)
    '''

    # resize image
    res = cv2.resize(thresh, (50, 50))
    # store file in disk folder
    # cv2.imwrite(filename, img[, params])
    # outfile = '%s/%s.jpg' % (self.tgtdir, self.basename)
    cv2.imwrite('%d.png'%(id), res)
    plt.imshow(res)
    # plt.show()

'''
使用pytesser 做圖片辨識，但是發現效果不佳，因此我們用Word建立基準圖片後，使用簡單的Mean Square Error公式計算兩張圖片的相似度(兩張圖片的距離為多少)，
果然簡單的最好，輕輕鬆鬆破解惱人的驗證碼。
'''
# 取出A-Z的序列
import string
d = dict.fromkeys(string.ascii_uppercase, 0) # https://docs.python.org/2/library/string.html
a = [i for i in d.keys()] # List 串列
a.sort()
for i in a:
    print(i,)

pic0 = cv2.imread('0.png')
pic1 = cv2.imread('1.png')
pic2 = cv2.imread('2.png')
pic3 = cv2.imread('3.png')
pic4 = cv2.imread('4.png')

def mse(imageA, imageB):
    err = np.sum((imageA.astype('float') - imageB.astype('float')) ** 2) # Python has an exponentiation operator using the double stars "**"
    err /= float(imageA.shape[0] * imageA.shape[1])
    return err

print(mse(pic0, pic3)) # get a number to indicate the distance between two images, 數字越小越類似
print(mse(pic2, pic3)) # get a number to indicate the distance between two images, 數字越小越類似

import os

def getNumber(pic):
    min_a = 9999999999
    min_png = None # min_png is None
    min_png_name = None
    for png in os.listdir('alphabet'):
        ref = cv2.imread('alphabet/' + png)
        if mse(ref, pic) < min_a:
            min_a = mse(ref, pic)
            min_png = png
            # Getting the name of the file without the extension
            min_png_name = os.path.splitext('alphabet/' + png)[0]
            # What if the filename contains multiple dots:
            # if there are multiple dots, splitext splits at the last one (so splitext('kitty.jpg.zip') gives ('kitty.jpg', '.zip'))
    return min_png_name, min_png, min_a

print(getNumber(pic4))

# we use pandas to produce a beautiful table or excel (.xlsx, .csv, ..)
'''
先介紹一下Pandas是什麼，簡單來說就是把Excel的表格觀念丟到Python來，你在Excel所有的操作都可以透過Pandas的函式做簡單的處理，像是欄位的加總、分群、樞紐分析表、小計、畫折線圖、
圓餅圖等等… 在你學會Pandas這些處理的技巧之後，加上一點程式的概念，以後就可以利用程式取代Excel做到許多自動化script的處理（比如說你可以用pandas做完資料處理，畫完圖之後，利用
python撰寫Email小程式，再搭配一些定時的排程工具（像是linux的cron job）將圖表以及csv檔每天固定時間寄給你想要的人，無形之中你每天就可以省下許多時間，提升工作效率），另外就我
自己的經驗，當你學會使用Python＋Pandas之後會覺得這樣的方式比起去寫Excel的巨集方便多了。

Pandas主要有兩大資料結構：
  Series 欄位(一維度)
  DataFrame 表格(二維度)
  1.Series：用來處理時間序列相關的資料(如感測器資料等)，主要為建立索引的一維陣列。
  2.DataFrame：用來處理結構化(Table like)的資料，有列索引與欄標籤的二維資料集，例如關聯式資料庫、CSV 等等
'''

# 讀取 CSV File
import pandas as pd
df = pd.read_csv('shop_list.csv')
print(df)

# 讀取 HTML
import pandas as pd
dfs = pd.read_html('http://rate.bot.com.tw/xrt?Lang=zh-TW')
type(dfs) #list
len(dfs) #1
dfs[0]

dfs.to_csv('stockData.csv')
