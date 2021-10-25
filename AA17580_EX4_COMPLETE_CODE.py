# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 16:06:54 2019

@author: AA17580
"""

import matplotlib.pyplot as plt
import numpy as np
import pylab

# Constants and inputs.

G = 6.67e-11                     # Gravitational Constant.
M_E = 5.9722e24                  # Mass of Earth.
m = 2300000                      # Mass of rocket
    
def x_position():                # Initial rocket x-position.
    
    x0_value = float(input("Enter a value for the initial x-position in meters: "))
    x0 = float(x0_value)
    print("\nYou have entered a value of", x0_value, "m.")
    return x0
      
 
def Semi_Major_Axis_a():         # Semi-major axis for elliptical and eccentric rocket orbits.
    
    a0_value = float(input("Enter a value for the semi-major axis in meters: "))
    a0 = float(a0_value)
    print("\nYou have entered a value of", a0_value, "m.")
    return a0    


def Vertical_Velocity_Vy0():     # Rocket's initial vertical velocity. 
    
    Vy0_value = float(input("Enter a value for the vertical velocity component in m/s: "))
    Vy0 = float(Vy0_value)
    print("\nYou have entered a value of", Vy0_value, "m/s.")
    return Vy0


def Time_Step_h():               # Time step h
    
    h_value = float(input("Enter a value for the time step in seconds (positive number): "))
    while h_value != float():
        if float(h_value) < 0:                   # Ensures input is positive.
            h_value = input("Enter a positive number: ")
        elif float(h_value) >= 0:
            break
    h = float(h_value)
    print("\nYou have entered a value of", h_value, "seconds.")
    return h


# Definitions.   

def f1(Vx):                                             # dx/dt
    
    return Vx

def f2(Vy):                                             # dy/dt 
    
    return Vy

def f3(x, y, x_M, y_M):                                 # dVx/dt 
    
    return -((G*M_E*x)/(x**2 + y**2)**(3/2)) - (G*M_M*(x - x_M))/(((x - x_M)**2 + (y - y_M)**2)**(3/2))

def f4(x, y, x_M, y_M):                                 # dVy/dt 
    
    return -((G*M_E*y)/(x**2 + y**2)**(3/2)) - (G*M_M*(y - y_M))/(((x - x_M)**2 + (y - y_M)**2)**(3/2))         # f3 and f4 combines the potentials of both the Earth and the Moon to avoid adding extra lines for the Moon part. 
                                                                                                                # However, for inputs 1 - 2 the Moon's parameters are not needed so x_M, y_M and M_M are set to zero.
                                                                                                                
def Orbit(t, x, y, Vx, Vy):                                                                                     
    
    # Creating empty arrays to store the required values in them.
    tplots, xplots, yplots, Vxplots, Vyplots, KEplots, PEplots, Eplots = [], [], [], [], [], [], [], [] 
    d_closest = 10e8                                                                                            # Arbitrarily large distance to be able to calculate the closest 
                                                                                                                # distance the rocket can be from the Moon without crashing.
    for i in np.arange(0,T,h): 
    
        k1x = f1(Vx)                                     # Defining all 16 k terms.                            
        k1y = f2(Vy)                                                           
        k1Vx = f3(x, y, x_M, y_M)                                               
        k1Vy = f4(x, y, x_M, y_M)                                               
                    
        k2x = f1(Vx + (h*k1Vx)/2)                                               
        k2y = f2(Vy + (h*k1Vy)/2)                                               
        k2Vx = f3(x + (h*k1x)/2, y + (h*k1y)/2, x_M, y_M)                       
        k2Vy = f4(x + (h*k1x)/2, y + (h*k1y)/2, x_M, y_M)                       
    
        k3x = f1(Vx + (h*k2Vx)/2)                                               
        k3y = f2(Vy + (h*k2Vy)/2)                                              
        k3Vx = f3(x + (h*k2x)/2, y + (h*k2y)/2, x_M, y_M)                       
        k3Vy = f4(x + (h*k2x)/2, y + (h*k2y)/2, x_M, y_M)                       
        
        k4x = f1(Vx + h*k3Vx)                                                   
        k4y = f2(Vy + h*k3Vy)                                                  
        k4Vx = f3(x + h*k3x, y + h*k3y, x_M, y_M)                              
        k4Vy = f4(x + h*k3x, y + h*k3y, x_M, y_M)                              
                                                         # Stating the loops.
        tplots.append(t)
        t = t + h
        xplots.append(x)
        x = x + (h/6)*(k1x + 2*k2x + 2*k3x + k4x)
        yplots.append(y)
        y = y + (h/6)*(k1y + 2*k2y + 2*k3y + k4y)
        Vxplots.append(Vx)
        Vx = Vx + (h/6)*(k1Vx + 2*k2Vx + 2*k3Vx + k4Vx)
        Vyplots.append(Vy)
        Vy = Vy + (h/6)*(k1Vy + 2*k2Vy + 2*k3Vy + k4Vy)
                                                         # Stating the energy loops.
        KE0 = 0.5*m*(Vx0**2 + Vy0**2) 
        PE0 = -(G*M_E*m)/(x0**2 + y0**2)**0.5 
        E0 = KE0 + PE0                                   # Initial total energy.
        KE = 0.5*m*(Vx**2 + Vy**2) 
        KEplots.append(KE)
        PE = -(G*M_E*m)/(x**2 + y**2)**0.5 - (G*M_M*m)/((384.4e6 - x)**2 + y**2)**0.5
        PEplots.append(PE)
        E = -(KE + PE)/E0      # Division by E0 to normalise the total energy.
        Eplots.append(E)
    
        if MyInput != '3':  
        
            if np.sqrt(x**2 + y**2) <= 6371e3:                 # Crash condition on Earth.
                print("\n>>> You have crashed on the Earth!")
                print("\n>>> Total time elapsed =", "{:.3f}".format(t), "s","({:.3f}".format(t/(24*3600)), "days).")
                break
            
        elif MyInput == '3':    
        
            if x < x0 + 100000 and x > x0 - 100000 and t > 1000:       # Condition to stop simulation when one orbit is complete in the moon senario. At the end of the orbit, xfinal is not necessarily equal to x0 so tolerance limits were added.
                print("\n>>> Total time elapsed =", "{:.3f}".format(t), "s","({:.3f}".format(t/(24*3600)), "days).")
                break
            
            if np.sqrt(x**2 + y**2) <= 6371e3:                 # Crash condition on Earth.
                print("\n>>> You have crashed on the Earth!")
                print("\n>>> Total time elapsed =", "{:.3f}".format(t), "s","({:.3f}".format(t/(24*3600)), "days).")
                break
                                                               # Crash condition on Moon.
            if abs(x - 384.4e6) <= 1737.1e3 and abs(y) <= 1737.1e3:
                print("\n>>> You have crashed on the Moon!")
                print("\n>>> Total time elapsed =", "{:.3f}".format(t), "s","({:.3f}".format(t/(24*3600)), "days).")
                break
             
            d_moon = np.sqrt((x - 384.4e6)**2 + y**2) - 1737.1e3
            if d_moon < d_closest:
               d_closest = d_moon                              # Closest distance rocket can be from Moon without crashing into it.
            
        print("t -> {:.0f}\tx -> {:.0f}\ty -> {:.0f}\tVx -> {:.0f}\tVy -> {:.0f}\tE -> {:.15f}".format(t, x, y, Vx, Vy, E))
    
    return tplots, xplots, yplots, Vxplots, Vyplots, KEplots, PEplots, Eplots, d_closest  
    # returning the occupied arrays

# User inputs.

MyInput = '0'
while MyInput != 'q':
    print("__________________________________________________________________________________________")
    print("\nThis simulation will allow you to simulate circular, elliptical and eccentric (comet-like) orbits and investigate how the shape of the orbits changes with different initial parameters. In addition, it also simulates the slingshot orbit of a rocket launched from the Earth to the Moon and allows you to investigate the behaviour of the orbit for different initial conditions. \n\nNotes: \n\nFor simplicity, the initial y-position of the rocket y0 and the initial horizontal velocity component Vx0 were both set to 0 so that the rocket begins it's motion from the x-axis (line y = 0). \n\nGenerally, choosing a smaller time step increases the stability and the accuracy of the energy conservation. However, as the dimensions of the orbit become very large, larger time steps can be used (but the accuracy of the energy conservation may be lost and the orbits may not be repeatable).")
    MyInput = input("Select one of the following options: \n\n(1) To plot a circular orbit, \n\n(2) To plot an elliptical or eccentric orbit, \n\n(3) To plot the slingshot orbit to the Moon and back, \n\n(q) To quit the simulation. \n\n>>> Selected Option: ")
    print('\n>>> You have selected option: ',MyInput)
    
    if MyInput == '1':
        
        print("\n>>> In this part you can plot a circular orbit. The only inputs requied here are the initial x-position (so rocket begins its motion from the x-axis) and the time step h. The initial vertical velocity component Vy0 will be calculated automatically using the formula Vy0 = sqrt(GM_E/|x0|). The total time duration of the orbit will also be calculated autmatically using the equation T = (2*Pi*|x0|)/Vy0.")
        x_M = 0                             
        y_M = 0
        M_M = 0                                           
        t = 0
        x0 = x_position()
        y0 = 0
                                                          # Condition to prevent user from starting inside or at the surface of the Earth.
        while abs(x0) <= 6371e3:
            print("\n>>> You have entered a radius of", "{:.0f}".format(abs(x0)), "m which is less than 6371000 m. So you are at the surface or inside Earth. Please enter |x0| > 6371000 m.")
            x0 = x_position()
            y0 = 0
        if abs(x0) > 6371e3:
            x = x0
            y = y0
        
        Vx0 = 0
        Vy0 = np.sqrt(G*M_E/(abs(x0)))                    # Velocity for a circular orbit V = sqrt(GM/|x|).
        Vx = Vx0
        Vy = Vy0
        print("\n>>> The recommended time step value is h <= 50s.")
        h = Time_Step_h()
        
        Time_period = '0'
        while Time_period != 'q':
            Time_period = input(">>> Select option: \n\n(a) to plot one orbit, \n\n(b) to plot three repeated orbits (test for repeatability), \n\n(q) To restart simulation. \n\n>>> Selected Option: ")
            print('\n>>> You have selected option: ',Time_period)
            if Time_period == 'a':
                T = (2*np.pi*abs(x0))/Vy0                        # Time period for a circular orbit.
            elif Time_period == 'b':
                T = 3*(2*np.pi*abs(x0))/Vy0                      # repeats orbit 3 times.
            elif Time_period == 'q':
                break
                
            # Calling the occupied arrays of values from the definition Orbit(t, x, y, Vx, Vy).
            tplots, xplots, yplots, Vxplots, Vyplots, KEplots, PEplots, Eplots, d_closest = Orbit(t, x, y, Vx, Vy)
            
            # Plotting the orbit.
            plt.figure('Figure 1')
            Earth = plt.Circle((0,0), 6371000, color = 'royalblue')
            Rocket = plt.Circle((x0,y0), 200000, color = 'k')
            plt.gcf().gca().add_artist(Earth)                 # Plots Earth sized circle.
            plt.gcf().gca().add_artist(Rocket)                # Plots Rocket sized circle.
            plt.axis('equal')
            plt.plot(xplots,yplots,linestyle = '--' , color = 'm')
            plt.title("y-position against x-position")
            plt.xlabel("x-position (m)")
            plt.ylabel("y-position (m)")
            plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
            plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
            plt.show()
            print("\n>>> Orbit radius =","{:.0f}".format(abs(x0)),"m","({:.0f}".format(abs(x0) - 6371e3),"m above Earth's surface).\n\n>>> Vertical velocity component for stable orbit =","{:.0f}".format(Vy0),"m/s. \n\n>>> Total time elapsed =", "{:.3f}".format(T),"s","({:.3f}".format((T)/(24*3600)), "days).")
            
            # Plots to demonstrate energy conservation.
            pylab.plot(tplots,KEplots, linewidth = 1, color = 'b', label = 'KE')
            pylab.plot(tplots,PEplots, linewidth = 1, color = 'r', label = 'PE')
            pylab.plot(tplots,Eplots, linewidth = 1, color = 'k', label = 'E')
            pylab.title("Energy against time")
            pylab.xlabel("Time (s)")
            pylab.ylabel("Energy (J)")
            pylab.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
            pylab.legend(ncol = 3, loc = "center")
            pylab.show()  
            
            print("\n>>> The graph below is a zoomed in version of the second graph. It is clear that the energy is approximately conserved and has a constant normalised value of -1J.")
            plt.plot(tplots,Eplots, color = 'k')
            plt.title("Total energy against time")
            plt.xlabel("Time (s)")
            plt.ylabel("Energy (J)")
            plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
            plt.ylim(-1.5, -0.5)
            plt.show()
      
    elif MyInput == '2':
        
        print("\n>>> In this part you can plot an elliptical orbit. The inputs requied here are the initial x-position (so rocket begins its motion from the x-axis), the time step h and the semi-major axis a0 to allow you to control the eccentricity of the orbit (to get an eccentric orbit, choose a0 >> x0). The initial vertical velocity component Vy0 will be calculated automatically using the vis-viva formula Vy0 = sqrt((G*M_E)*((2/|x0|)-(1/|a0|))). The total time duration of the orbit will also be calculated autmatically using the equation T = (2*Pi*a0^(3/2))/sqrt(G*M_E).")
        x_M = 0
        y_M = 0
        M_M = 0
        t = 0
        x0 = x_position()
        y0 = 0
                                                  
        while abs(x0) <= 6371e3:
            print("\n>>> You have entered a starting x-position of", "{:.0f}".format(abs(x0)), "m which is less than 6371000 m. Please enter |x0| > 6371000 m.")
            x0 = x_position()
            y0 = 0
        if abs(x0) > 6371e3:
            x = x0
            y = y0
        
        a0 = Semi_Major_Axis_a()
        
        while abs(a0) < abs(x0):
            print("\n>>> You have entered a semi-major axis of","{:.0f}".format(abs(a0)), "m which is less than", "{:.0f}".format(abs(x0)), "m. Please enter |a0| > |x0|.")
            a0 = Semi_Major_Axis_a()
        if abs(a0) >= abs(x0) > 6371e3:
            a = a0           
        
        Vx0 = 0
        Vy0 = np.sqrt((G*M_E)*((2/abs(x0))-(1/abs(a0))))                   # Velocity for an elliptical orbit V = sqrt((G*M_E)*((2/|x0|)-(1/|a0|)))
        Vx = Vx0
        Vy = Vy0
        print("\n>>> The recommended time step value is h <= 50s.")
        h = Time_Step_h()
        
        Time_period = '0'
        while Time_period != 'q':
            Time_period = input(">>> Select option: \n\n(a) to plot one orbit, \n\n(b) to plot three repeated orbits (test for repeatability), \n\n(q) To restart simulation. \n\n>>> Selected Option: ")
            print('\n>>> You have selected option: ',Time_period)
            if Time_period == 'a':
                T = (2*np.pi*(abs(a0))**(3/2))/(G*M_E)**0.5               # Time period for an elliptical orbit.
            elif Time_period == 'b':
                T = 3*(2*np.pi*(abs(a0))**(3/2))/(G*M_E)**0.5             
            elif Time_period == 'q':
                break
        
            tplots, xplots, yplots, Vxplots, Vyplots, KEplots, PEplots, Eplots, d_closest = Orbit(t, x, y, Vx, Vy)
    
            plt.figure('Figure 1')
            Earth = plt.Circle((0,0), 6371000, color = 'royalblue')
            Rocket = plt.Circle((x0,y0), 200000, color = 'k')
            plt.gcf().gca().add_artist(Earth)                 
            plt.gcf().gca().add_artist(Rocket)                
            plt.axis('equal')
            plt.plot(xplots,yplots,linestyle = '--' , color = 'm')
            plt.title("y-position against x-position")
            plt.xlabel("x-position (m)")
            plt.ylabel("y-position (m)")
            plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
            plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
            plt.show()
            print("\n>>> Initial x-position =","{:.0f}".format(x0),"m","({:.0f}".format(abs(x0) - 6371e3),"m above Earth's surface). \n\n>>> Semi-major axis =","{:.0f}".format(abs(a0)),"m. \n\n>>> Vertical velocity component for stable orbit =","{:.0f}".format(Vy0),"m/s. \n\n>>> Total time elapsed =", "{:.3f}".format(T), "s","({:.3f}".format(T/(24*3600)), "days).\n\n>>> Eccentricity of the orbit is","{:.3f}".format(1 - abs(x0/a0)),"." )
            
            pylab.plot(tplots,KEplots, linewidth = 1, color = 'b', label = 'KE')
            pylab.plot(tplots,PEplots, linewidth = 1, color = 'r', label = 'PE')
            pylab.plot(tplots,Eplots, linewidth = 1, color = 'k', label = 'E')
            pylab.title("Energy against time")
            pylab.xlabel("Time (s)")
            pylab.ylabel("Energy (J)")
            pylab.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
            pylab.legend()
            pylab.show()  
            
            print("\n>>> The graph below is a zoomed in version of the second graph. It is clear that the energy is approximately conserved and has a constant normalised value of -1J.")
            plt.plot(tplots,Eplots, color = 'k')
            plt.title("Total energy against time")
            plt.xlabel("Time (s)")
            plt.ylabel("Energy (J)")
            plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
            plt.ylim(-1.5, -0.5)
            plt.show()
    
    elif MyInput == '3':
        
        print("\n>>> In this part you can plot the slingshot orbit of a rocket launched from Earth to the Moon and back to Earth. To obtain the successful path, the recommended values are: \n\n>>> x-position = -6750000 m \n>>> Vertical velocity component Vy0 = 10755.325 m/s \n>>> Time step h <= 100s. \n\nTo test the crash condition, input the same values but change the vertical velocity component from 10755.325 m/s to 10758 m/s or 10760 m/s.")
        M_M = 7.3478e22                     # Mass of the Moon.
        x_M = 384.4e6                       # x-coordinate of the Moon's centre (Earth-Moon centre to centre distance).
        y_M = 0                             # y-coordinate of the Moon's centre.
        t = 0
        x0 = x_position()
        y0 = 0
        
        while np.sqrt((x0**2 + y0**2)) <= 6371e3:
            print("\n>>> You have entered a starting x-position of","{:.0f}".format(abs(x0)), "m which is less than 6371000 m. So you are at the surface or inside Earth. Please enter |x0| > 6371000 m.")
            x0 = x_position()
            y0 = 0
        if np.sqrt((x0**2 + y0**2)) > 6371e3:
            x = x0
            y = y0
            
        Vx0 = 0
        Vy0 = Vertical_Velocity_Vy0()
        Vx = Vx0
        Vy = Vy0
        print("\n>>> The recommended time step value is h <= 100s.")
        h = Time_Step_h()
        T = 2000000                                       # Arbitrary big value for time period for moon stopping condition to work within the tolerances stated.

        tplots, xplots, yplots, Vxplots, Vyplots, KEplots, PEplots, Eplots, d_closest = Orbit(t, x, y, Vx, Vy)

        plt.figure('Figure 1')
        Earth = plt.Circle((0,0), 6371000, color = 'royalblue')
        Moon = plt.Circle((384.4e6,0), 1737100, color = 'gray')
        Rocket = plt.Circle((x0,y0), 200000, color = 'k')
        plt.gcf().gca().add_artist(Earth)
        plt.gcf().gca().add_artist(Moon)                  # Plots Moon sized circle.
        plt.gcf().gca().add_artist(Rocket)  
        plt.axis('equal')
        plt.plot(xplots,yplots,linestyle = '--' , color = 'm')
        plt.title("y-position against x-position")
        plt.xlabel("x-position (m)")
        plt.ylabel("y-position (m)")
        plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
        plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
        plt.show()
        print("\n>>> Initial x-position =","{:.0f}".format(x0),"m","({:.0f}".format(abs(x0) - 6371e3),"m above Earth's surface). \n\n>>> Vertical velocity component entered =","{:.3f}".format(Vy0),"m/s.")
        print("\n>>> The Closest distance the rocket can get to the moon without crashing =","{:.0f}".format(d_closest),"m (ignore if you have crashed on the Moon).")
        
        pylab.plot(tplots,KEplots, linewidth = 1, color = 'b', label = 'KE')
        pylab.plot(tplots,PEplots, linewidth = 1, color = 'r', label = 'PE')
        pylab.plot(tplots,Eplots, linewidth = 1, color = 'k', label = 'E')
        pylab.title("Energy against time")
        pylab.xlabel("Time (s)")
        pylab.ylabel("Energy (J)")
        pylab.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
        pylab.legend()
        pylab.show()  
        
        print("\n>>> The graph below is a zoomed in version of the second graph. Assuming you haven't crashed, it is clear that the energy is approximately conserved and has a constant normalised value of -1J.")
        plt.plot(tplots,Eplots, color = 'k')
        plt.title("Total energy against time")
        plt.xlabel("Time (s)")
        plt.ylabel("Energy (J)")
        plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
        plt.ylim(-1.5, -0.5)
        plt.show()
        
    elif MyInput == 'q':
        print("\n>>> You have exited the simulation - Goodbye!")