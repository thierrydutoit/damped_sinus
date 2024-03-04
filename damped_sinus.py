import streamlit as st
from numpy import *
from matplotlib.pyplot import *
import soundfile
import io

def st_audio(signal, samplerate=44100):
    byte_io = io.BytesIO()
    soundfile.write(byte_io, signal, samplerate, subtype='FLOAT', format='WAV')
    st.audio(byte_io)

st.title('My first damped sine wave')
st.markdown('''How does the time constant of a damped sine wave influence 
            its shape and sound? Let us try...''')
   
tau=st.slider('Time constant $tau$ [s]', 0.01, 1.0, 0.2) 

f=100;
fe=10000;
t=arange(0.0,1,1/fe) 
signal=multiply(sin(2*pi*f*t),exp(-t/tau))

fig,ax = subplots(figsize=(10,4))
title('$\sin(2 \pi 100 t) \ exp(-t/tau)$') 
xlim(0,1); ylim(-1, 1)
plot(t,signal)
grid()
plot([0,tau],[1,0])
xlabel('Time (seconds)')   
st.pyplot(fig)

st_audio(signal,fe)

with st.expander("Open for comments"):
   st.markdown('''Damping signal $f$ is defined as:''')
   st.latex(''' f_d(t) = f(t) \exp(-t/tau)''') 
   st.markdown('''Its time constant $tau$ is such that:''')
   st.latex('''f_d(t) = 0 \ for \ t> 5 \ tau''')
   st.markdown('''ant that:''')
   st.latex('''f_d'(t=0) = -1 / \ tau''')
   st.markdown('''This means that the tangent at $t=0$ is as shown in orange on the plot''')
    
