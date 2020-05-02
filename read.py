data = []

with open('reviews.txt', 'r') as f:
    for line in f:	
         data.append(line.strip())
         if len(data) % 1000 == 0:
         	print(len(data))


word_count = {}
for d in data:
	words = d.split(' ')
	for word in words:
		if word in word_count:
			word_count[word] += 1
		else:
			word_count[word] = 1

for word in word_count:
	if word_count[word] > 1000000:
		print(word, word_count[word])

while True:
	word = input('Please enter the word you would like to look up(enter \'q\' to quit): ')
	if word == 'q':
		break
	if word in word_count:
		print('There are',word_count[word], word, 'in the file')
	else:
		print(word, 'is not exist in the file')