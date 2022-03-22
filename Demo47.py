from urllib.request import urlopen
from PIL import Image
URL = "https://www.uuu.com.tw/Public/content/edm/220301_redblue-event/images/TITLE.png"
FILE = "./images/original.png"
imageToSave = urlopen(URL)
image = Image.open(imageToSave)
image.save(FILE)