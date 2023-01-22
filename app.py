import subprocess
import os

from rich.console import Console
from rich.prompt import Prompt
from rich.progress import track
from rich.panel import Panel
from rich.layout import Layout
from rich.traceback import install
install()


OUTPUT_DIR = "./output"
console = Console()


def menu():
    options = """Select an option:
    [blue]1[/] - Cut timestamps
    [blue]2[/] - Convert output folder to mp3
    [blue]3[/] - Do all from above
    [blue]0[/] - Exit"""

    console.print(Panel(options, title="[bold]Menu"))
    return int(console.input("[green bold]> "))


def ffmpeg_cut(video_path, output_path=OUTPUT_DIR):
    with open("cuts.csv") as f:
        for line in track(f.readlines(), description="Cutting..."):

            filename, start, end = line.strip().split(',')
            output_video_path = os.path.join(output_path, filename)

            if not os.path.isfile(output_video_path):
                cmd = ["ffmpeg", "-i", video_path, "-ss", start, "-to", end, "-c", "copy", output_video_path]

                subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)


def ffmpeg_mp4_to_mp3(output_path=OUTPUT_DIR):
    audio_path = os.path.abspath(output_path + "/mp3/")

    create_dir(audio_path)

    for filename in track(os.listdir(output_path), description="Converting..."):

        output_video_path = os.path.join(output_path, filename)
        output_audio_path = os.path.join(audio_path, filename[:-4] + ".mp3")

        if filename.endswith(".mp4") and not os.path.isfile(output_audio_path):
            cmd = ["ffmpeg", "-i", output_video_path, output_audio_path]

            subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)


def prompt_cut():
    while True:
        video_path = os.path.abspath(Prompt.ask("Enter the path of the video file"))
        if os.path.isfile(video_path):
            console.print(f'[bold green]Video file found![/bold green] [blue]{os.path.basename(video_path)}[/blue]')
            break

        console.print('[bold red]Video file not found![/bold red]')

    create_dir(OUTPUT_DIR)

    ffmpeg_cut(video_path)


def prompt_mp4_mp3():
    create_dir(OUTPUT_DIR)
    ffmpeg_mp4_to_mp3(OUTPUT_DIR)


def create_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)


def main():

    while True:
        key = menu()
        match key:
            case 1:
                prompt_cut()
            case 2:
                prompt_mp4_mp3()
            case 3:
                prompt_cut()
                prompt_mp4_mp3()
            case 0:
                exit()


if __name__ == '__main__':
    main()