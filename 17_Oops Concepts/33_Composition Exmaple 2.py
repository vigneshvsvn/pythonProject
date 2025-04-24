
class SportsNews:
	def sportInfo(self):
		print("SportsNews News... ")
		print("Today we have IPL MI vs CSK:")
		print("Today we have IPL RCB vs KKR:")

class MovieNews:
	def movieInfo(self):
		print("MovieNews News... ")
		print("Today Good Bad Ugly released:")
		print("Today Jailer released:")

class PoliticsNews:
	def politicInfo(self):
		print("PoliticsNews News... ")
		print("ADMK aligned with BJP in TamilNadu for 2026 Election")


class News:
	def __init__(self):
		self.SportsNews=SportsNews()
		self.MovieNews=MovieNews()
		self.PoliticsNews=PoliticsNews()

	def getNews(self):
		print("Welcome to GVK TV News... ")
		self.SportsNews.sportInfo()
		self.MovieNews.movieInfo()
		self.PoliticsNews.politicInfo()

news=News()
news.getNews()		