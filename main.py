import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import sys
from openai import OpenAI

#  ////////////////////////////// USE GTTX FOR BETTER EXPERIENCE IN SPEAK ///////////////////////////////////////
API_KEY = "56c0ac03edcf4b4a978ec7d5e53bf810"

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiProcess(command):
    client = OpenAI(
        api_key= "sk-proj-v3VujGR8DyBDrvXIa0zGT3BlbkFJYpSZfv9EKQsR0jZuULx4",
    )

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": "You are a Vitual assistant named Jarvis skilled in general task like Alexa and   Google cloud. Give short responces please"},
            {"role": "user", "content": command}
        ]
    )
    print(completion.choices[0].message.content)

def processCommand(c):
    # print(c)
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com/")
    elif "open instagram" in c.lower():
        webbrowser.open("https://www.instagram.com/")
    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com/")
    elif "open chatgpt" in c.lower():
        webbrowser.open("https://chatgpt.com/")
    elif "close" in c.lower():
        speak("Closing the Program...")
        print("Closed")
        sys.exit(0)
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        # Define the API endpoint and your API key
        url = f'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey={API_KEY}'

        # Make the GET request to fetch the news
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            news_data = response.json()
            
            # Extract and print the articles
            articles = news_data.get('articles', [])
            for article in articles:
                speak(article['title'])
        else:
            print(f"Failed to fetch news. Status code: {response.status_code}")
    
    else:
        # Let OpenAI handle the request
        output = aiProcess(c)
        speak(output)

if __name__ == "__main__" :
    speak("Initialising Jarvis!!")
    while True:
        # listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()

        print("Recongnizing")
        # recognize speech using Sphinx
        try:
            with sr.Microphone() as source:
                print("Listening....")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word  = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("YA !!")
                # Listen for comamnd
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

            # print(command)
        except Exception as e:
            print("Error; {0}".format(e))