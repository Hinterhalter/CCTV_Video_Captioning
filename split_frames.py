import shutil
import subprocess
import glob
from tqdm import tqdm
import numpy as np
import os
import argparse

import torch
from torch import nn
import torch.nn.functional as F
import pretrainedmodels
from pretrainedmodels import utils

C, H, W = 3, 224, 224

def extract_frames(video, dst):
    with open(os.devnull, "w") as ffmpeg_log:
        if os.path.exists(dst):
            print(" cleanup: " + dst + "/")
            shutil.rmtree(dst)
        os.makedirs(dst)
        video_to_frames_command = ["ffmpeg",
                                   # (optional) overwrite output file if it exists
                                   '-y',
                                   '-i', video,  # input file
                                   '-vf', "scale=400:300",  # input file
#                                    'frames:v', "40"
                                   '-qscale:v', "2",  # quality for JPEG
                                   '{0}/img_%05d.jpg'.format(dst)]
        subprocess.call(video_to_frames_command,
                        stdout=ffmpeg_log, stderr=ffmpeg_log)


dir_fc = 'UCF101_frames'
if not os.path.isdir(dir_fc):
    os.mkdir(dir_fc)
print('save video frames to %s' %(dir_fc))
video_list = glob.glob(os.path.join('./dataset/UCF101', '*.avi'))
for video in tqdm(video_list):
    video_name = video.split('/')[-1].split('.')[0][2:-8]
    video_id = video.split('/')[-1].split('.')[0]
    dst = 'dataset/UCF101_frames/'+ video_id # 추출된 프레임 경로에 폴더 생성
    extract_frames(video, dst)
