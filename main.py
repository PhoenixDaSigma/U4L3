# Phoenix Valent
	# U4L3
		# Reverse the ***WORDS*** of a file

from StackClass import ArrayStack as stack

def getFile():
	cleanText = ""
	with open("earnest.txt", 'r') as openFile:
		text = openFile.read()
		for char in text:
			if 65 <= ord(char) <= 90 or 97 <= ord(char) <= 122 or ord(char) == 32:
				cleanText+=char

	return cleanText.split(' ')

def reverseFile(text):
	reversedThing = ""
	reverser = stack()
	for i in text:
		reverser.push(i)
		reversedThing+=(reverser.pop())
		reversedThing+=" "
	return reversedThing

def main():
	text = getFile()
	reversedText = reverseFile(text)
	print(reversedText)

if __name__ == "__main__":
	main()