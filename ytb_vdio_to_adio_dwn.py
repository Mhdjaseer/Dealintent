# import packages 
from pytube import YouTube
import os

#geting input from user and downloading the audio of the youtube video .. and saving the file 
def Youtube_audio():
    
    # url input from user
    yt=YouTube(str(input("Enter the URL  of the video  you want to  summarize: \n>>")))
    # extract only audio 
    video=yt.streams.filter(only_audio=True).first()
    destination='.'
    # download the file 
    out_file=video.download(output_path=destination)

    base,ext=os.path.splitext(out_file)
    new_file = os.path.join(destination, 'audio.mp3') 

    os.rename(out_file,new_file)
    print(yt.title+"has been successfully downloaded .")

    return new_file
