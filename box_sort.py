# Author: Van Huynh
# GitHub username: huynhvan126
# Date: 10/23/2024
# Description: write a Box class that init method takes three parameters and uses them to initialize the private length, width and height data members of a Box
class Box:
    def __init__(self, length, width, height):
        """
        Initialize a box with given length and width and height.
        """
        self._length = length
        self._width = width
        self._height = height

    def volume(self):
        """
        Calculate the volume of the box.
        """

    def get_length(self):
        """
        Get the length of the box.
        """
        return self._length

    def get_width(self):
        """
        Get the width of the box.
        """
        return self._width

    def get_height(self):
        """
        Get the height of the box.
        """
        return self._height

def box_sort(box_list):
    """
    Sort the box list in ascending order.
    """
    for i in range(1, len(box_list)):
        current_box = box_list[i]
        current_volume = current_box.volume()
        j = i - 1
        box_list[j +1] = current_box