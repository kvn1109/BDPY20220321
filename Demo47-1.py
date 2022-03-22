from urllib.request import urlopen
from PIL import Image

URL = "https://www.uuu.com.tw/Public/content/edm/220301_redblue-event/images/TITLE.png"
FILE = "./images/original.png"
FILE2 = "./images/half.png"
FILE3 = "./images/r90.png"
FILE4 = "./images/r180.png"
FILE5 = "./images/r270.png"
imageToSave = urlopen(URL)
image = Image.open(imageToSave)
image.save(FILE)
print(image.size)
halfSize = (image.size[0] // 2, image.size[1] // 2)
halfImage = image.resize(halfSize, Image.ANTIALIAS)
halfImage.save(FILE2)
degrees = [Image.ROTATE_90, Image.ROTATE_180, Image.ROTATE_270]
files = [FILE3, FILE4, FILE5]
for file, degree in zip(files, degrees):
    t = image.transpose(degree)
    t.save(file)
image60 = image.rotate(60)
image60.save("./images/r60.png")