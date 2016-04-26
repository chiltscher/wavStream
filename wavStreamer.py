#Server to get wav data via UDP and play it.
#Author: Christian Hiltscher
#Date 25.04.2016

import os;
import sys;
import wave;
import socket;

path = os.path;
eol = os.linesep;

#setup variables
PATH = path.abspath(sys.argv[2]);
print(PATH)
exists = path.exists(PATH);

if not exists:
    print("File does not exists");
    sys.exit();
print("Streaming "+str(PATH));

ip = sys.argv[1];
port = 5000;
audioBuffer = 1024;

#setup udp Socket
udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
udpSocket.sendto("nf", (ip, port));

#setup pyaudio stream to soundcard
wavFile = wave.open(PATH, 'rb');
samples = wavFile.readframes(audioBuffer);
while (len(samples) > 0):
    udpSocket.sendto(samples, (ip, port));
    samples = wavFile.readframes(audioBuffer);

udpSocket.sendto("eof", (ip, port));

wavFile.close();
udpSocket.close();
