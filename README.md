# Voice-Activation-For-Shell

This is basically what it sounds like.  It is Voice activation for terminal in ubuntu, and soon microsoft command prompt/Bash.

# How to install everything

I used the following link below for everything:

https://realpython.com/python-speech-recognition/

The link will help you get an understanding on how the speech recognition will work.  As for what to download for python; you will need to download the following (Ubuntu):

  $ pip install SpeechRecognition
  
  $ sudo apt-get install python-pyaudio python3-pyaudio
  
  $ pip install google-cloud-speech
  
Those should work for everythin you need at the moment.  I believe you only get 50 API calls per 24hrs as we'll so don't go too wild with it.  If you the following installed and the code ready in python, just run output.py and say you're command.  Then watch the magic happen. 
  

# How it works

  It uses a google speech recognition api to hear the commands.  You will want to run output.py in any python IDE of your choice.  It will only listen to one command at a time (I will fix that, of course, as I have more time to work on it) but it will wait for you to say a command.  When you say a command such as "list everything in my current directory", it will listen to basic key words and then type the command based on that.  
  For the example, it will hear "list" and ignore the other words and type out the command "ls" in the terminal.  Then, voila!  It will show a list of everything in the current directory.  Of course, since this is only run in python at the moment, it will type into the python shell "os.system('ls')" to list evertyhing and "os.system('pwd')" to show the current direcory you are in.

# Goals/Milestones

 • Incorporate linux files and permissions
 
 • Run the python code and show the results in the terminal
 
 • Job scheduling
 
 • If I really have a lot of time: Firewalls, Network Management, Remote Access...
 
# Shoutouts

I would like to thank David Amos (author of the website link earlier) for explaining how to install the everything.  Also for providing a large chunk of code for implementing speech recognition.
