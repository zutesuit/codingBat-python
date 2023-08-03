# We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big bricks (5 inches each). Return True if it is possible to make the goal by choosing from the given bricks. This is a little harder than it looks and can be done without any loops. See also: Introduction to MakeBricks


def make_bricks(small, big, goal):
    big_bricks = 5 * big
    
    if small + big_bricks >= goal:
      if goal % 5 <= small:
        return True
    
    return False


