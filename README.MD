# Thermostat Emulator
## Setup
> This docs assume your system is debian/ubuntu or its derivative.

if you don't have a virtualenv installed, please install virtualenv and activate it:
```bash
sudo apt install python3-pip
python3 -m virtualenv env
source bin/activate
```

then, clone this repository:
```bash
https://github.com/ekharisma/thermometer-emulator.git
```

You need to install the project's requirements:
```bash
pip install -r requirements.txt
```

## Usage
Run thermostat.py file:
```bash
python3 thermostat.py
```
If you also want to know thermostat.py in action, you can run receiver.py file:
```bash
python3 receiver.py
```
