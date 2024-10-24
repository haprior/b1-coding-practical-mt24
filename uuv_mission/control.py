
class Controller:
    def __init__(self, kp, kd):
        self.kp = kp
        self.kd = kd

    def get_output(self, current_error, previous_error):
        output = current_error * (self.kp + self.kd) - previous_error * self.kd
        return output