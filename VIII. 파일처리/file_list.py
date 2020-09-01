#229
#텍스트 파일 : txt, html, ...
#이미지 파일 : jpg, png, jpeg, psd, ai, webp, bmp
#동영상 파일 : mp4, mpeg, mva, mov,avi, ogg


import os
data = os.listdir('..')
#print(data)
for d in data:
    print(d)
    print("is directory? : "+str(os.path.isdir(d))) #file
    print("is file? : "+str(os.path.isfile(d)))     #file