'''
 This script will simulate a motor and a joint controller 
 computing Iq current from motor position and velocity 
 
 You are asked to:
    1) write the motor simulation model in "update_state(self,current)"
    2) a - design and code a position controller tracking p_ref 
       b - design and code a virtual spring and damper controller
    3) design and code a velocity controller tracking v_ref
    4) Run this controllers on the real test bench
    5) adapt simulation model according to experiment
    6) Improve your controller
'''
import numpy as np
from IPython import embed
import matplotlib.pyplot as plt
class TorqueMotorModel:
    #motor constants
    Kt=1e-3
    inertia=2e-5
    
    #motor state
    position=0.
    velocity=0.
    acceleration=0.
    current=0.
    torque=0.
    
    def __init__(self,dt=1e-3):
        self.dt=dt
        return;

    def update_state(self,current):
        #TODO...
        return

def controller(p,v,p_ref,v_ref):
    #TODO...
    current_ref = 0.1 #dummy control, for test
    return current_ref

dt=1e-3     #control period and simulation timestep
T=10        #simulation time in second
N=int(T/dt)
motor = TorqueMotorModel(dt)

#prepare arrays for logs
currents      = np.empty(N)+np.nan
torques       = np.empty(N)+np.nan
accelerations = np.empty(N)+np.nan
velocities    = np.empty(N)+np.nan
positions     = np.empty(N)+np.nan
times         = np.empty(N)+np.nan

p_ref = 1.0 #Goal position
v_ref = 0.0 #Goal velocity

for i in range(N):
    #call the controller
    current_ref = controller(motor.position,
                             motor.velocity,
                             p_ref,
                             v_ref )

    #simulate motor
    motor.update_state(current_ref);
    
    #log the motor state
    currents[i]     = motor.current
    torques[i]      = motor.torque
    accelerations[i] = motor.acceleration
    velocities[i]   = motor.velocity
    positions[i]    = motor.position
    times[i]        = i*dt
    
plt.plot(times,positions, label="Position")
#TODO add more plots?
plt.show()
