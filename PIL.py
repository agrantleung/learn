from PIL import Image
im = Image.open('test.png')
print(im.format, im.size, im.mode)
PNG(400, 300)RGB
im.thumbnail((200,100))
im.save('thumb.jpg','JPEG')
