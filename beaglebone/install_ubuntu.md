## Ubuntu 16.04
Download ubuntu 16.04 image for beaglebone
- https://rcn-ee.com/rootfs/2017-06-12/flasher/BBB-eMMC-flasher-ubuntu-16.04.2-console-armhf-2017-06-12-2gb.img.xz

Extract image
- http://unarchiver.c3.cx/unarchiver

Flash image onto sd card
- [Pi Baker Download Link](https://www.atlas-scientific.com/_files/software/ApplePi-Baker.zip)

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
