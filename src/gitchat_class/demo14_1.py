import requests
from lxml import etree
import pandas as pd
import re
url = 'http://www.baidu.com'
with requests.get(url) as res:
    status = res.status_code
    print(status)
    content = res.content
    print(content)
    html = etree.HTML(content)

from PIL import Image,ImageFilter
# im = Image.open('dog.jpg')
# im.rotate(45).show()
# im.filter(ImageFilter.CONTOUR).show()
# im.thumbnail((128,72),Image.ANTIALIAS).show()

