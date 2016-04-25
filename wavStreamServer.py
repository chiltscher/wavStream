#Server to get wav data via UDP and play it.
#Author: Christian Hiltscher
#Date 25.04.2016


#import libs
import sys;
import os;
import socket;
import pyaudio;

eol = os.linesep;

#setup variables
ip = "localhost";
port = 5000;
audioBuffer = 1024;
samples = [];

#setup udp Server
udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
udpSocket.bind((ip, port));
print("Server ist listening to "+str(ip)+":"+str(port)+eol);

#setup pyaudio stream to soundcard
audio = pyaudio.PyAudio()
device = audio.get_default_output_device_info();
channels = device["maxOutputChannels"];
sampleRate = int(device["defaultSampleRate"])
samplingWidth = 2 # this is the number of used bytes per sampleRate; 2 bytes = 16 bit
audioFormat = audio.get_format_from_width(samplingWidth)

print("Device information: ");
print("Output device: "+device["name"]);
print(str(channels)+" channels");
print(str(sampleRate)+" Hz");

stream = audio.open(format=audioFormat,
                    channels=channels,
                    rate=sampleRate,
                    output=True,
                    frames_per_buffer=audioBuffer);

def playIt():
    stream.write(data, audioBuffer);
    udpSocket.close();
    stream.stop_stream();
    stream.close();

count = 0

while True:
    data, addr = udpSocket.recvfrom(audioBuffer*4);
    if data:
        print("reciving"+str(count))
        count +=1
        ready = False;
        samples.append(data);

        ready = True;
        continue;

    if ready == True:
        print("Finally playing")
        playIt();
