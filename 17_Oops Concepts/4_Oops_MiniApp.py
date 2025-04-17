class Movie:
	"""
	This Class Developed by Vignesh for Basic Understanding.
	"""
	def __init__(self,title,hero,heroine):   ## local Variable to hold data local to method.
		self.title=title               # self.title is Instance Variable
		self.hero=hero
		self.heroine=heroine

	def info(self):
		print("Movie Name:",self.title)
		print("Hero Of the Movie",self.hero)
		print("Heroine Name:",self.heroine)


m=Movie('Jailer','Rajinikanth','Thamana')

list_Movies=[]

while True:
	title=input("Enter Movie Name:")
	hero=input("Enter Hero Name:")
	heroine=input("Enter Heroine Name:")
	m=Movie(title,hero,heroine)
	list_Movies.append(m)
	print("Movie added Successfully.")

	option=input("Do you want to add one more Movie [Yes/No ?]:")
	if option.lower()=='no':
		break


print("All Movies Information....")

for each_movie in list_Movies:
	each_movie.info()
	print()


