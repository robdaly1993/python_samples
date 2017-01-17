available = "banana split;hot fudge;cherry;malted;black and white"

sundaes = available.split(';')
menu = "Our available flavors are: {}."

display_menu = ", ".join(sundaes)

menu.format(display_menu)

print(menu.format(display_menu))

