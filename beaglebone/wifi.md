## Issue w/bbb-wireless w/ubuntu 16.04
- https://bbs.archlinux.org/viewtopic.php?id=193820

## Setup Wifi
Open network manager
```
sudo connmanctl
```
Enable wifi
```
enable wifi
```
Disable wifi tether
```
tether wifi disable
```
Scan wifi
```
scan wifi
```
Show wifi networks
```
services
```
Register agent
```
agent on
```
Connect to wifi network
```
connect <name>
```

Sources
- https://www.digikey.com/en/maker/blogs/how-to-setup-wifi-on-the-beaglebone-black-wireless/f6452fa17bd24347a59f306355ebfef8
- http://stackoverflow.com/questions/43233008/issue-with-connmactl-in-beaglebone-green-wireless
