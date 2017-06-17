## Ubuntu 16.04
Download ubuntu 16.04 image for beaglebone and flash onto micro-sd card
- https://rcn-ee.com/rootfs/2017-04-07/elinux/ubuntu-16.04.2-console-armhf-2017-04-07.tar.xz

Flash onto eMMC
- Turn off beaglebone
- Plug in sd card
- Hold button near sd card
- Turn on beaglebone
- Watch leds cylon (+---, -+--, --+-, ---+, --+-, ...)
- Once pi turns off, re-plug into usb port

Connect into beaglebone
```
ssh ubuntu@192.168.7.2

pwd: temppwd
```

Sources
- http://elinux.org/BeagleBoardUbuntu#Ubuntu_.2816.04.2.29