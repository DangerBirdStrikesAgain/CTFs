"""
Given a string, print in the desired positions
"""

cText = "rs␣r␣enigm␣␣aierhe␣i␣gluucsclhetersnti␣a␣rla␣t␣riayrgpetai␣diu␣Fawhiho}sipatfy␣ihr␣a␣rfa␣pes␣etohwrea␣octtonee␣eihetTpxcdeghi␣ro␣ped␣yGaledemXToneepetlhtseghectnatanst␣ripctiharaics␣foarscee␣ebrn␣te␣doemrr␣c__ltcsaicsa␣coo␣wbrn␣␣aranmeibti,haarhra,sipklti␣ci.ctst␣a␣lxtcnaenlkLeoakelXpohry␣patakrntd␣cilxsU␣inehe␣cwthers␣rpo␣narahhtr␣aienlsrtrr␣o.{rd___nXnti␣␣ornrtoyrgoors␣te.ksip␣␣crs␣␣c␣pohelhgctn␣ie␣erntatecg␣teeeAsuvesuX"


# Prime factorisation 2, 3, 71 (write the best algorithm for this)
width = 6
depth = 71

# Write in rows
"""
for x in range (d):
    temp = cText[(d*x):(d*x+w)]
    for letter in temp:
        print(letter, end = " ")
    print("   ")

    """
# Write in columns
"""
for d in range (depth):
    for w in range (width):
        
        letter = cText[]
        print(letter, end = " ")
    print("   ")
"""


#first row
for d in range(depth):
    print(cText[(d*depth)+w], end="  ")
    