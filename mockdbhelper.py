class MockDBHelper:
	
	def connect(self, database='crimemap'):
		pass

	def add_crime(self, category, date, latitude, longitude, description):
		# data=[category, date,latitude, longitude, description]
		# for i in data:
		# 	print i, type(i)
		pass

	def get_all_crimes(self):
		return [
		{'latitude': -1.2639045737456047,
		'longitude': 36.73707962036133,
		'date': "2000-01-01",
		'category': "mugging",
		'description': "mock description"}]

	def add_input(self, data):
		pass

	def clear_all(self):
		pass