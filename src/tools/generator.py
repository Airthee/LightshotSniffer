# *-* coding: utf8


class Generator:
    CHARACTERS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self, start, end):
        self.__start = start
        self.__end = end
        self.__direction = 1 if start < end else -1
        self.__current = start

    def next(self):
        """
            Get the next string according to the direction
        """

        # Get last char of current string
        index = len(self.__current) - 1

        # Return none if current is equal to end
        if self.__current == self.__end:
            return None

        # Get next string
        while index >= 0:
            # Apply next
            currentChar = self.__current[index]
            nextIndex = (
                self.CHARACTERS.index(currentChar.upper()) + self.__direction
            ) % len(self.CHARACTERS)
            nextChar = self.CHARACTERS[nextIndex]
            self.__current = (
                self.__current[:index] + nextChar + self.__current[index + 1 :]
            )

            # If first char, increase left char
            if nextChar == self.CHARACTERS[0 if self.__direction > 0 else -1]:
                index -= 1
                continue

            # Return string
            return self.value()

    def previous(self):
        self.__direction *= -1
        previousChar = self.next()
        self.__direction *= -1
        return previousChar

    def value(self):
        return self.__current.lower()
