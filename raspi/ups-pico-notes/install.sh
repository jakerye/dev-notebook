#!/bin/bash

sudo apt-get update
sudo apt-get -y dist-upgrade
sudo apt-get install python-rpi.gpio
sudo apt-get install -y git python-dev python-serial python-smbus python-jinja2 python-xmltodict python-psutil python-pip
sudo pip install xmltodict
cd ~
sudo git clone https://github.com/modmypi/PiModules.git
cd ~/PiModules/code/python/package
sudo python setup.py install
cd ~/PiModules/code/python/upspico/picofssd
sudo python setup.py install
sudo update-rc.d picofssd defaults
sudo update-rc.d picofssd enable
sudo apt-get install i2c-tools
