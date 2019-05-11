import time


class ProgressBar(object):

	def __init__(self, iterations):
		self.iterations = iterations
		self.currentProgress = 0
		self.arrowLength = 30
		self.printOnNextUpdate = ''
		self._startTime = time.time()
		self._lastPrintTime = self._startTime
		self._minTimeBetweenPrints = 1
		st = '%%%dd' % len(str(iterations))
		self.__progN__ = '%s / %s' % (st, st % iterations)

	def update(self, progress = None, text = ''):
		if progress == None:
			self.currentProgress += 1
			progress = self.currentProgress
		else:
			self.currentProgress = progress
		self._printCurrentProgress(text = text)

	def reset(self, newNbrIter = None):
		self._startTime = time.time()
		self.currentProgress = 0
		if newNbrIter != None:
			self.iterations = newNbrIter

	def __time_to_string(self, elapsedTime):
		hours = int(elapsedTime/3600)
		minuites = int(elapsedTime / 60 - 60 * hours)
		seconds = int(elapsedTime - 60 * minuites - 3600 * hours)
		elapsedTime_s = ''
		if hours > 0:
			elapsedTime_s +='%i h, ' % hours
		if minuites > 0:
			elapsedTime_s +='%i min, ' % minuites
		elapsedTime_s += '%i s' % seconds
		return elapsedTime_s

	def _printCurrentProgress(self, text = ''):
		currentTime = time.time()
		if self.currentProgress == self.iterations:
			loadString = '[%s]' % ('=' * self.arrowLength)
			print(self.__progN__ % self.currentProgress, loadString)
			print('Complete! Finished in %s.' % self.__time_to_string(time.time() - self._startTime))
		elif currentTime - self._lastPrintTime < self._minTimeBetweenPrints:
			pass
		else:
			arrow = '=' * int(self.arrowLength * self.currentProgress / self.iterations) + '>'
			dots = '.' * (self.arrowLength - len(arrow))
			loadString = '[%s%s]' % (arrow, dots)
			remainingTime = (currentTime - self._startTime) * (self.iterations - self.currentProgress) / (self.currentProgress)  # remaining time in seconds
			remainingTime = self.__time_to_string(remainingTime)
			self._lastPrintTime = currentTime
			if text == '':
				text = self.printOnNextUpdate
				self.printOnNextUpdate = ''
			print(self.__progN__ % self.currentProgress, loadString, remainingTime, text)

if __name__ == '__main__':
	n = 65
	l = LoadBar(n)
	for i in range(n):
		time.sleep(1)
		l.update(i+1, 'hej')
