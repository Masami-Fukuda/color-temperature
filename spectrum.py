import numpy as np
from matplotlib import pyplot as plt

l = np.arange(1,1200)
T = [2900,5000,6500,9300]

# set cofficients
h = 6.6260755e-34
k = 1.380658e-23
c = 2.99792458e8

#set wavelength of R,G,B
rl = 700e-9
gl = 546e-9
bl = 436e-9


for t in T:
    spectrum = ( 8 * np.pi * h * c) / ((l*1e-9)**5*np.e**(h*c/(k*t*(l*1e-9))-1))
    spectrum = spectrum/spectrum.max()
    plt.plot(l,spectrum)

plt.show()


