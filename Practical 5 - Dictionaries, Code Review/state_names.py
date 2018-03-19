"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
               "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
# print(STATE_NAMES)

for abbreviated_state, state in STATE_NAMES.items():
    print("{:3} - {}".format(abbreviated_state, state))

state = input("Enter short state: ").upper()
while state != "":
    if state in STATE_NAMES:
        print(state, "is", STATE_NAMES[state])
    else:
        print("Invalid short state")
    state = input("Enter short state: ").upper()

# Color codes in a Dictionary
COLOR_HEXS = {"AliceBlue": "#f0f8ff", "Cyan": "#00ffff", "DarkGreen": "#006400",
              "Gold": "#ffd700", "Green": "#00ff00", "HotPink": "#ff69b4", "LightBlue": "#bfefff",
              "Blue": "#0000cd", "Pink": "#ffc0cb", "Red": "#ff0000"}
# User inputs color name and receives code
color = input("Enter a color name: ")
while color != "":
    if color in COLOR_HEXS:
        print("{} - {}".format(color, COLOR_HEXS[color]))
    else:
        print("Invalid color")
    color = input("Enter a color name: ")

word_dict = {}
sentence = input("Text: ").lower()
split_sentence = sentence.split()
for word in split_sentence:
    if word in word_dict.keys():
        word_dict[word] += 1
    else:
        word_dict[word] = 1

word_list = [(v, k) for v, k in word_dict.items()]
# Finds length of words.
word_length_list = []
for word in word_dict.keys():
    length = len(word)
    word_length_list.append(length)
word_length_list.sort()

for pair in sorted(word_list):
    print("{:{}} : {}".format(pair[0], word_length_list[-1], pair[1]))
