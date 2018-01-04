test = WasRun("testMethod")
print(test.wasRun)
test.testMethod()
print(test.wasRun)

class WasRun:
  def __init__(self,name):
    pass
