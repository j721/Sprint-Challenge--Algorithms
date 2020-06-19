class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        """
        Sort the robot's list.
        """

        #first method
        #turn on the robot's light to have the robot running
        self.set_light_on()

        #while light is on, pick up the item in front of it
        while self.light_is_on():
            self.swap_item()
            #while the robot is moving to the right with the item to be compared/swapped in hand
            while self.can_move_right():
                self.move_right()
                #compare the items. Swap if the value of the item being held is greater than the one on the list
                if self.compare_item() ==1:
                    self.swap_item()
            #move to the left if there are still items remaining to be compared
            while self.can_move_left() and self.compare_item() !=None:
                self.move_left()
            #continue with loop of swaping and comparing items, moving to the right again if the item value in hand is greater. (direction left to right)    
            self.swap_item()
            self.move_right()

            #if the robot can't move right anymore then turn light off. If there's nothing else left to compare
            if not self.can_move_right():
                self.set_light_off()
            #else keep light turned on 
            else:
                self.set_light_on()
        


        # if self.can_move_right() is False:
        #     return self._list
        
        # self.swap_item()

        # while self.can_move_right() is True:
        #     self.move_right()

        #     if self.compare_item() ==1:
        #         self.swap_item()
        
        # while self.can_move_left() is True:
        #     self.move_left()

        #     if self.compare_item() == None:
        #         self.swap_item()
        #         break
        # self.move_right()
        # self.sort()

        # while self.can_move_right():
        #     self.swap_item()

        #     while self.can_move_right():
        #         self.move_right()

        #         if self.compare_item() ==1:
        #             self.swap_item()
        
        # while self.can_move_left() and self.compare_item() !=None:
        #     self.move_left()
        
        # self.swap_item()
        # self.move_right()


      


#U
#in order for the robot to be able to sort through things, its light switched needs to be turned on
#there has to be list of things present. At least greater than 1 for the robot to sort


#the robot has to pick up the item in front of it
        #swap item function- The robot swaps its currently held item with the list item in front
                # of it.
#robot has to be compare the item when swapping
#   If the held item's value is greater, return 1.
#         If the held item's value is less, return -1.
#         If the held item's value is equal, return 0.
#         If either item is None, return None.

#after the item has been swapped then the robot is able to move in left to right direction. 
    #can_move_right =True
        #self.move right()
    #can_move_left = True
        #self.move left()


# P
#propably use of recursion and most likely calling other methods made for the robot
#going to assume that the robot moves from left to right. 
#go right to go forwards
#go left to go backwards
# E
#while light is on, the robot can pick up an item
#and robot can start by moving forwards (right)
#need to pick up item in front of robot and compare it with the other item
#the item can be swapped once the one in hand has a greater value than the one in the list
#continue this process of going right to sort through any other items that need to be swapped

#if there are any items that are remaining, then we can move to the left
    #and repeat the same process of comparing and swapping items

    #continue the loop

#to exit out of the loop- need to turn of light with a condition
#if the robot can't move right anymore, there's nothing left to compare/sort then turn light off
#else turn light on

# R#

if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)