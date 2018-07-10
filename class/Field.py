from string import punctuation

class Robot:
    population = 0

    def __init__(self, name):
        '''Initializes the data'''
        self.name = name
        print('(Initialize {0})'.format(self.name))

        Robot.population += 1

    def __del__(self):
        '''I am dying.'''

        Robot.population -= 1
        print('{0} is destroyed!'.format(self.name))

        if Robot.population == 0:
            print('{0} was the last one.'.format(self.name))
        else:
            print('There are still {0:d} robots working'.format(Robot.population))

    def greet(self):
        '''Greeting by the robot

        Yeah, they can do that.'''
        print('Greetings, my master call me [0]'.format(self.name))

    @staticmethod
    def howMany():
        '''Print the current population of robot.'''
        print('We have {0:d} robots'.format(Robot.population))

robot_1 = Robot('R2-D2')
robot_1.greet()
Robot.howMany()

robot_2 = Robot('C-3P0')
robot_2.greet()
Robot.howMany()

del robot_1
del robot_2