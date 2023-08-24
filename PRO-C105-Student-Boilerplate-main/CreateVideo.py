import os
import cv2


path = "FAMPICS"

images = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)
        
print(len(images))
count = len(images)
frame = cv2.imread(images[0]) 
height, width, channels = frame.shape 
size = (width,height)

out = cv2.VideoWriter('projectfam1.mp4',cv2.VideoWriter_fourcc(*'DIVX'), 0.10, size)
for i in range(0,count): 
    frame = cv2.imread(images[i]) 
    out.write(frame) 
out.release()
print("Done")

