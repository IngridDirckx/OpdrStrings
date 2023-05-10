# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
#opdracht part 1
scorer1 = "Ruud Gullit"
scorer2 = "Marco van Basten"
goal_0 = 32
goal_1 = 54
scorers = (((scorer1 + " " + str(goal_0)) + ", ") + (scorer2 + " " + str(goal_1)))
report = f"{scorer1} scored in the {goal_0}nd minute\n{scorer2} scored in the {goal_1}th minute"
print (report)


#opdracht part 2
player = "Ronald Koeman" #opdr 1 naam van een speler
first_name = player [0: player.find(" ")] # opdr 2 variabele die de voornaam van de speler heeft
print (first_name) #opdr 2 controle voornaam

#opdracht part 3 lengte van de achternaam van player
last_name_len = len(player [player.find(" ")+1:len(player)])
print (last_name_len)

# opdracht part 4 bewerking van de naam player
# voornaam zie opdracht 2
last_name_player = player [player.find(" ")+1:len(player)]# achternaam van player in een variabele zetten
name_short = f"{(first_name[0:1])}. {last_name_player}"#voor en achternaam samenvoegen
print(name_short) 

#Opdracht part 5
#firstname plus uitroepteken 
lengte_voornaam = len(first_name)
# lengte is gelijk aan het aantal herhalingen
#spatie tussen herhalingen, maar niet achter de laatste
chant = (first_name + "! ") * (lengte_voornaam -1) + (first_name + "!")
print(chant)

#opdracht part 6 controle van de laatste letter 
#isoleren van de laatste letter van variabele chant
#laatste letter vergelijken met een " " (spatie)
laatste_letter = (chant [len(chant) - 1])
good_chant = laatste_letter != " "
print (good_chant)




