import subprocess
import os

from rich.console import Console
from rich.prompt import Prompt
from rich.progress import track
from rich.panel import Panel
from rich.layout import Layout
from rich.traceback import install
install()

# progress = Progress()

# TODO implement menu()
#   TODO implement convert to mp3

OUTPUT_DIR = "./output"
console = Console()


def menu():
    pass


def ffmpeg_cut(video_path, output_path=OUTPUT_DIR):
    with open("cuts.csv") as f:
        for line in track(f.readlines(), description="Cutting..."):

            filename, start, end = line.strip().split(',')
            output_video_path = os.path.join(output_path, filename)

            if not os.path.isfile(output_video_path):
                cmd = ["ffmpeg", "-i", video_path, "-ss", start, "-to", end, "-c", "copy", output_video_path]

                subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)



            # progress.log(f"Cutting {filename} from {start} to {end}")
            subprocess.run(cmd, stdout=subprocess.DEVNULL,
                           stderr=subprocess.STDOUT)


def ffmpeg_convert_to_mp3(video_path, output_path=OUTPUT_DIR):
    pass


def main():
    while True:
        video_path = os.path.abspath(
            input("Enter the path of the video file: "))
        if os.path.isfile(video_path):
            print(
                f'[bold green]Video file found![/bold green] [blue]{os.path.basename(video_path)}[/blue]')
            break

        print('[bold red]Video file not found![/bold red]')

    if not os.path.exists(OUTPUT_DIR):
        os.mkdir(OUTPUT_DIR)
        
    ffmpeg_cut(video_path)


if __name__ == '__main__':
    main()
