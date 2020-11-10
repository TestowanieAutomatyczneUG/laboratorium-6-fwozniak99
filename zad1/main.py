class FizzBuzz:
    """A Fizzbuzz game
    >>> c = FizzBuzz()
    >>> c.game(10)
    'Buzz'
    >>> c.game(3)
    'Fizz'
    >>> c.game(15)
    'FizzBuzz'
    >>> c.game(2)
    '2'
    >>> c.game(7)
    '7'
    >>> c.game(7.6)
    Traceback (most recent call last):
      File "C:/Users/filip/OneDrive/Pulpit/GITTEST/laboratorium-6-fwozniak99/zad1/main.py", line 33, in <module>
        c.game(7.6)
      File "C:/Users/filip/OneDrive/Pulpit/GITTEST/laboratorium-6-fwozniak99/zad1/main.py", line 17, in game
        raise TypeError("Must be an int")
    TypeError: Must be an int
    >>> c.game("a")
    Traceback (most recent call last):
      File "C:/Users/filip/OneDrive/Pulpit/GITTEST/laboratorium-6-fwozniak99/zad1/main.py", line 33, in <module>
        c.game("a")
      File "C:/Users/filip/OneDrive/Pulpit/GITTEST/laboratorium-6-fwozniak99/zad1/main.py", line 17, in game
        raise TypeError("Must be an int")
    TypeError: Must be an int
    >>> c.game()
    Traceback (most recent call last):
      File "C:/Users/filip/OneDrive/Pulpit/GITTEST/laboratorium-6-fwozniak99/zad1/main.py", line 47, in <module>
        c.game()
    TypeError: game() missing 1 required positional argument: 'num'
    """
    def game( self, num):
        if type(num) != int:
            raise TypeError("Must be an int")
        elif ((num % 5) == 0) and ((num % 3) != 0):
            return "Buzz"
        elif ((num % 5) != 0) and ((num % 3) == 0):
            return "Fizz"
        elif ((num % 15) == 0):
            return "FizzBuzz"
        elif num % 5 != 0 and num % 3 != 0 and type(num) == int:
            return str(num)
        else:
            raise Exception("Error in FizzBuzz")

if __name__ == '__main__':
    import doctest
    doctest.testmod()