from string import ascii_letters, digits

class Password():
    def ValidPassword(self, password):
        if len(password) < 10:
            return False
        else:
            if set(password).difference(ascii_letters + digits):
                return True
            else:
                return False


if __name__ == "__main__":
    import doctest
    doctest.testmod()