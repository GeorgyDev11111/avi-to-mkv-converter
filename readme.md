# AVI to MKV Converter

[Convert AVI to MKV without reencode with support folders](https://superuser.com/questions/1424411/convert-avi-to-mkv-without-reencode)


## Install


```bash
$ git clone https://github.com/GeorgyDev11111/avi-to-mkv-converter.git
$ cd avi-to-mkv-converter
$ sudo ./install.sh
```

## Uninstall

```bash
$ sudo ./uninstall.sh
```


## Install ffmpeg

You need install [ffmpeg](https://ffmpeg.org/) on your PC



## Usage

1. Run the program:

```bash
$ avi-to-mkv-converter.py
```

2. Enter the path to the source folder containing AVI video files and the path to the destination folder where the converted MKV files will be saved:

``` bash
Source folder: name_path_src
Target folder: name_path_target
```

The program will process all the video files in the specified source folder and save them in the new destination folder.

## Requirements

- Python 3 => Python 3.11
- ffmpeg (must be installed and available in PATH)
