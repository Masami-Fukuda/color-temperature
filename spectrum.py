import numpy as np
from matplotlib import pyplot as plt

l = np.arange(1,1200)
T = np.array([[2900,'red'],[5000,'green'],[6500,'black'],[9300,'blue']])

# set cofficients
h = 6.6260755e-34
k = 1.380658e-23
c = 2.99792458e8

#set wavelength of R,G,B
rl = 700e-9
gl = 546e-9
bl = 436e-9


for t in T:
    spectrum = ( 8 * np.pi * h * c) / ((l*1e-9)**5*np.e**(h*c/(k*t[0].astype(np.int)*(l*1e-9))-1))
    spectrum = spectrum/spectrum.max()
    plt.plot(l,spectrum, label=t[0],color=t[1])

plt.legend()
plt.title('Color Temperature and wave length')
plt.xlabel('Wave Length: (nm)')

plt.show()


