#!/usr/bin/env python3.7
import os, sys
import random
from PIL import Image, ImageFont, ImageDraw

if(len(sys.argv) < 2):
    print("{} <width> <height>".format(sys.argv[0]))
    sys.exit(1)

w, h = int(sys.argv[1]), int(sys.argv[2])
#w, h = 2560, 1600
im = Image.new('RGB', (w, h))
draw = ImageDraw.Draw(im)
full = [(0, 0), (w, h)]
fill = (random.randint(126, 255), random.randint(126, 255), random.randint(126, 255))
font = './AdobeClean-Medium.otf'
imfont = ImageFont.truetype(font, 70)

draw.rectangle(full, fill=fill)

#for flag in os.listdir('./flags'):
flag = random.choice(os.listdir('./flags'))
name = flag[:-4]
ext = flag[-4:]
with open('joined.txt', 'r') as f:
    for line in f:
        cc = line.lower().split()[0]
        cname = ' '.join(line.split()[1:])
        if(cc == name):
            #print(flag, cc, cname)
            break
print(flag, cc, cname)
tw, th = draw.textsize(cname, font=imfont)
draw.text(((w-tw)/2, (h-th)/2-500), cname, font=imfont, fill=(0, 0, 0))
flagim = Image.open('./flags/' + flag).convert('RGBA')
flagw, flagh = flagim.size
flagim = flagim.resize((int(flagw/3), int(flagh/3)))
flagw, flagh = flagim.size
im.paste(flagim, (int((w-flagw)/2), int((h-flagh)/2)))
outname = cname.replace(' ', '_').lower() + '.png'
im.save(outname)
print('Image saved at ' + outname)
