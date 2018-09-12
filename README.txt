As of 9/12/18, this code is incomplete, but near completion.

What this code aims to do is to isolate the forehead reigon, take the average of the green pixels located there,
apply FFT to the forehead, then find the maximum value of the FFT plot. This maximum value corresponds with an
approximation of the users heart beat.

If you run the code, you notice that I have added a plot toward the end for diagnostic purposes. This plots the
absolute values of the the scaled FFT function. From here, it should be easy to see the heart beat as the max y 
value. However, the plot is crowded with various different signals, and as of now I'm figuring out how to remove
all the noise in the plot.

This code is still very much in development. 