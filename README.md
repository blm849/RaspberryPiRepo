# RaspberryPiRepo
A repository for files related to my working on the Raspberry Pi

I wanted to have a repository to share any files or information pertaining to work I am doing with the Raspberry Pi

The config.txt file is one I used with an old Raspberry Pi to send composite/component video output (i.e. not HDMI) to an old Toshiba TV. Details on the set up can be found here: https://smartpeopleiknow.com/2017/04/18/how-to-get-a-raspberry-pi-working-with-a-tv-with-compositecomponent-input-as-opposed-to-hdmi/

The Python programs are sample code to perform various actions on the Raspberry Pi.
led_blink.py and switch.py are two test programs I wrote, based on sample code from O'Reilly,
that allow me to work with LEDs and switches attached to my Pi.
ippushover.py is a program I have listed at the bottom of file /etc/profile of my headless
Raspberry Pis that have network connections. When it runs it uses the API from pushover.net
to send the IP address to my iPhone. I can then SSh or Scp into the headless Pi.

See the comments in the .py programs for more information.
