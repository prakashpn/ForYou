import random
import string


def randomString(lengthOfString):
    # lengthOfString = 10
    res = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase +
                                 string.digits, k=lengthOfString))
    return res

# print(randomString())
