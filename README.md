<h1 align="center">Welcome to Video Batch Cutter 👋</h1>


> Cut videos with multiple timestamps using ffmpeg and python

## Install

```sh
git clone https://github.com/ericksantos12/ffmpeg-cropper.git

cd ffmpeg-cropper

pip install -r requirements.txt
```

## Usage
Create a `cuts.csv` file in source directory and add title, start, and end timestamps in the following format separated by commas, line by line for the respective cuts:

```
filename,start_timestamp,end_timestamp
```
### Example
```
video1.mp4,00:00:01,00:02:00
video2.mp4,00:02:01,00:03:00
```
**Important:** do not forget the file format in the title, it needs to correspond to the original file format

After that you can execute the script
```sh
python app.py
```
After being prompted with the menu, just follow the instructions in terminal

## Author

👤 **Erick Santos**

* Website: https://ericksantos12.neocities.org
* Twitter: [@ErickSantosS12](https://twitter.com/ErickSantosS12)
* Github: [@ericksantos12](https://github.com/ericksantos12)

## Show your support

Give a ⭐️ if this project helped you!

***
_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_