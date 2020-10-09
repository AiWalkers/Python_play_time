from PIL import ImageGrab
import keyboard

while True:
	try:
		if keyboard.is_pressed("c"):
			image = ImageGrab.grab()
			image.save("capture.png")
			break
		else:
			pass

	except:
		break