"""
To solve Caesar cyphers
"""

# Cypher text to decrypt
cText = "d3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrXzg2a2wzMmsyfQ"
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


for offset in range (1, 26):
    pText = ""
    print(f"\n \nOffset of {offset}")
    for letter in cText:
        try: 
            letter = letter.lower()
            index = alphabet.index(letter)
            index = (index+offset) % 26
            pText+=alphabet[index]
        except ValueError:
            pText+=letter
   
    print(pText)