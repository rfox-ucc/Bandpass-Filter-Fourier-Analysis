This project involved designing and building a bandpass filter circuit, to isolate a single component frequency of different types of wave. 
This was a really fun project, as it combined a whole bunch of skills we'd developed that year; circuit design in LTSpice, data manipulation in Excel, and Fourier analysis of different periodic waveforms.
Some interesting features I added were using Python to help pick appropriate components for the circuit, based on mandated minimums or maximums of different performance metrics. This can be seen in RCValues.py
I also created a LabVIEW utility to automatically identify appropriate timesteps for labelling the FFT data.

The report got a mark of 18/20 with the following feedback:
 (+1) Great job using code to calculate many different permutations for maximizing Q factor. 
 (+1) Fantastic verification of time constant. As for your conclusion, it's excellent. 
 The FFT of your output does in fact show a peak at 900Hz, however, the amplitude is far less than predicted. You can also visibly see it in the waveform, as there's a pattern that repeats every 3 wavelengths. 
 I'm unsure as to why the effects of the 1st harmonic are not more apparent when you let the square wave through. 
 One possibility is that a resistor is off from what you expected, so your gain is greater than the 10 you calculated, leading to the peak at 900hz being relatively low. 
 Looking at your frequency response, I would estimate it at no higher than 11 however. With the current resolution of your frequency response this is hard to verify. 
 It would also likely result in your frequency being slightly off (which you appear to have approximately counteracted by adding 30hz), which could once again throw off the actual gain values. 
 Overall fantastic report. Final Grade: 18
