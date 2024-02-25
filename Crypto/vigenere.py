"""
To solve Vigenere cyphers
"""

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
pText = ""

# Cypher text to decrypt
cText = "rgnoDVD{O0NU_WQ3_G1G3O3T3_A1AH3S_cc82272b}"


# key
key = "cylab"
usefulKey=[]

for l in key:
    usefulKey.append(alphabet.index(l))
print(usefulKey)


count = 0
for letter in cText:
    try: 
        letter = letter.lower()
        index = alphabet.index(letter)
        offset = usefulKey[count % len(usefulKey)]
        index = (index-offset) % 26
        pText+=alphabet[index]
        count+=1
    except ValueError:
        pText+=letter

print(pText)