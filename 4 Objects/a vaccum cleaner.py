# a vaccum cleaner

vacuumCleaner = {
  "size": "small",
  "color": "black",
  "inside": ["dust", "hair", "crumbs"]
}

days = raw_input("What day do you usually vacuum a room?")
days.lower()

if days != "friday":
	print("You are more industrious than usual!")
else:
	print("You are doing well")