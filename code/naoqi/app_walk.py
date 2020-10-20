from naoqi import ALProxy


motion = ALProxy("ALMotion", "nao.local", 9559)
motion.setStiffnesses("Body", 1.0)
motion.moveInit()
motion.moveTo(0.5, 0, 0)
