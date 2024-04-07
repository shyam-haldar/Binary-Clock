# Binary-Clock
This script displays the current localtime as a 64 bit binary data in a 8x8 matrix format.

<img width="279" alt="Screenshot 2024-04-01 at 5 55 52 PM" src="https://github.com/shyam-haldar/Binary-Clock/assets/159643896/6123c33e-b94e-487d-ac86-4d06c0af2b4b">


I came across various such projects on thernet where this was done using Arduino. This is my take using Python & PyQt5.

## Note
Please stop the clock before closing the app otherwise it crashes. I did not go through the task to fix this as this app does not do anything useful.
This is just a fancy app.

If you want you can add an edit bar to accept a date and time and then represent that in a 8x8 matrix.

## Readme
I have included the PyQt5 ui file as well 'binary_clock.ui'. You can use this generate the gui file which manages the Window part of the script.
To generate the file 'binary_clock_gui.py' run the following command...

```bash
pyuic5 -o binary_clock_gui.py binary_clock.ui
```

And to run the script, place both the py files in the same directory and run the following command...

```bash
python binary_clock_main.py
```

I have used the 'Anaconda' distribution of python and install PyQt5 which includes 'pyuic5'.
