# About
This sensor will monitor basic stats like player count and latency.\
It will base its error limits off the max player count at the time of creation.

# Setting up
You will need to add the below libaries to "C:\Program Files (x86)\PRTG Network Monitor\python\\"\
https://pypi.org/project/mcstatus/ \
https://pypi.org/project/dnspython/ \
https://pypi.org/project/asyncio-dgram/

# Sensor Atributes
The sensor will work off host name of the device.\
To set a custom port add it to the additional parameters.\
If the additional parameters is not set or it cannot convert to an int it will revert back to the default port of 25565.
