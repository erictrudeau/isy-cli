isy-cli
=======

a simple cli for controlling Insteon devices using the REST API on the Universal Devices ISY home automation controller.

## Running

You will need to modify the script to include the server, username and password of your ISY controller.  You wil also need to add the name & addresses of your Insteon devices to the **devices** dict.  Note that the format for the address is **XX XX XX 1**.

## Todo

* Convert dimmer values to percentages (from 0-255 to 0-100)
* Add aliases for devices (maybe)

## Licence

[isy-cli](https://github.com/erictrudeau/isy-cli) by [Eric Trudeau](https://github.com/erictrudeau) is licensed under a [Creative Commons Attribution-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-sa/3.0/deed.en_US).

[![Creative Commons License](http://i.creativecommons.org/l/by-sa/3.0/88x31.png)](http://creativecommons.org/licenses/by-sa/3.0/deed.en_US)
