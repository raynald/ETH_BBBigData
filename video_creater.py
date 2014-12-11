#!/usr/bin/env python
import sys

from cv2 import *

im = []

for i in range(2002,2014):
    im.append(imread(str(i)+".png"))
for i in range(2002,2014):
    im.append(imread(str(i)+"-us.png"))
for i in range(2002,2014):
    im.append(imread(str(i)+"-aus.png"))

fps = 10
#frame_size = cv.GetSize(im[0])

writer = VideoWriter("out.avi", cv.FOURCC(*tuple('MJPG')), fps, (im[0].shape[1], im[0].shape[0]))

if not writer:
    print "Error in creating video writer"
    sys.exit(1)
else:
    for i in im:
        writer.write(i)
        writer.write(i)
        writer.write(i)
        writer.write(i)
        writer.write(i)
        writer.write(i)

    destroyAllWindows()
    writer.release()

