from PIL import Image,ImageFilter,ImageDraw,ImageFont
# im = Image.open('dog.jpg')
# w,h = im.size
# print('original image size:%s*%s' %(w,h))
# im.thumbnail((w//2,h//2))
# print('resize image to : %s*%s' %(w//2,h//2))
# im.save('thumbnail.jpg','jpeg')
print('===========================')
# im = Image.open('dog.jpg')
# im2 = im.filter(ImageFilter.BLUR)
# im2.save('blur.jpg','jpeg')
print('================================')
import  random
# 随机字母:
def randchar():
    return chr(random.randint(65,90))
# 随机颜色1:
def randcolor():
    return (random.randint(64,255),random.randint(64, 255), random.randint(64, 255))
# 随机颜色2:
def randColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))
width = 60*4
height = 60
image = Image.new('RGB',(width,height),(255,255,255))
# 创建font对象
font = ImageFont.truetype('C:/Windows/Fonts/Arial.ttf', 36)
# 创建draw对象
draw = ImageDraw.Draw(image)
# 填充每个像素
for x in range(width):
    for y in range(height):
        draw.point((x,y),fill=randcolor())
# 输出文字
for t in range(4):
    draw.text((60*t+10,10),randchar(),font=font,fill=randColor2())
# 模糊
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg','jpeg')
