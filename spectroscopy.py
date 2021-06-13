import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)

# Hydrogen Wide: [434,486,656]
# Hydrogen Thin: [397,410]
# Helium Wide: [388,588,668,706]
# Helium Thin: [447,471,492,501,558,616,728,778]

wideMeasured = [435,498,653]
thinMeasured = [415]
wideTrue = [434,486,656]
thinTrue = [397,410]

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

fig, ax = plt.subplots(2,1,figsize=(6,2.8))

ax[0].set_title("Measured Results")
ax[1].set_title("True Results")

ax[0].set_xlabel("Wavelength (nm)")
ax[1].set_xlabel("Wavelength (nm)")

for i in ax:
    i.set_xlim(380,780)
    i.set_ylim(0,1)

    i.set_xticks(range(400,800,50))

    i.xaxis.set_major_locator(MultipleLocator(50))
    i.xaxis.set_major_formatter('{x:.0f}')

    i.xaxis.set_minor_locator(MultipleLocator(10))

    i.set_yticks([])

plt.grid()


w,red,green,blue=[],[],[],[]
for wl in range(380,781):
    w+=[wl]
    if wl >= 380 and wl <= 440:
        r=-1*(wl-440)/(440-380)
        g=0
        b=1
    elif wl >= 440 and wl <= 490:
        r=0
        g=(wl-440)/(490-440)
        b=1
    elif wl >= 490 and wl <= 510:
        r=0
        g=1
        b=-1*(wl-510)/(510-490)
    elif wl >= 510 and wl <= 580:
        r=(wl-510)/(580-510)
        g=1
        b=0
    elif wl >= 580 and wl <= 645:
        r=1
        g=-1*(wl-645)/(645-580)
        b=0
    else:
        r=1
        g=0
        b=0

    if wl <= 420:
        s = 0.3+0.7*(wl-380)/(420-380)
    elif wl >= 700:
        s = 0.3+0.7*(780-wl)/(780-700)
    else:
        s=1

    red+=[s*r]
    green+=[s*g]
    blue+=[s*b]

wavelengths = range(380,781)

absorption = False

for wavelength in wavelengths:
    waveNum = wavelengths.index(wavelength)
    rgb = [red[waveNum],green[waveNum],blue[waveNum]]
    if not absorption:
        ax[0].plot([wavelength,wavelength],[0,1],c=(0,0,0),linewidth=5)
        ax[1].plot([wavelength,wavelength],[0,1],c=(0,0,0),linewidth=5)
    else:
        ax[0].plot([wavelength,wavelength],[0,1],c=rgb,linewidth=2)
        ax[1].plot([wavelength,wavelength],[0,1],c=rgb,linewidth=2)

def DrawLines(lines, graph, width):
    for wavelength in lines:
        waveNum = wavelengths.index(wavelength)
        rgb = [red[waveNum],green[waveNum],blue[waveNum]]
        if absorption:
            ax[graph].plot([wavelength,wavelength],[0,1],c=rgb,linewidth=width)
        else:
            ax[graph].plot([wavelength,wavelength],[0,1],c=(0,0,0),linewidth=width)

DrawLines(thinMeasured, 0, 1)
DrawLines(wideMeasured, 0, 2)
DrawLines(thinTrue, 1, 1)
DrawLines(wideTrue, 1, 2)


plt.tight_layout()

plt.show()
