class Controller:
    """
    This class implement using a PD feedback controller
    attribute: 
    Kp: proportional gain of the controller
    Kd: derivative gain of the contronller
    previous_error: use to record the error at previous time step

    """
    def __init__(self, Kp, Kd):
        self.Kp = Kp
        self.Kd = Kd
        self.previous_error = 0

    def pd_output(self, reference,observation):
        error = reference - observation
        output  = self.Kp * error + self.Kd*(error - self.previous_error)
        self.previous_error = error
        return output
    
    def reset(self):
        self.previous_error = 0