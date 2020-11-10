class Password():
    def ValidPassword(self, password):
        if len(password) < 10:
            return False

if __name__ == "__main__":
    import doctest
    doctest.testmod()