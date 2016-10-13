from PIL import Image


catIm = Image.open('zophie.png')
catCopyIm = catIm.copy()
faceIm = catIm.crop((335, 345, 565, 560))
catCopyIm.paste(faceIm, (0, 0))
catCopyIm.paste(faceIm, (400, 500))
catCopyIm.save('pasted.png')


catImWidth, catImHeight = catIm.size
faceImWidth, faceImHeight = faceIm.size
catCopyTwo = catIm.copy()
for left in range(0, catImWidth, faceImWidth):
    for top in range(0, catImHeight, faceImHeight):
        print(left, top)
        catCopyTwo.paste(faceIm, (left, top))
catCopyTwo.save('tiled.png')       


quartersizedIm = catIm.resize((int(catImWidth / 2), int(catImHeight / 2)))
quartersizedIm.save('quartersized.png')
svelteIm = catIm.resize((catImWidth, catImHeight + 300))
svelteIm.save('svelte.png')


catIm.rotate(90).save('rotated90.png')
catIm.rotate(180).save('rotated180.png')
catIm.rotate(270).save('rotated270.png')


catIm.rotate(6).save('rotated6.png')
catIm.rotate(6, expand=True).save('rotated6_expanded.png')


catIm.rotate(270, expand=True).save('rotated270_expanded.png')
catIm.rotate(90, expand=True).save('rotated90_expanded.png')


catIm.transpose(Image.FLIP_LEFT_RIGHT).save('horizontal_flip.png')
catIm.transpose(Image.FLIP_TOP_BOTTOM).save('vertical_flip.png')



def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

print('415-555-4242 is a phone number:')
print(isPhoneNumber('415-555-4242'))
print('Moshi moshi is a phone number:')
print(isPhoneNumber('Moshi moshi'))


message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
print('Done')


