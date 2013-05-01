from time import time

EPOCH = time()
SEC_PER_DAY = 86400
UNIX_YR = EPOCH / (SEC_PER_DAY * 365)
UNIX_MON = UNIX_YR * 12
UNIX_DAY = UNIX_YR * 365
UNIX_HR = UNIX_DAY * 24
UNIX_MIN = UNIX_HR * 60
UNIX_SEC = UNIX_MIN * 60


class myDateTime:
	def __init__(self, yr, mon, day, hr, mn, sec):
		self.yr = yr
		self.mon = mon
		self.day = day
		self.hr = hr
		self.mn = mn
		self.sec = sec

		assert 0 < mon <= 12, '{} is out of range'.format(mon)
		assert 0 < day <= 31, '{} is out of range'.format(day)
		assert hr <= 24, '{} is out of range'.format(hr)
		assert mn <= 59, '{} is out of range'.format(mn)
		assert sec <= 59, '{} is out of range'.format(sec)

	def __str__(self):
		if self.hr < 10:
			self.hr = '0' + str(self.hr)
		if self.mn < 10:
			self.mn = '0' + str(self.mn)
		if self.sec < 10:
			self.sec = '0' + str(self.sec)

		return '{0}, {1}, {2} {3}:{4}:{5}'.format(self.yr, self.mon, self.day, self.hr, self.mn, self.sec)

	def __add__(self, new_dt):
		pass

	def getUnix(self):
		pass

		'''
	>>> d = myDateTime(2013, 4, 30, 5, 15, 20, 12)

	>>> print d
	'2013, 4, 30, 
	'''
