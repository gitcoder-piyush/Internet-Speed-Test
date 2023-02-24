# Internet-Speed-Test
Check your internet's uploading and downloading speed.

# Technology Used

* Tkinter

* SpeedTest-cli

# Working Principle:

Tkinter is used to create the graphical user interface. The speedtest-cli is a ommand line interface for testing internet bandwidth using speedtest.net. This project has 5 labels that contains information to be displayed graphically and one function i.e. speedcheck (). get_servers() method in Speedtest class returns uploading and downloading speed from the servers with is displayed using config() function. upload and download function return speed in bytes per second which is then converted to Mbps by dividing with (10^6).The resulant number is then rounded up to 3 decimal digits using round function.

# Video

https://user-images.githubusercontent.com/111907542/221173706-98893250-b986-4acf-8805-543fe3168785.mp4




