from matplotlib import pyplot as plt
import pyabf
import numpy as np

#Setup
abf = pyabf.ABF("Action Potentials.abf")
abf.setSweep(1)
plt.title("Phase Plot of 1 Action Potential")
plt.ylabel("V/s")
plt.xlabel("mV")
abf.setSweep(sweepNumber=1, channel=0)
arrayX = np.array(abf.sweepX).tolist()
arrayY = np.array(abf.sweepY).tolist()
arrayY = np.delete(arrayY,19999)
dvdt = np.diff(abf.sweepY)
dvdt = dvdt*10
dvdtlist = np.array(dvdt).tolist()
plt.plot(arrayY, dvdt, label = "Phase Plot")

#Threshold
tempDiff = 100
thresholdIndex = 0
for index in range(0,len(dvdtlist)):
  if (dvdtlist.__getitem__(index)) >= 20:
      thresholdIndex = index
      break
plt.axvline(arrayY.__getitem__(thresholdIndex), linewidth = 1, color = "red", linestyle = "dashed",label = "Threshold Point (20 V/s)")
plt.text(arrayY.__getitem__(thresholdIndex),dvdtlist.__getitem__(thresholdIndex),(str)((round)(arrayY.__getitem__(thresholdIndex),2))+"mV")


#Max Rise Rate
tempMax = 0
maxRateIndex = 0
for i in range(0,len(dvdtlist)):
    if(dvdtlist.__getitem__(i) > tempMax):
        tempMax = dvdtlist.__getitem__(i)
        maxRateIndex = i
plt.axvline(arrayY.__getitem__(maxRateIndex), linewidth = 1, color = "yellow", linestyle = "dashed", label = "Max Rise Rate")
plt.text(arrayY.__getitem__(maxRateIndex)-24,dvdtlist.__getitem__(maxRateIndex),(str)((round)(dvdtlist.__getitem__(maxRateIndex),2))+"V/s")

#Max Fall Rate
tempMin = 0
minRateIndex = 0
for i in range(0,len(dvdtlist)):
    if(dvdtlist.__getitem__(i) < tempMin):
        tempMin = dvdtlist.__getitem__(i)
        minRateIndex = i
plt.axvline(arrayY.__getitem__(minRateIndex), linewidth = 1, color = "orange", linestyle = "dashed", label = "Max Fall Rate")
plt.text(arrayY.__getitem__(minRateIndex),dvdtlist.__getitem__(minRateIndex)+4,(str)((round)(dvdtlist.__getitem__(minRateIndex),2))+"V/s")

#Peak Amplitude
tempMaxValue = 0
peakIndex = 0
for i in range(0, len(arrayY)):
    if(arrayY.__getitem__(i) > tempMaxValue):
        tempMaxValue = arrayY.__getitem__(i)
        peakIndex = i
plt.axvline(arrayY.__getitem__(peakIndex), linewidth = 1, color = "green", linestyle = "dashed", label = "Peak Amplitude")
plt.text(arrayY.__getitem__(peakIndex),dvdtlist.__getitem__(peakIndex),(str)((round)(arrayY.__getitem__(peakIndex)-arrayY.__getitem__(thresholdIndex),2))+"mV")

#AHP
tempMinValue = 0
AHPIndex = 0
for i in range(thresholdIndex, thresholdIndex+2000):
    if(arrayY.__getitem__(i) < tempMinValue):
        tempMinValue = arrayY.__getitem__(i)
        AHPIndex = i
plt.axvline(arrayY.__getitem__(AHPIndex), linewidth = 1, color = "purple", linestyle = "dashed", label = "AHP")
plt.text(arrayY.__getitem__(AHPIndex),dvdtlist.__getitem__(AHPIndex),(str)((round)(arrayY.__getitem__(AHPIndex),2))+"mV")

plt.legend()
plt.show()