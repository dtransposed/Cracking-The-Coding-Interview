#O(N)
import unittest

def oneEditAway(string1, string2):
    if len(string1) == len(string2):
        return one_edit_replace(string1, string2)

    elif len(string1) -1 == len(string2):
        return one_edit_insert(string2, string1)

    elif len(string1) +1 ==  len(string2):
        return one_edit_insert(string1, string2)
    else:
        return False

def one_edit_replace(string1, string2):
    edited = False
    for index in range(len(string1)):
        if string1[index] != string2[index]:
            if edited:
                return False
            edited = True
    return True

def one_edit_insert(string1, string2):
    edited = False
    i = 0
    j = 0
    while i < len(string1) and j < len(string2):
        if string1[i] != string2[j]:
            if edited:
                return False
            edited = True
            j = j + 1
        else:
            j = j + 1
            i = i + 1
    return True


class Test(unittest.TestCase):
    data = [
        ('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('paleabc', 'pleabc', True),
        ('pale', 'ble', False),
        ('a', 'b', True),
        ('', 'd', True),
        ('d', 'de', True),
        ('pale', 'pale', True),
        ('pale', 'ple', True),
        ('ple', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
        ('pale', 'pse', False),
        ('ples', 'pales', True),
        ('pale', 'pas', False),
        ('pas', 'pale', False),
        ('pale', 'pkle', True),
        ('pkle', 'pable', False),
        ('pal', 'palks', False),
        ('palks', 'pal', False)
    ]

    def test_one_away(self):
        for [test_s1, test_s2, expected] in self.data:
            actual = oneEditAway(test_s1, test_s2)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()







