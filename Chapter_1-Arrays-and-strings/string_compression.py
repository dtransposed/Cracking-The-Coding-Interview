import unittest

def string_compression(string):
    new_string = ''
    counter = 0

    for i in range(len(string)):
        if i !=0 and string[i] != string[i-1]:
            new_string = new_string + string[i-1] + str(counter)
            counter = 0
        counter = counter + 1

    new_string = new_string + string[-1] + str(counter)
    if new_string > string:
        return string
    else:
        new_string

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('aabcccccaaa', 'a2b1c5a3'),
        ('abcdef', 'abcdef')
    ]

    def string_compression(self):
        for [test_string, expected] in self.data:
            actual = string_compression(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()