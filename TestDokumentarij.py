import unittest
import time
from dokumentarij import DokumentarijModel, DokumentarijView, DokumentarijController

class DokumentarijTestCase(unittest.TestCase):
	def testIfAddingNamesMakesTheListBigger(self):
		gameTest = DokumentarijController(DokumentarijModel(), DokumentarijView())
		namesList = gameTest.model.names

		initNumOfNames = len(namesList)
		gameTest.add_new_name()
		postNumOfNames = len(namesList)

		self.assertLess(initNumOfNames, postNumOfNames, "Broj studenata u dokumentariju mora biti veći nakon unosa")

if __name__ == "__main__":
	unittest.main()