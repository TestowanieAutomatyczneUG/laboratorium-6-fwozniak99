from string import ascii_letters, digits
import string

class Password():
    def ValidPassword(self, password):
        if len(password) < 10:
            return False
        else:
            if set(password).difference(ascii_letters + digits):
                if set(password).difference(ascii_letters + string.punctuation):
                    return True
                else:
                    return False
            else:
                return False



if __name__ == "__main__":
    import doctest
    doctest.testmod()