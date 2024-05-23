import streamlit as st
import os
from bokeh.models.widgets import Button
from bokeh.models import CustomJS
from streamlit_bokeh_events import streamlit_bokeh_events
from PIL import Image
import time
import glob
import paho.mqtt.client as paho
import json
from gtts import gTTS
from googletrans import Translator
st.title("Tercera página")

import os
import streamlit as st
from bokeh.models.widgets import Button
from bokeh.models import CustomJS
from streamlit_bokeh_events import streamlit_bokeh_events
from PIL import Image
import time
import glob
import paho.mqtt.client as paho
import json
from gtts import gTTS
from googletrans import Translator

def on_publish(client,userdata,result):             #create function for callback
    print("el dato ha sido publicado \n")
    pass

def on_message(client, userdata, message):
    global message_received
    time.sleep(2)
    message_received=str(message.payload.decode("utf-8"))
    st.write(message_received)

broker="157.230.214.127"
port=1883
client1= paho.Client("KarolVoz2")
client1.on_message = on_message



st.title("ROOM 2")
st.subheader("CONTROL WITH VOICE")






st.write("Tap the button and speak")

stt_button = Button(label=" Inicio ", width=200)

stt_button.js_on_event("button_click", CustomJS(code="""
    var recognition = new webkitSpeechRecognition();
    recognition.continuous = true;
    recognition.interimResults = true;
 
    recognition.onresult = function (e) {
        var value = "";
        for (var i = e.resultIndex; i < e.results.length; ++i) {
            if (e.results[i].isFinal) {
                value += e.results[i][0].transcript;
            }
        }
        if ( value != "") {
            document.dispatchEvent(new CustomEvent("GET_TEXT", {detail: value}));
        }
    }
    recognition.start();
    """))

result = streamlit_bokeh_events(
    stt_button,
    events="GET_TEXT",
    key="listen",
    refresh_on_update=False,
    override_height=75,
    debounce_time=0)

if result:
    if "GET_TEXT" in result:
        st.write(result.get("GET_TEXT"))
        client1.on_publish = on_publish                            
        client1.connect(broker,port)  
        message =json.dumps({"Act2":result.get("GET_TEXT").strip()})
        ret= client1.publish("kpv_ctrl", message)

    
    try:
        os.mkdir("temp")
    except:
        pass

st.subheader("CONTROL WITH BUTTONS")

st.text("Yellow Light")

if st.button('ON'):
    act1="ON"
    client1= paho.Client("clientekp")                           
    client1.on_publish = on_publish                          
    client1.connect(broker,port)  
    message =json.dumps({"Act2":act1})
    ret= client1.publish("kp_s", message)
 
    #client1.subscribe("Sensores")
    
    
else:
    st.write('')

if st.button('OFF'):
    act1="OFF"
    client1= paho.Client("clientekp")                           
    client1.on_publish = on_publish                          
    client1.connect(broker,port)  
    message =json.dumps({"Act2":act1})
    ret= client1.publish("kp_s", message)
  
    
else:
    st.write('')

