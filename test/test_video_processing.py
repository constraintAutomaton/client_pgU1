import sys
import os
sys.path.append(os.path.join('..','pgU1_client','video_processing'))
from videoProcessing import VideoProcessing


os.chdir(os.path.join('..','pgU1_client','video_processing'))

test_video = VideoProcessing()
test_video.camera_config()
test_video.run_camera_debug()