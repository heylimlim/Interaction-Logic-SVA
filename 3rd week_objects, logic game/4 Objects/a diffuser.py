
# Diffuser

myDiffuser = {
  "color": "white",
  "material": "plastic",
  "functions":["diffuse", "fragrantMist", "light"]
}

humidity = raw_input("What is the humidity in your room?")

if humidity < 30:
	print ("It's like a DESERT! Turn on the Diffuser with high mist")

elif humidity >= 30 or humidity < 70:
	print ("It's dry. Turn on the Diffuser with low mist")

else:
	print ("Enjoy the fragrance of Mist or light mode")

