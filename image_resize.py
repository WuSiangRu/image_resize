import cv2
import os

def main():
    img_w=416
    img_h=416
    img_org_path='D:/org/'
    img_con_path='D:/con_picture/'
    img_list=os.listdir(img_org_path)

    if not os.path.exists(img_con_path):
        os.makedirs(img_con_path)
    i=0
    for file in img_list:
        i=i+1
        img = cv2.imread(img_org_path+file)
        res = cv2.resize(img, (img_w, img_h), interpolation=cv2.INTER_AREA)
        cv2.imwrite(img_con_path+str(i).zfill(3)+'.jpg',res)

    print("Done~~")
if __name__=='__main__':
    main()