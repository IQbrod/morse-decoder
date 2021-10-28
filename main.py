import sys
sys.path.append('./dict')
from dict import *

answers = []

def decipher(answer, message):
    if (message == ""):
        #print(answer)
        answers.append(answer)
    else:
        for letter in MORSE_CODE_DICT.keys():
            if(message.startswith(MORSE_CODE_DICT[letter])):
                #print(answer+letter +"+"+ message[len(MORSE_CODE_DICT[letter]):])
                decipher(answer + letter, message[len(MORSE_CODE_DICT[letter]):])

riddle = "..-.-.---....-.--.-.-....-.-...."
decipher("", riddle)
print(answers)