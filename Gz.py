# Credits to Ayush Moghe
import wikipedia
import os
import pyttsx3
import ephem
import pyperclip
import webbrowser
from datetime import datetime, timedelta
import translate
import time
def speak(text):
    '''will translate the text'''
    e=pyttsx3.init()
    e.say(text)
    e.runAndWait()
def translate(from_language,to_language,text_of_translation):
    '''will translate the text'''
    from translate import Translator
    translator= Translator(from_lang=from_language ,to_lang=to_language)
    translation = translator.translate(text_of_translation)
    print (translation)
def speak_in_language(text_to_speak,language_code,name_of_file_to_save):
    '''will speak the text in required language'''
    from gtts import gTTS
    # This module is imported so that we can
    # play the converted audio
    import os
    # The text that you want to convert to audio
    mytext = text_to_speak
    # Language in which you want to convert
    language = language_code
    myobj = gTTS(text=mytext, lang=language, slow=False)
    # Saving the converted audio in a mp3 file named
    # welcome
    myobj.save(name_of_file_to_save)
    # Playing the converted file
    os.system('start '+name_of_file_to_save) 
def wikit(question):
    '''will search wikipedia for your question'''
    print(wikipedia.summary(question))
def openfile(file_name_or_location):
    os.system('start '+file_name_or_location)
def name_of_creator():
    print('Ayush Moghe')
def date_solar_eclipse():
    '''will give predecting details for solar eclipses'''
    import ephem
    from datetime import datetime, timedelta
    curtime = datetime(2020, 1, 1, 0, 0, 0)        # start time
    endtime = datetime(2100, 12, 31, 23, 59, 59)   # end time
    moon = ephem.Moon()
    sun = ephem.Sun()
    observer = ephem.Observer()
    observer.elevation = -6371000    # place observer in the center of the Earth
    observer.pressure = 0            # disable refraction
    while curtime <= endtime:
         observer.date = curtime.strftime('%Y/%m/%d %H:%M:%S')
         # computer the position of the sun and the moon with respect to the observer
         moon.compute(observer)
         sun.compute(observer)
         # calculate separation between the moon and the sun, convert
         # it from radians to degrees
         sep = abs((float(ephem.separation(moon, sun))
                    / 0.01745329252))
         # a solar eclipse happens if Sun-Earth-Moon alignment is <1.5976°.
         # this should detect all total and partial eclipses, but will
         # include some near misses.
         if sep < 1.59754941:
             print(curtime.strftime('%Y/%m/%d %H:%M:%S'), sep)
             # an eclipse cannot happen more than once in a day,
             # so we skip 24 hours when an eclipse is found
             curtime += timedelta(days = 1)
         else:
            # advance five minutes if an eclipse is not found
            curtime += timedelta(minutes = 5)
def date_lunar_eclipse():
    import ephem
    from datetime import datetime, timedelta
    '''will give predicting details for lunar eclipses'''
    currenttime = datetime(2020,1,1,0,0,0)
    endtime=datetime(2100,12,31,23,59,59)
    moon=ephem.Moon()
    sun=ephem.Sun()
    observer=ephem.Observer()
    observer.elevation= -6371000
    observer.pressure = 0
    while currenttime <= endtime:
        observer.date=currenttime
        moon.compute(observer)
        sun.compute(observer)
        sep = abs((float(ephem.separation(moon, sun))
                   / 0.01745329252) - 180)
        if sep < 0.9:
            print(currenttime.strftime('%Y/%m/%d %H:%M:%S'), sep)
            currenttime += timedelta(days = 1)
        else:
            currenttime += timedelta(hours = 1)
def copy(text_to_copy):
    '''will copy the text'''
    pyperclip.copy(text_to_copy)
def paste_text():
    '''will paste the text'''
    pyperclip.paste()
def search(search_term):
    '''will search on google'''
    new=2
    url=search_term
    webbrowser.open('https://www.google.com/search?q='+url,new)
def show_date():
    '''will show the date'''
    print(datetime.date.today())
def show_time():
    '''will show the time'''
    print(time.strftime('%H'+':'+'%M'+':'+'%S')) 
