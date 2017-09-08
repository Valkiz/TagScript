import TagScriptEngine
from unittest import TestCase

class test_variable_functionality(TestCase):

    def setUp(self):
        """ Sets up engine and other variables that might be needed between tests """
        self.engine = TagScriptEngine.Engine()
    def tearDown(self):
        """ Cleans the plate to make tests consistent """
        self.engine.Clear_Variables()
        self.engine = None

    # Actual tests below
    # ======

    def test_basic_variables(self):
        
        phrase = self.engine.Process("""!{player1=Kintark}\n!{player2=Carl}\n$player1 says hi to $player2""")
        self.assertEqual(phrase, "Kintark says hi to Carl")

    def test_long_variables(self):
        phrase = self.engine.Process("!{ava=and this is a long variable with spaces!} say hi to $ava")
        self.assertEqual(phrase, "say hi to and this is a long variable with spaces!")

    def test_false_variables(self):
        self.engine.Add_Variable("me", "pysnow")
        phrase = self.engine.Process("$me $notme")
        self.assertEqual(phrase, "pysnow $notme")