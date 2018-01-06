u""" テストメソッドを動的に呼び出すクラス
nameに与えた名前のメソッドをrunメソッドで呼び出す
"""
class TestCase:
    def __init__(self,name):
        self.name = name
    def setUp(self):
        pass
    def run(self):
        self.setUp()
        method = getattr(self,self.name)
        method()
u""" テストか呼び出されたかどうかを記録するクラス

"""
class WasRun(TestCase):
    def __init__(self,name):
        self.wasRun = None
        super().__init__(name)


    def testMethod(self):
        self.wasRun = 1
    def setUp(self):
        self.wasSetUp = 1
u""" テストケースを呼び出すクラス
"""
class TestCaseTest(TestCase):
    def testRunning(self):
        test = WasRun("testMethod")
        assert(not test.wasRun)
        test.run()
        assert(test.wasRun)
    def testSetUp(self):
        test = WasRun("testMethod")
        test.run()
        assert(test.wasSetUp)

TestCaseTest("testRunning").run()
TestCaseTest("testSetUp").run()
