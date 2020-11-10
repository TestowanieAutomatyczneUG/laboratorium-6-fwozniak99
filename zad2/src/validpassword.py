from string import ascii_letters, digits
import string


class Password():
    """Check if given password is correct
    >>> c = Password()
    >>> c.ValidPassword("abc")
    False
    >>> c.ValidPassword("Password9$")
    True
    >>> c.ValidPassword("Password99")
    False
    >>> c.ValidPassword("Password&&")
    False
    >>> c.ValidPassword("Passw667&&")
    False
    >>> c.ValidPassword("password9$")
    False
    >>> c.ValidPassword(99)
    Traceback (most recent call last):
      File "C:/Users/filip/OneDrive/Pulpit/GITTEST/laboratorium-6-fwozniak99/zad2/src/validpassword.py", line 54, in <module>
        c.ValidPassword(99)
      File "C:/Users/filip/OneDrive/Pulpit/GITTEST/laboratorium-6-fwozniak99/zad2/src/validpassword.py", line 26, in ValidPassword
        raise TypeError("Must be a string")
    TypeError: Must be a string
    """
    def ValidPassword(self, password):
        lettersNum = 0
        upperLettersNum = 0
        if type(password) != str:
            raise TypeError("Must be a string")
        if len(password) < 10:
            return False
        else:
            if set(password).difference(ascii_letters + digits):
                if set(password).difference(ascii_letters + string.punctuation):
                    for letter in password:
                        if letter not in digits+string.punctuation:
                            lettersNum = lettersNum + 1
                    if lettersNum>=8:
                        for letter2 in password:
                            if letter2.isupper():
                                upperLettersNum = upperLettersNum + 1
                        if upperLettersNum >= 1:
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False

if __name__ == "__main__":
    import doctest
    doctest.testmod()