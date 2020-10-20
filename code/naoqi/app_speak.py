from naoqi import ALProxy


tts = ALProxy("ALTextToSpeech", "nao.local", 9559)
tts.say("Hello, world!")
