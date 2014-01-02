# Tested on Arch linux
# Perform pacman -S python2 pulseaudio-alsa alsa-lib alsa-utils
# Wavs go in [jenplay dir]/sounds/FINISHED/FAILURE/

import os
import json
import SocketServer
from random import choice
from subprocess import Popen, PIPE

class MyTCPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        #print self.data
        message = json.loads(self.data)
        build = message['build']
        phase = build.get('phase')
        status = build.get('status')
        self.playRndSound(phase, status)
        
        if (phase == 'FINISHED'):
            if (status == 'FAILURE'):
                self.speak(message.get('name') + ' has failed')
            if (status == 'UNSTABLE'):
                self.speak(message.get('name') + ' is unstable')

    def playRndSound(self, phase, status):
		print "Play sound"
		path = 'sounds/' + ("" if phase is None else phase) + '/' + ("" if status is None else status) + '/'
		print "path " + path
		if os.path.exists(path):
			file = choice(os.listdir(path))
			self.playSound(path + file)
		else:
			print "Invalid path: " + path

    def playSound(self, file):
        self.runCommand('aplay ' + file)
        
    def speak(self, text):
        self.runCommand('echo "' + text + '" | festival --tts')
        
    def runCommand(self, command):
        print "Running command " + command
        p = Popen(command, shell=True, stdout=PIPE, stderr=PIPE)
        out, err = p.communicate()
        print "o: " + out
        if err is not None:
            print "e: " + err

if __name__ == "__main__":
    HOST, PORT = "", 91

    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)
    server.serve_forever()
