"""
Takes an alphabet that corresponds to our normal alphabet and performs a substitution
"""

alphabet = list('abcdefghijklmnopqrstuvwxyz')
permutation = list('aipfhrswmokqdkoulgybuntevc')
dictionary = dict(zip(alphabet, permutation))
#dictionary = dict(zip(permutation, alphabet))
plain=''

text = open('../PicoCTF/message.txt', 'r').read()
for c in text:
    if c.lower() in dictionary: 
        plain += dictionary[c.lower()].upper()
    else:
        plain += c

print(plain)