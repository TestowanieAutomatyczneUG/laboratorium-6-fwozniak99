from string import ascii_letters, digits
import string


class Password():
    def ValidPassword(self, password):
        lettersNum = 0
        if len(password) < 10:
            return False
        else:
            if set(password).difference(ascii_letters + digits):
                if set(password).difference(ascii_letters + string.punctuation):
                    for letter in password:
                        if letter not in digits+string.punctuation:
                            lettersNum = lettersNum + 1
                    if lettersNum>=8:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False

if __name__ == "__main__":
    import doctest
    doctest.testmod()