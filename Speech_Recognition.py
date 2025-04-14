import streamlit as st
import speech_recognition as sr
import pyttsx3 as pt
import pywhatkit as pk
listening = sr.Recognizer()
engine = pt.init('dummy')

def speak(text):
    engine.say(text)
    engine.runAndWait()
def hear():
    cmd = None  #Initialize cmd 
    try:
        with sr.Microphone() as mic:
            st.info("listening....")
            voice = listening.listen(mic, timeout=5, phrase_time_limit=10)
            cmd = listening.recognize_google(voice)
            cmd = cmd.lower()
            if 'vaheed' in cmd:
                cmd = cmd.replace('vaheed', '').strip()
            st.success(f"Recognized: {cmd}")
    except sr.UnknownValueError:
        st.error("Speech not recognized, please try again.")
    except sr.RequestError as e:
        st.error(f"API unavailable or unnresponsive: {e}")
    except Exception as e:
        st.error(f"Error in hear() {e}")
    return cmd        

def process_command():
    cmd = hear()
    if cmd:
        if 'play' in cmd:
            song = cmd.replace('play', '').strip()
            speak('playing' + song)
            pk.playonyt('Playing...' + song)
        else:
            st.warning("No command detected")
    else:
        st.warning("Command not recognized. Please try again.")            
        
st.title("Voice Assistant Front End")
st.write("Say 'Vaheed' followed by your command. Example: 'Vaheed play Despacito")    
      
if st.button("Start Voice Assistant"):
    process_command()