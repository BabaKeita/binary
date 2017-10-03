#動画の下にある数値部分のみ抜き出し出力
#それに二値化処理を行い

import cv2
import sys
import time 
 
#cap = cv2.VideoCapture('http://zeus.info.kanazawa-it.ac.jp/~takago/movie/optflow.flv')
# cap = cv2.VideoCapture('http://www.sharp.co.jp/galileo/guide/movie/sample/sample2_c.mpg') # 学内からは無理かも
cap = cv2.VideoCapture('/home/owner/NORM2853.AVI')
 
if cap.isOpened() == False:
    print('OpenError')
    sys.exit()
cv2.namedWindow("demo", cv2.WINDOW_NORMAL)
 
while(True):
    ret, frame = cap.read()
    if ret==False:
        break
    # frame = frame[960:990, 104:2000]
    n = 19 #19 43 ←変わりやすい数値
    a=int(1+n/10);
    frame = frame[960:990, 104+38*(n-1)+a:104+38*(n-1)+a+29]
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    retval, frame = cv2.threshold(frame, 200, 255,  cv2.THRESH_BINARY) #(画像,閾値,閾値を越えた時の値,2値化の際の方法) 第二引数を200にするとある程度綺麗な黄色と黒に分れる。
    cv2.imshow('demo',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    time.sleep(1.0/30)
 
cap.release()
cv2.destroyAllWindows()
for i in range (1,5):
    cv2.waitKey(1)
