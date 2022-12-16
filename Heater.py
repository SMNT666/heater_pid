import random

def constrain(value, min_out, max_out):
    if value < min_out:
        return min_out
    elif value > max_out:
        return max_out
    return value


class Heater:
    def __init__(self):
        self.C_heater = 0.385
        self.C_air = 1.000
        self.Ro_air = 1.2
        self.L_air = 160.0
        self.temp_air = 20.0
        self.current_temp_air = 20.0



        self.power = 0.0
        self.weight = 1.0

    def get_power(self):
        return self.power

    def get_current_temp_air(self):
        return self.current_temp_air

    def compute(self, power, dt):
        self.power = power
        print(f"TEMP AIR: {self.current_temp_air}, POWER: {self.power}")

        deltaT = (self.power * dt - self.C_heater * self.weight * (self.current_temp_air - self.temp_air) * dt) / (self.C_air * self.Ro_air * self.L_air)
        self.current_temp_air += deltaT

class PID:
    integral = 0
    prevErr = 0
    kp = 10.0
    ki = 0.06
    kd = 0.1
    minOut = 0
    maxOut = 0

    def __init__ (self,maxpower):
        self.maxOut = maxpower

    def computePID(self, input_t, setpoint, dt):
        err = setpoint - input_t
        integral = constrain(PID.integral + err * dt * self.ki, self.minOut, self.maxOut)
        D = (err - PID.prevErr) / dt
        PID.prevErr = err
        return constrain(err * self.kp + integral + D * self.kd, self.minOut, self.maxOut)


