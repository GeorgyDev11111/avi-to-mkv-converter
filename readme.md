# AVI to MKV Converter

[Convert AVI to MKV without reencode with support folders](https://superuser.com/questions/1424411/convert-avi-to-mkv-without-reencode)


## Install

Clone this repo:

```bash
git clone https://github.com/GeorgyDev11111/avi-to-mkv-converter.git
cd avi-to-mkv-converter
pip install -r requirements.txt
```


## Install ffmpeg

You need install ffmpeg on your PC
https://ffmpeg.org/


## Usage

1. Run the program:

```bash
python converter.py
```

2. Enter the path to the source folder containing AVI video files and the path to the destination folder where the converted MKV files will be saved:

``` bash
Source folder: path/to/your/input_directory
Target folder: path/to/your/output_directory
```

The program will process all the video files in the specified source folder and save them in the new destination folder.

## Requirements

- Python 3 => Python 3.11
- ffmpeg (must be installed and available in PATH)
