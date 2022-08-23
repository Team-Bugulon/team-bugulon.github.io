#find every pictures in folders
import os
import PIL
from PIL import Image
from tkinter import filedialog

#folder dialog box
folder = filedialog.askdirectory()

#find all images in folder
for root, dirs, files in os.walk(folder):
    for file in files:
        if file.endswith(".png"):
            path = os.path.join(root, file)

            print(path)

            #remove .png from path
            path = path[:-4]

            
            #open image
            img = PIL.Image.open(path + ".png")
            #backup image

            img.save(path + "_backup.png")

            #resize image
            img = img.resize((320,256), PIL.Image.ANTIALIAS)

            #save image
            #img.save(path + ".png")
            
            #if path ends with bg
            if path.endswith("bg"):
                #delete file at path
                os.remove(path + ".png")
                #set image mode to rgb
                img = img.convert("RGB")
                img.save(path + ".jpg", quality=100)
            else:
                img.save(path + ".png")
            
            
            
