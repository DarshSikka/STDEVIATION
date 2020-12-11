import dropbox
import time
import cv2
import random
start_time=time.time()
def upload_file(img_name):
    access_token = 'sl.AlepGXina8mmpaKNEIUCTohmPZdrw2V6rj4YWXtNk_62-zXkBnUguqEYa5Xckyh5WKutkAd2Vq7rTBJnA-rtAVqT5Xt4cWbZ5QH8o-JiOH8gNuOSMN-HDr3eW7DaRFnwMl8lfFc'
    file_from = img_name
    file_to = '/File Practice/'+img_name
    print('success')
    dbx = dropbox.Dropbox(access_token)
    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to)
        print('file uploaded')
        
def takeSnap():
    number=random.randomint(1, 100)
    video_object=cv2.VideoCapture(0)
    result=True
    print(result)
    while(result):
        ret, frame= video_object.read()
        img_name="img"+str(number)+".png"
        cv2.imwrite(img_name, frame)
        start_time=time.time()
        result=False
    return img_name
    print('snapshot taken')
def main():
    while(True):
        if((time.time()-start_time)>=300):
            name=takeSnap()
            upload_file(name)
main()