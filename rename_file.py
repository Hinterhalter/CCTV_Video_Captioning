import sys
from os import rename, listdir
# 현재 위치의 파일 목록
files = listdir('/home/pirl/video_cap/Video2Description/VideoDataset/videos')
maindir = "/home/pirl/video_cap/Video2Description/VideoDataset/videos/"

# "video4123.mp4 파일 형식을 video를 제거하고 4123.mp4 형식으로 변경함"

for name in files:
    if name[0:5] == 'video':

        rename(maindir+name, maindir+name[5:])
        print("{0} --> {1}".format(name, name[5:]))
