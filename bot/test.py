import requests

words = ['привет', 'пока', 'дурак', '7', 'вещь', 'anglish']

while True:
	word = input("введите слово: ")
	if word in words:
		print(word)
		continue
	sim = []
	for i in words:
		url = 'https://rusvectores.org/araneum_none_fasttextcbow_300_5_2018/' + word + '__' + i + '/api/similarity/'
		r = requests.get(url).content.decode().split("\t")[0]
		sim.append(r)
	resu = words[sim.index(max(sim))]