import random
bingolist = [
'Surreal',
'Not surreal, but include surreal characters',
'Pepe',
'Nobody:',
'South Park',
'Advice Animal',
'Anime',
'I\'m about to end this man\'s whole career',
'Niche meme format',
'Skyrim',
'Rage comic characters',
'Thanos',
'Marvel',
'Internet influencer/celebrity',
'Straight from Vine',
'Popular from September, 2019 onward',
'Star Wars',
'JoJo reference',
'Smash Brothers',
'Quantum Dreams games',
'Image macro',
'Gender stereotype',
'Keanu Reeves',
'Drake',
'Inclusion of baby',
'Donald Trump',
'>= 4 panels, exclude pure text',
'Bee movie',
'Emoji movie',
'Shrek',
'Wrong punchline',
'Monster Inc.',
'Lack of image',
'Focus person is black',
'Soviet Union/Russia',
'Ricardo',
'Pokemon',
'Big brain/Galaxy brain',
'Meme that reads like a manga',
'YTP',
'Spiderman',
'Cat',
'Dog',
'Non-Human animal IRL',
'Toy Story',
'Disney',
'Reactions(Drake,Galaxy Brain, etc.)',
'Roblox',
'Minecraft',
'Fortnite',
'EA',
'Low hanging fruit',
'Looks like one format, but is actually another',
'Dank meme',
'New format',
'Reiteration of known format',
'Bryan Dechart',
'Improper grammar',
'Spongebob',
'Despicable Me',
'TikTok',
'Refer to real world countries',
'Bone hurting juice']

seed = input('Please enter the seed for the generator(Input nothing for random seed):\n')
if seed == '':
	random.seed()
	seed = random.randrange(0xffffffff)
else:
	if seed.isdigit():
		seed = int(seed)
random.seed(seed)

meme_table = open("meme_bingo_" + str(seed) + ".html","w+")
meme_table.write("""<!DOCTYPE html>
<html>
<head>
<style>
table, th, td {
  border: 1px solid black;
}
table{
  table-layout: fixed;
  width: 100%;
}
td{
  text-align: center;
  height: 100px;
}
</style>
</head>
<body>
\t<h1>Meme Bingo!</h1>
\t<table>
""")
for i in range(5):
	meme_table.write("\t\t<tr>\n")
	for j in range(5):
		if i == 2 and j == 2:
			meme_table.write("\t\t\t<td bgcolor=\"#ffff00\"><input type=\"checkbox\" checked>")
		elif (i + j) % 2 == 0:
			meme_table.write("\t\t\t<td bgcolor=\"#c0c0c0\"><input type=\"checkbox\">")
		else:
			meme_table.write("\t\t\t<td bgcolor=\"#ffffff\"><input type=\"checkbox\">")
		if i == 2 and j == 2:
			meme_table.write('Free Space')
		else:
			choice = random.randrange(len(bingolist))
			meme_table.write(bingolist[choice])
			bingolist.pop(choice)
		meme_table.write("</td>\n")
	meme_table.write("\t\t</tr>\n")
meme_table.write("""\t</table>
</body>
</html>""")
meme_table.close()