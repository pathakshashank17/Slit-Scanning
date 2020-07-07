from PIL import Image
import glob, os

# Extracting the frames
for invideo in glob.glob("video\*"):
    os.system('ffmpeg.exe -i ' + invideo +' -filter:v "crop=2:1080:960:1" -q:v 1 temp/images-%04d.jpeg')

print("frames extracted")

# Using glob to add the path to all frames
imgArr = glob.glob("temp\*.jpeg")

# Specifying result image size
imgSize = (len(imgArr), 1080)
result = Image.new("RGB", imgSize)
currentPixelCol = 0

for filePath in imgArr:
    file, ext = os.path.splitext(filePath)
    img = Image.open(filePath)
    ## Extracting a 1 x 1080 strip from the frame
    im_strip = img.crop((0, 0, 1, 1080))
    ## Pasting the strip into result image
    result.paste(im_strip, (currentPixelCol, 0))
    currentPixelCol += 1
    img.close()
    ## Deleting the strip
    os.remove(filePath)
    print(file)

result.save("result/unwrapped.jpeg", "JPEG")

print("done")