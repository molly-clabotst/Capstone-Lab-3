from unittest import TestCase
import camelCase

class TestCamelCase(TestCase):
    def test_camelcase_sentence(self):
        #arrange
        
        #action

        #assert
        self.assertEqual('helloWorld', camelCase.camel_case('Hello World'))
        self.assertEqual('', camelCase.camel_case(''))
        self.assertEqual('helloWorld', camelCase.camel_case('   Hello   World   '))
        self.assertEqual('🙂🙂', camelCase.camel_case('🙂 	🙂'))