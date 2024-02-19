from math import *
import numpy as np
import matplotlib.pyplot as plt


# coil dimentions and winding parameters


# other inputs
rwidth = 0.086     #dimention of the Al pad which is 80 mm + 6mm each side 
cheight = 0.022    # up to cheight winding can go  
clength = 0.025    # area for winding per layer 
mu0 = 1.26e-6      
rho = 0.02e-9      
Bmax = 0.001    # Tesla


def lay(d):
    return int((cheight/d - 1) * sin(60 / 180 * pi) + 1)


def Imax(d):
    return Bmax * clength / (mu0 * wind(d))


def wind(d):
    return clength/d * lay(d)


def eff_length(d):
    return wind(d) * (rwidth + cheight) * 4


def R(d):
    A = (d/2)**2 * np.pi

    return rho * eff_length(d)/A


def P(d):
    return Imax(d)**2 * R(d)


def I(d):
    print('layer:', lay(d))
    print('windings:', wind(d))
    print('Imax:', Imax(d))
    print('Power:', P(d))


#  Magnetic field distribution 

def B_field(x,y,d):
    z= np.sqrt(3) * (x + 0.5 *y)
    return Bmax *np.exp(-2*np.pi*(x**2 + y**2) /(d**2)) * np.cos(z / (d/2))



# Heat 

def plot_heat_variation():
    dimensions = np.linspace(0.001, 0.0001, 100)  # range of coil dimesion to nalysis
    heat = [P(d) for d in dimensions]
    plt.plot(dimensions, heat)
    plt.xlabel('Coil Dimension (m)')
    plt.ylabel('Heat (W)')
    plt.title('Heat Variation with Coil Dimension')


def analyze_heat(d):
    print('layer:', lay(d))
    print('winding:', wind(d))
    print('Imax:', Imax(d))
    print('Power:', P(d))
