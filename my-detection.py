#!/usr/bin/env python3
#
# Copyright (c) 2019, NVIDIA CORPORATION. All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.
#

#from jetson_inference import detectNet
#from jetson_utils import videoSource, videoOutput

import jetson.inference
import jetson.utils
#import cv2

net = jetson.inference.detectNet("ssd-mobilenet-v2", threshold=0.5)
#camera = jetson.utils.videoSource("/dev/video0")      # '/dev/video0' for V4L2
camera = jetson.utils.videoSource("/home/nvidia/Desktop/0002.jpg")  
display = jetson.utils.videoOutput("display://0") # 'my_video.mp4' for file

while display.IsStreaming():
   #img = cv2.imread('/home/nvidia/Desktop/0efba00170d8bc8b.jpg')
   img = camera.Capture()
   if img is None: # capture timeout
      continue

   detections = net.Detect(img) 
   print(detections[0])
   display.Render(img)
   display.SetStatus("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))
