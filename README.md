jenplay
=======

An audial notification server for [Jenkins](http://jenkins-ci.org/) and the [Notification Plugin](https://wiki.jenkins-ci.org/display/JENKINS/Notification+Plugin). Alerts on failures with systhansised speech and play a random sound.

Tested on Arch linux. Installation requires alsa and festival:
pacman -S python2 pulseaudio-alsa alsa-lib alsa-utils festival

Wavs can be played on failure or unstable. They should be placed in [jenplay dir]/sounds/FINISHED/FAILURE/ and [jenplay dir]/sounds/FINISHED/UNSTABLE/.