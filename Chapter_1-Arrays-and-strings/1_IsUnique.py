#O(N)
import unittest

def unique(string):
    if len(string) > 128:
        return False
    else:
        set_characters = [False for _ in range(128)]
        for char in string:
            if set_characters[ord(char)] is False:
               set_characters[ord(char)] = True
            else:
                return False
        return True

class Test(unittest.TestCase):
    dataT = [('abcd'), ('s4fad'), ('')]
    dataF = [('23ds2'), ('hb 627jh=j ()')]

    def test_unique(self):
        # true check
        for test_string in self.dataT:
            actual = unique(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = unique(test_string)
            self.assertFalse(actual)

if __name__ == "__main__":
    unittest.main()

