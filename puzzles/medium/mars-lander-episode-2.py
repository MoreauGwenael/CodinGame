import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

max_vspeed_landing = 40
max_hspeed_landing = 20
danger_landing_angle = 30
fast_landing_angle = 45

class Shutle:
    angle = 0
    power = 0
    v_speed = 0
    h_speed = 0
    v_a = 0
    h_a = 0
    
    def get_params(self):
        v_speed_last, h_speed_last = self.v_speed, self.h_speed
        self.x, self.y, self.h_speed, self.v_speed, self.fuel, self.rotate, self.power = [int(i) for i in input().split()]
        self.v_a, self.h_a = (self.v_speed - v_speed_last), (self.h_speed - h_speed_last)
    
    def print_params(self):
        print(self.angle, self.power)

class LandingZone:
    _landing_start = 0
    _landing_end = 7000
    _landing_height = 0
    _shutle = Shutle()    
    _dir_mult = 0
    _hightest_dot = 0    
    def __init__(self):
        surface_n = int(input())
        land_x_prev = land_y_prev = 0
        for i in range(surface_n):
            land_x, land_y = [int(j) for j in input().split()]
            if (land_x_prev != 0 and land_y_prev == land_y):
                self._landing_height = land_y
                self._landing_start = land_x_prev
                self._landing_end = land_x
            if self._hightest_dot<land_y:
               self._hightest_dot = land_y 
            land_x_prev, land_y_prev = land_x, land_y

    def getShutleSituation(self):        
        self._shutle.get_params()
        if self._landing_start < self._shutle.x < self._landing_end:
            self._dir_mult = 0
        elif self._shutle.x < self._landing_start:
            self._dir_mult = - 1
        else:
            self._dir_mult = 1
            

    def getToSafeZone(self):
        if self._dir_mult != 0:
            if self._shutle.y - self._hightest_dot <500:
                l_a = danger_landing_angle
                l_s = max_hspeed_landing
            else:
                l_a = fast_landing_angle
                l_s = max_hspeed_landing*2
            self._shutle.power = 4
            if ((-self._dir_mult * self._shutle.h_speed) < l_s):
                self._shutle.angle = int(self._dir_mult * l_a)
            elif (-self._dir_mult * self._shutle.h_speed > l_s + 5):
                self._shutle.angle = -int(self._dir_mult * l_a)
            else:
                self._shutle.angle = 0
        else:
            self.gorisontalCorrect()

    def gorisontalCorrect(self):
        if abs(self._shutle.h_speed) > max_hspeed_landing  or(self._shutle.h_speed>0 and self._landing_end -self._shutle.x<500) or(self._shutle.h_speed<0 and self._landing_start -self._shutle.x<-500):            
            self._shutle.angle = self._shutle.h_speed * 3
            if self._shutle.angle > danger_landing_angle:
                self._shutle.angle = danger_landing_angle
            elif self._shutle.angle < -danger_landing_angle:
                self._shutle.angle = -danger_landing_angle
        else:
            self._shutle.angle = 0
                

    def landing(self):    
        if (self._shutle.v_speed < -(max_vspeed_landing - 5) or self._shutle.angle!=0 or self._dir_mult!=0) and self._shutle.y<2800:
            self._shutle.power = 4
        else:
            self._shutle.power = 3

    def run(self):
        self.getToSafeZone()    
        self.landing()
        self._shutle.print_params()

landing_zone = LandingZone()
while True:
    landing_zone.getShutleSituation()
    landing_zone.run()
