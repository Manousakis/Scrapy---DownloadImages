#coding = utf-8

import os
import PIL
from PIL import Image
import pytesseract
import glob
from PIL import ImageEnhance

os.chdir("C:/Users/Ioannis/Desktop/1/full")
file_list = glob.glob(u"*.jpg")
for file in file_list:
    image = Image.open(file).convert('L')
    enh = ImageEnhance.Contrast(image)
    image = enh.enhance(10)
    pytesseract.pytesseract.tesseract_cmd = "E:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"
    tessdata_dir_config = '--tessdata-dir "E:\\Program Files (x86)\\Tesseract-OCR\\tessdata" --outputbase nobatch digits preproc'
    width, height = image.size
    image = image.crop((3,3,width-3,height-3))
    width, height = image.size
    data = image.load()
    chop = 1
    for y in range(height):
        for x in range(width):
            # Make sure we're on a dark pixel.
            if data[x, y] > 128:
                continue
            # Keep a total of non-white contiguous pixels.
            total = 0
            # Check a sequence ranging from x to image.width.
            for c in range(x, width):
                # If the pixel is dark, add it to the total.
                if data[c, y] < 128:
                    total += 1
                # If the pixel is light, stop the sequence.
                else:
                    break
            # If the total is less than the chop, replace  with white.
            if total <= chop:
                data[x, y] = 255
            # Skip this sequence we just altered.
            x += total
    num = pytesseract.pytesseract.image_to_string(image, lang="eng",config=tessdata_dir_config).replace(",","").replace("-","").replace(".","").replace(" ","")
    if len(num) == 11:
        num = num[0:4] + num[5:11]
    if len(num) != 10:
        num = "can't recognize number properly"
    print file, num
    image.show()
