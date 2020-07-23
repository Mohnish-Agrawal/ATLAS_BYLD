# Voice-interactive Atlas game
We have developed a console-based game in python, implementing the classic Atlas Game. It implements voice recognition, speech to text conversion using google APIs.

## Requirements
One needs to install python 3.8 or above to run the game. The game can run on IDE or any normal shell capable of executing a file.

## List of modules/softwares required
Please make sure that you have pip/pip3 installed for easy installation of libraries
* speechRecognizer
* PyAudio
* PyDub
* gtts
* urllib
* ffmpeg

If you face any problems installing PyAudio, please check your Python version (can be checked by simply running python on terminal), click on this [link](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) and download the corresponding PyAudio file. 

Once you download it, browse to the folder containing the downloaded python file and run this command - 
`` pip install "FileName"``

## Error handling
Many may face an error reporting that the system could not find the ffmpeg or ffprod files. In this case, one can try two things:
 ### 1. Remove lines from tts2.py
 * Comment line numbers 5 - 7, they look like this:
 ```
			AudioSegment.converter = "C:\\Program Files\\ffmpeg-20200721-b5f1e05-win64-static\\bin\\ffmpeg.exe"
			AudioSegment.ffmpeg = "C:\\Program Files\\ffmpeg-20200721-b5f1e05-win64-static\\bin\\ffmpeg.exe"
			AudioSegment.ffprobe = "C:\\Program Files\\ffmpeg-20200721-b5f1e05-win64-static\\bin\\ffprobe.exe"
```	
* Restart the system, and then run atlas_script.py

### 2. Changing the browser locations
* Instead of commenting lines 5 - 7, one can also simply change the browser locations of converter, ffmpeg, ffprobe to location of ffmpeg\bin folder in his system.
* It is observed that this is much more likely to work than the first solution
* After changing the locations, the system needs to be restarted, and run again

## Running the game
Once all the modules and software has been downloaded, one can run the game by simply typing the following command in the terminal: 
```python atlas_script.py```

To play the game, we first enter our names, and then start saying names of the countries with the letter suggested by the PC. One can exit the game by saying exit instead of a place's name.

The leaderboard is displayed once the user says exit. For the best experience, we recommend you to use headphones with inbuilt-mic in it. 

			
