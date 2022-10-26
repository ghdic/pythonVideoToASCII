# PythonVideoToASCII
convert video frame to ascii from youtube videos

## result video


## environment

you need to install opencv

* MacOS Ventura 13.0
* python 3.11.0
* numpy 1.23.4
* pillow 9.2.0
* opencv-python 4.5.5.62
* pytube 12.1.0
* pyobjc 8.5.1
* playsound 1.3.0

## setting
1. install python and set environment

2. install dependency package

```commandline
pip install -r requirements.txt
```


## run
execute command from your terminal(not pycharm run)

```commandline
python main.py
```

and enter the youtube video url you want

## custom
you can change `settings.json`

```json
{
  "ASCII_CHARS" : ["#", "?", "%", ".", "S", "+", ".", "*", ":", ",", "@", "="],
  "OUTPUT_WIDTH" : 50,
  "DETAIL_PRIORITY" : 20,
  "FRAME": 22
}
```

* ASCII_CHARS : candidate to be converted, you can add any character
* OUTPUT_WIDTH : output width you terminal, height will resize image ratio
* DETAIL_PRIORITY : the smaller it is, the more detailed(max 255)
* FRAME : playing video frame. since the speed of each computer is different, if the sound and video do not match, adjust