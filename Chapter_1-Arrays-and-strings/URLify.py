import unittest

def urlify(str1):
    result = []
    insert = '%20'
    for index, char in zip(range(len(str1)), list(str1)):
        if char != ' ':
            if char == str1[:-1]:
                pass
            else:
                result.append(char)
        else:
            if str1[index + 1] == ' ':
                pass
            else: result.append(insert)
    return "".join(result)

class Test(unittest.TestCase):
    '''Test Cases'''
    # Using lists because Python strings are immutable
    data = [
        ('much ado about nothing      ', 22,
         'much%20ado%20about%20nothing'),
        ('Mr John Smith    ', 13, 'Mr%20John%20Smith')]

    def URLify(self):
        for [test_string, length, expected] in self.data:
            actual = urlify(test_string,)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()



