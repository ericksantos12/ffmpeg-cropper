import subprocess
import os

def main():
    video_path = os.path.abspath(input("Enter the path of the video file: "))
    
    ffmpeg_cut(video_path)

def ffmpeg_cut(video_path, output_path = os.path.abspath('./output')):
    with open("cuts.csv") as f:
        for line in f.readlines():
            filename, start, end = line.strip().split(',')
            cmd = ["ffmpeg", "-i", video_path, "-ss", start, "-to", end, "-c", "copy", os.path.join(output_path, filename)]
            
            subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)


if __name__ == '__main__':
    main()