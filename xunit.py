class TestCase:
	def __init__(self, name):
		self.name = name
	def setUp(self):
		pass
	def run(self,reuslt):
		result.testStarted()
		self.setUp()
		try:
			method = getattr(self, self.name)
			method()
		except:
			result.testFailed()
		self.tearDown()
	def tearDown(self):
		pass
class TestResult:
	def __init__(self):
		self.runCount = 0
		self.errorCount = 0
	def testStarted(self):
		self.runCount = self.runCount + 1
	def testFailed(self):
		self.errorCount = self.errorCount + 1

	def summary(self):
		return "%d run, %d failed" % (self.runCount, self.errorCount)

class WasRun(TestCase):
	def testMethod(self):
		self.log = self.log + "testMethod "
	def setUp(self):
		self.log = "setUp "
	def tearDown(self):
		self.log = self.log + "tearDown "
	def testBrokenMethod(self):
		raise Exception
class TestSuite:
	def __init__(self):
		self.tests = []
	def add(self, test):
		self.tests.append(test)
	def run(self,result):
		for test in  self.tests:
			test.run(result)
class TestCaseTest(TestCase):
	def testTemplateMethod(self):
		test = WasRun("testMethod")
		test.run()
		assert("setUp testMethod tearDown " == test.log)
	def testResult(self):
		test = WasRun("testMethod")
		result = test.run()
		assert("1 run, 0 failed" ==result.summary())
	def testFailedResult(self):
		test = WasRun("testBrokenMethod")
		result = test.run()
		assert("1 run, 1 failed" ==result.summary())
	def testFailedResultFormatting(self):
		result = TestResult()
		result.testStarted()
		result.testFailed()
		assert("1 run, 1 failed" == result.summary())
	def testSuite(self):
		suite = TestSuite()
		suite.add(WasRun("testMethod"))
		suite.add(WasRun("testBrokenMethod"))
		result = TestResult()
		suite.run(result)
		assert("2 run, 1 failed" == result.summary())

suite = TestSuite()
suite.add(TestCaseTest("testTemplateMethod"))
suite.add(TestCaseTest("testResult"))
suite.add(TestCaseTest("testFailedResult"))
suite.add(TestCaseTest("testFailedResultFormatting"))
suite.add(TestCaseTest("testSuite"))
result = TestResult()
suite.run(result)
print(result.summary())
