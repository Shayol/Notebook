import datetime

class Record:

	def __init__(self, text):
		self.text = text
		self.date = str(datetime.datetime.now())

	def __repr__(self):
		return("\033[1;31;40m {} \033[0m {} \n".format(self.date[:19], self.text))
