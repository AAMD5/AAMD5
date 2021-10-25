# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 23:17:48 2018

@author: AA17580
"""

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ START OF PROGRAM ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

import numpy as np
import matplotlib.pyplot as plt

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ NOTE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

 # Before starting the exercise, the Simpsons rule code used in the exercise 
 # will be tested for sin(x) to demonstrate that it works by giving correct 
 # values for the intergral of sin(x) between any two limits.

#~~~~~~~~~~~~~~~~~~~~~~ SIMPSON'S RULE CODE FOR SIN(X) ~~~~~~~~~~~~~~~~~~~~~~~#

def sinx(x0,xN):

    E = lambda x: np.sin(x)    
    t = 0        
    dx = (xN - x0) / N
    S = E(x0) + E(xN)                               # The initial value of the sum is sin(x0) + sin(xN) according to the Simpson rule.
        
    for n in range (0,N):                           # Initiation of the summing loop.
        
        if n % 2 != 0 and n < N:                    # This gives the condition that if n is odd then the odd terms are multiplied by 4.
            t = 4        
        else:                                       # This gives the condition that if n is even then the even terms are multiplied by 2.
            t = 2
                
        S += t*E(x0 + n*dx)                         # This completes the summation of all the odd terms and even terms along with the initial stated sum.            
        Integral_sinx = (dx/3)*S                    # Integration value (area under the curve) for sin(x) between the limits xN and x0.
            
    return Integral_sinx

#~~~~~~~~~~~~~~~~~~ CODE FOR PART (A) AND (B) OF THE EXERCISE ~~~~~~~~~~~~~~~~#

k = (2*np.pi)/(1e-6)                             # wavenumber
e0 = 8.8541878718e-12                            # permittivity of free space
c = 3e8                                          # speed of light

def Intensity1D(u1,u2,z,x0,xN):                         # u is x' and x is screen coordinate in x direction.
    
    xplots = []                                         # Empty list which will have all the x-values appended in it.
    yplots = []                                         # Empty list which will have all the Intensity values evaluated at each x-value appended in it.      

    E = lambda u: e0*c*((k)/(2*np.pi*z))*np.exp(((k*1j)/(2*z))*((x0 - u)**2))    # This is the expression for Eq(4) on the exercise which is to be integrated. 
    
    while (x0 < xN):
        
        t = 0      
        du = (u2 - u1) / N                              # dx'
        S = E(u1) + E(u2)                               # The initial value of the sum is f(x1') + f(x2') according to the Simpson rule.
        
        for n in range (0,N):                           # Initiation of the summing loop.
        
            if n % 2 != 0 and n < N:                    # This gives the condition that if n is odd then the odd terms are multiplied by 4.
                t = 4       
            else:                                       # This gives the condition that if n is even then the even terms are multiplied by 2.
                t = 2
               
            S += t*E(u1 + n*du)                         # This completes the summation of all the odd terms and even terms along with the initial stated sum.               
        Electric_field_x = (du/3)*S                     # Final value of integral at the first x-value (x0).       
        Intensity = abs(Electric_field_x)**2            # This is the intensity at the first x-value (x0).       
        dx = 0.00001        
        x0 += dx                                        # This tells python to repeat the process above for another x-value x = x0 + 0.00001 until it reaches the last x-value x = xN. The while loop ensures that this is the case.        
        xplots.append(x0)                               # putting all the x-values in the list xplots = [].        
        yplots.append(Intensity)                        # putting all the intensity values in the list yplots = [].
    
    return xplots, yplots

#~~~~~~~~~~~~~~~~~~ CODE FOR PART (C) AND (D) OF THE EXERCISE ~~~~~~~~~~~~~~~~#

def Electric_field_x(u1,u2,z,x0,xN):
            
     E = lambda u: e0*c*((k)/(2*np.pi*z))*np.exp(((k*1j)/(2*z))*((x0 - u)**2))  # This is the expression for Eq(4) on the exercise which is to be integrated.            
     t = 0                
     du = (u2 - u1) / N        
     S = E(u1) + E(u2)                
     for n in range (0,N):
                
         if n % 2 != 0 and n < N:
             t = 4                
         else:
             t = 2
             
         S += t*E(u1 + n*du)                        
     Electric_field_x = (du/3)*S 
            
     return Electric_field_x
            
def Electric_field_y(v1,v2,z,y0,xN):                                # v is y' and y is screen coordinate in y-direction.
            
    E = lambda v: np.exp(((k*1j)/(2*z))*((y0 - v)**2))              # This is the same expression for Eq(4) on the exercise but in terms of y and y' which is to be integrated.           
    t = 0            
    dv = (v2 - v1) / N    
    S = E(v1) + E(v2)
                
    for n in range (0,N):
                
        if n % 2 != 0 and n < N:
            t = 4                
        else:
            t = 2
                   
        S += t*E(v1 + n*dv)        
    Electric_field_y = (dv/3)*S 
            
    return Electric_field_y

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ TEST FOR SIN(X) ~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ INPUTS SECTION ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
Selected_Option = '0'

while Selected_Option != 'q':
    Selected_Option = input('Select one of the following options: \n\n(a) Select this option to test the Simpsons rule code on sin(x). \n(b) Select this option to plot relative intensity (E^2) against x. \n(c) Select this option to plot a 2D intensity image. \n(q) Select this option to exit the program. \n\n>>> Selected option: ')

    if Selected_Option == 'a':
        print('\nYou have selected option (a)')
        
        print("\nThis option will allow you to test the Simpson's rule code on the function sin(x). You can choose the following parameters: \n\n(1) The lower limit of x. \n(2) The upper limit of x. \n(3) The number of iterations N")
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ x0 value ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        
        x0_value = float(input("(1) Enter a value for the lower limit of x: "))               
        x0 = float(x0_value)            
        print("\nYou have entered x0 = ",x0_value)
                
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ xN value ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
            
        xN_value = float(input("(2) Enter a value for the upper limit of x: "))                 
        xN = float(xN_value)           
        print("\nYou have entered xN = ",xN_value)
        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Number of iterations N ~~~~~~~~~~~~~~~~~~~~~~#
                
        N_value = float(input("(3) Enter a value of N (even integer): "))
        
        while N_value != float():
                    
            if float(N_value) < 0 or float(N_value) % 2 != 0:
                N_value = input("Enter an even positive integer: ")
                        
            elif float(N_value) >= 0 and float(N_value) % 2 == 0:
                break
                    
        N = int(N_value)     
        print("\nYou have entered a value of", N_value)   
        print("\nThe value of the integral (area under the curve) for sin(x) from x =", x0 ,"to x =", xN ,"is", sinx(x0,xN),".")
    
#~~~~~~~~~~~~~~~~~~~~~~~ PART (A) AND (B) OF THE EXCERCISE ~~~~~~~~~~~~~~~~~~~#
    
    elif Selected_Option == 'b':
        print('\nYou have selected option (b)')       
        print("\nThis option will allow you to plot a graph of relative intensity against screen coordinate x for different parameter values. You can adjust the following parameters: \n\n(1) The lower limit of the apperture x1'. \n(2) The upper limit of the apperture x2'. \n(3) The lower limit of the screen x0. \n(4) The upper limit of the screen xN. \n(5) The screen distance z. \n(6) The number of iterations N. \n\nTo obtain the Fraunhofer far-field diffraction for a single-slit graph, the recommended parameters are: \n\n(1) x1' = -1 x 10^-5 m. \n(2) x2' = 1 x 10^-5 m. \n(3) x0 = -5 x 10^-3 m. \n(4) xN = 5 x 10^-3 m. \n(5) z = 2 cm. \n(6) N >= 100. \n\nTo obtain the Frensel near-field diffraction for a single-slit graph, the recommended parameters are: \n\n(1) x1' = -40 x 10^-5 m. \n(2) x2' = 40 x 10^-5 m. \n(3) x0 = -5 x 10^-3 m. \n(4) xN = 5 x 10^-3 m. \n(5) z = 2 cm. \n(6) N >= 600.")
        

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ INPUTS SECTION ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

# A note on the input section for the rest of the code from this point onwards:
        
    # The use of the "while" loop along with the "break" tool will be used 
    # in all the inputs to ensure that x1',y1',x0 and y0 are always less 
    # than zero as well as ensuring that x2',y2',xN and yN are always above
    # zero. This is so that the symmetry of the 1D and 2D plots is 
    # preserved. The same code idea is used to ensure that N is always even
    # and positive.

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ x1' value ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        
        u1_value = float(input("(1) Enter a value for aperture's lower limit (x 10^-5 m): "))
       
        while u1_value != float():
     
            if float(u1_value) > 0:
                u1_value = input("Enter a negative number: ")
        
            elif float(u1_value) <= 0:
                break
                                                 
        u1 = float(u1_value)*1e-5
        
        print("\nYou have entered x1' =",u1_value,"x 10^-5 m ")
        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ x2' value ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        
        u2_value = float(input("(2) Enter a value for aperture's upper limit (x 10^-5 m): "))
       
        while u2_value != float():
     
            if float(u2_value) < 0:
                u2_value= input("Enter a positive number: ")
                
            elif float(u2_value) >= 0:
                break
            
        u2 = float(u2_value)*1e-5
        
        print("\nYou have entered x2' =",u2_value,"x 10^-5 m ")      
        print("\nApperture's width = ", float(u2 - u1), "m")
         
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ x1 value ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        
        x0_value = float(input("(3) Enter a value for screen's lower limit (x 10^-3 m): "))
       
        while x0_value != float():
     
            if float(x0_value) > 0:
                x0_value= input("Enter a negative number: ")
                
            elif float(x0_value) <= 0:
                break
            
        x0 = float(x0_value)*1e-3      
        print("\nYou have entered x0 =",x0_value,"x 10^-3 m ")
        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ x2 value ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    
        xN_value = float(input("(4) Enter a value for screen's upper limit (x 10^-3 m): "))
       
        while xN_value != float():
     
            if float(xN_value) < 0:
                xN_value= input("Enter a positive number: ")
                
            elif float(xN_value) >= 0:
                break
            
        xN = float(xN_value)*1e-3       
        print("\nYou have entered xN =",xN_value,"x 10^-3 m ")     
        print("\nScreen width =", float(xN - x0), "m")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Screen distance z ~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        
        z_value = float(input("(5) Enter the distance to the screen (cm): "))
        
        while z_value != float():
     
            if float(z_value)<0:
                z_value= input("Enter a positive number: ")
                
            elif float(z_value)>=0:
                break
            
        z = float(z_value)*0.01        
        print("\nYou have entered z =",z_value,"cm")

#~~~~~~~~~~~~~~~~~~~~~~~~~ Number of iterations N ~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        
        N_value = float(input("(6) Enter a value of N (even integer): "))
  
        while N_value != float():
            
            if float(N_value) < 0 or float(N_value) % 2 != 0:
                N_value = input("Enter an even positive integer: ")
                
            elif float(N_value) >= 0 and float(N_value) % 2 == 0:
                break
            
        N = int(N_value)
        print("\nYou have entered a value of", N_value)

#~~~~~~~~~~~~~~~~~~~~~~~~~~ Graphing the intensity  ~~~~~~~~~~~~~~~~~~~~~~~~~~#

        xplots = Intensity1D(u1,u2,z,x0,xN)[0]                     # calling the x-values list (xplots) from the function definition which contains x-values from x0 to xN.
        yplots = Intensity1D(u1,u2,z,x0,xN)[1]                     # calling the y-values list (yplots)  from the function definition which contains intensity values evaluated at each x-value.
        plt.plot(xplots,yplots)
        plt.xlabel("Screen Coordinates x (m)")
        plt.ylabel("Relative Intensity (E^2)")
        plt.title("Relative Intensity against Screen Coordinate x")
        plt.show()                                                 # plotting the graph
 
#~~~~~~~~~~~~~~ PART (C) AND (D) OF THE EXERCISE: THE 2D IMAGE  ~~~~~~~~~~~~~~#
        
    elif Selected_Option == 'c':
        print('\nYou have selected option (c)')       
        print("\nThis option will allow you to plot a 2D intensity image graph for coordinates x and y while also allowing you to choose different parameter values. You can adjust the following parameters: \n\n(1) The lower limit of the apperture x1'. \n(2) The upper limit of the apperture x2'. \n(3) The lower limit of the screen x0. \n(4) The upper limit of the screen xN. \n(5) The lower limit of the apperture y1'. \n(6) The upper limit of the apperture y2'. \n(7) The lower limit of the screen y0. \n(8) The upper limit of the screen yN. \n(9) The screen distance z. \n(10) The number of iterations N. \n\nTo obtain a far field Fraunhofer diffraction image, the recommended parameters are: \n\n(1) x1' = -1 x 10^-4 m. \n(2) x2' = 1 x 10^-4 m. \n(3) x0 >= -3.5 x 10^-4 m. \n(4) xN >= 3.5 x 10^-4 m. \n(5) y1' = -1 x 10^-4 m. \n(6) y2' = 1 x 10^-4 m. \n(7) y0 >= -3.5 x 10^-4 m. \n(8) yN >= 3.5 x 10^-4 m. \n(9) z >= 25 mm. \n(10) N >= 100.\n\nIf you enter a value of z > 40 mm, it is advisable to make the screen width bigger by varying x0, xN and y0, yN. \n\nAs for the Frensel near-field diffraction image, the recommended parameters are: \n\n(1) x1' = -1 x 10^-4 m. \n(2) x2' = 1 x 10^-4 m. \n(3) x0 = -2.5 x 10^-4 m. \n(4) xN = 2.5 x 10^-4 m. \n(5) y1' = -1 x 10^-4 m. \n(6) y2' = 1 x 10^-4 m. \n(7) y0 = -2.5 x 10^-4 m. \n(8) yN = 2.5 x 10^-4 m. \n(9) 5 <= z <= 40 mm. \n(10) N >= 100. \n\nIf you enter a value of z < 5 mm, it is advisable to decrease the screen width by varying x0,xN and y0,yN. The value of N should also be increased to reduce the effect of artefacts. However, at values of z < 1 mm, the diffraction pattern breaks and appear 'unphysical'.")
        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ x1' value ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        
        u1_value = float(input("(1) Enter a value for aperture's lower limit in the x' direction (x 10^-4 m): "))
       
        while u1_value != float():
     
            if float(u1_value) > 0:
                u1_value = input("Enter a negative number: ")
                
            elif float(u1_value) <= 0:
                break
            
        u1 = float(u1_value)*1e-4        
        print("\nYou have entered x1'= ",u1_value,"x 10^-4 m ")
        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ x2' value ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        
        u2_value = float(input("(2) Enter a value for aperture's upper limit in the x' direction (x 10^-4 m): "))
       
        while u2_value != float():
     
            if float(u2_value) < 0:
                u2_value= input("Enter a positive number: ")
                
            elif float(u2_value) >= 0:
                break
            
        u2 = float(u2_value)*1e-4        
        print("\nYou have entered x2' =",u2_value,"x 10^-4 m ")        
        print("\nApperture's width in the x' direction =", float(u2 - u1), "m")
        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ x0 value ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        
        x0_value = float(input("(3) Enter a value for screen's lower limit in the x direction (x 10^-4 m): "))
       
        while x0_value != float():
     
            if float(x0_value) > 0:
                x0_value= input("Enter a negative number: ")
                
            elif float(x0_value) <= 0:
                break
            
        x0 = float(x0_value)*1e-4       
        print("\nYou have entered x0 =",x0_value,"x 10^-4 m ")
        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ xN value ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    
        xN_value = float(input("(4) Enter a value for screen's upper limit in the x direction (x 10^-4 m): "))
       
        while xN_value != float():
     
            if float(xN_value) < 0:
                xN_value= input("Enter a positive number: ")
                
            elif float(xN_value) >= 0:
                break
            
        xN = float(xN_value)*1e-4       
        print("\nYou have entered xN =",xN_value,"x 10^-4 m ")    
        print("\nScreen width in the x direction =", float(xN - x0), "m")
        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ y1' value ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        
        v1_value = float(input("(5) Enter a value for aperture's lower limit in the y' direction (x 10^-4 m): "))
       
        while v1_value != float():
     
            if float(v1_value) > 0:
                v1_value = input("Enter a negative number: ")
                
            elif float(v1_value) <= 0:
                break
            
        v1 = float(v1_value)*1e-4     
        print("\nYou have entered y1'=",v1_value,"x 10^-4 m ")
        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ y2' value ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        
        v2_value = float(input("(6) Enter a value for aperture's upper limit (x 10^-4 m): "))
       
        while v2_value != float():
     
            if float(v2_value) < 0:
                v2_value= input("Enter a positive number: ")
                
            elif float(v2_value) >= 0:
                break
            
        v2 = float(v2_value)*1e-4        
        print("\nYou have entered y2'=",v2_value,"x 10^-4 m ")    
        print("\nApperture's width in the y' direction= ", float(v2 - v1), "m")
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ y0 value ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        
        y0_value = float(input("(7) Enter a value for screen's lower limit in the y direction (x 10^-4 m): "))
       
        while y0_value != float():
     
            if float(y0_value) > 0:
                y0_value= input("Enter a negative number: ")
                
            elif float(y0_value) <= 0:
                break
            
        y0 = float(y0_value)*1e-4        
        print("\nYou have entered y0 =",y0_value," x 10^-4 m ")
        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ yN value ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    
        yN_value = float(input("(8) Enter a value for screen's upper limit in the y direction (x 10^-4 m): "))
       
        while yN_value != float():
     
            if float(yN_value) < 0:
                yN_value= input("Enter a positive number: ")
                
            elif float(yN_value) >= 0:
                break
            
        yN = float(yN_value)*1e-4        
        print("\nYou have entered yN =",yN_value,"x 10^-4 m ")        
        print("\nScreen width in the y direction =", float(yN - y0), "m")
        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Screen distance z ~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        
        z_value = float(input("(9) Enter the distance to the screen (mm): "))
        
        while z_value != float():
     
            if float(z_value)<0:
                z_value= input("Enter a positive number: ")
                
            elif float(z_value)>=0:
                break
            
        z = (float(z_value)*0.001)/2       
        print("\nYou have entered z =",z_value,"mm")
        
#~~~~~~~~~~~~~~~~~~~~~~~~~~ Number of iterations N ~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        
        N_value = float(input("(10) Enter a value of N (even integer): "))
  
        while N_value != float():
            
            if float(N_value) < 0 or float(N_value) % 2 != 0:
                N_value = input("Enter an even positive integer: ")
                
            elif float(N_value) >= 0 and float(N_value) % 2 == 0:
                break
            
        N = int(N_value)
        print("\nYou have entered a value of", N_value)
            
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ THE 2D PLOT ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#        
       
        dx = (xN - x0) / (N - 1)       #dx
        dy = (xN - x0) / (N - 1)       #dy
        intensity = np.zeros( (N,N) )
        for i in range(N):
            x0 = (i * dx) - xN          #The term - xN is important to shift the pattern to the centre
            for j in range(N):
                y0 = (j * dy) - yN      #The term - yN is important to shift the pattern to the centre
                #print(x0,y0)
                intensity[i,j] = (abs(Electric_field_x(u1,u2,z,x0,xN) * Electric_field_y(v1,v2,z,y0,yN))**2) # This is the calculation for Eq(5) on the exercise.
                print("{:.6f}".format(x0),"{:.6f}".format(y0),"{:.6f}".format(intensity[i,j]))
        
        plt.imshow(intensity)
        plt.xlabel('x (m)',fontsize = 15)
        plt.ylabel('y (m)',fontsize = 15)
        plt.colorbar(label = 'Intensity (arbitrary units)')
        plt.title("Intensity pattern from a square aperture")
        plt.show()
       
    elif Selected_Option == 'q':

        print('\nYou have exited the program - goodbye!')
        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ END OF PROGRAM ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
