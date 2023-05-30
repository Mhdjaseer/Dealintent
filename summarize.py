import whisper
from ytb_vdio_to_adio_dwn import Youtube_audio


# calling the youtube audio download function from ytb_vdio_to adio_dwn file
name_of_file=Youtube_audio()


def Transcribe():
    model = whisper.load_model("base")
    result = model.transcribe("audio.mp3")
    # print(result["text"])
    result_text = result["text"]
    output_file = "Transcribe_txt_file/Transcribe.txt"
    with open(output_file, "w") as file:
        file.write(result_text)
    # print("Transcription saved in", output_file)


