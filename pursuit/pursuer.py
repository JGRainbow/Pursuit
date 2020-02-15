from abc import ABC, abstractmethod

class Pursuer(ABC):

    _dt = 1

    def __init__(self, current_position_x, current_position_y, speed):
        self.current_position_x = current_position_x
        self.current_position_y = current_position_y
        self.speed = speed
        super().__init__()

    @abstractmethod
    def evolve(self, pursued_position_x, pursued_position_y):
        print('Evolving using parent method')


