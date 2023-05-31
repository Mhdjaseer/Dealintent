

import openai
from summarize import Transcribe


# calling the transcribe funtion to transcribe the downloaded youtube audio file 
transcribe=Transcribe()

# GPT    summarizing the text 
API_KEY=open("API_KEY.txt","r").read()
openai.api_key=API_KEY

# opening the file that Transcribe from vedio 
with open("Transcribe_txt_file/Transcribe.txt", "r") as f:
    file_contents = f.read()
# print(file_contents)

try:
    response=openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "model": "gpt-3.5-turbo",
                "messages": [{"role": "user", "content":file_contents +"find and extract business ideas from the following text, then create a compelling headline and provide a concise summary."}],
            }
        ]
    )
except:
    print("check your billing detials in GPT ")

generated_text = response.choices[0].message["content"]
# print(generated_text)

# Save the generated result to a text file
with open("generated_result.txt", "w") as output_file:
    output_file.write(generated_text)

print("Generated result saved to generated_result.txt")