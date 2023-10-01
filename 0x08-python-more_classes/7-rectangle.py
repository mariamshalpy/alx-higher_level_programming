#!/usr/bin/python3

"""Defines rectangle class"""


class Rectangle:
    """
    Class that defines properties

    Attributes:
        width (int): width
        height (int): height
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):

        """Creates new instances

        Args:
            width (int, optional): width
            height (int, optional): height
        """

        self.height = height
        self.width = width
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Width getter

        Returns:
            int: the width
        """

        return self.__width

    @property
    def height(self):
        """Height getter

        Returns:
            int: the height
        """

        return self.__height

    @width.setter
    def width(self, value):
        """ setter for width

        Args:

            value (int): width

        Raises:
            TypeError: if width  not an integer.
            ValueError: if width < 0.
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:

            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """setter for height

        Args:
            value (int): height

        Raises:
            TypeError: if height  not an integer.
            ValueError: if height < than 0.
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:

            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):

        """Calculates area

        Returns:
            int: area.
        """

        return self.__height * self.__width

    def perimeter(self):
        """Calculates perimeter

        Returns:
            int: perimeter.
        """
        if self.__height == 0 or self.width == 0:
            return 0

        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):

        """Prints with the character # .

        Returns:
            str: rectangle
        """

        rectangle = []

        if self.__width == 0 or self.__height == 0:
            return ""

        for i in range(self.__height):

            for j in range(self.__width):

                rectangle.append(str(self.print_symbol))
            rectangle.append("\n")

        # remove blank line
        rectangle.pop()

        return "".join(rectangle)

    def __repr__(self):
        """Returns a string

        Returns:
            str: rectangle
        """

        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):

        """Deletes instances
        """
        print("{:s}".format("Bye rectangle..."))
        type(self).number_of_instances -= 1
