# startup-rpi
Notes on running apps on startup with raspberry pi

## Non-GUI (rc.local)

Edit this file: 
```
sudo nano /etc/rc.local
```
Add in path to executable **BEFORE** "exit 0":
```
python /path/to/non-gui.py
```


## GUI (lxde autostart)

Edit this file:
```
sudo nano /home/pi/.config/lxsession/LXDE-pi/autostart
```

Add in path to executable:
```
@python /path/to/gui.py
```

## Test
```
ps aux | grep 'the-name-of-your-progam'
```

## Kill
```
kill -TERM [put-your-pid-here]
```
or 
```
kill -KILL [put-your-pid-here]
```


## Sources:
- http://www.raspberry-projects.com/pi/pi-operating-systems/raspbian/auto-running-programs-gui
- https://unix.stackexchange.com/questions/239519/how-can-i-kill-a-program-started-from-rc-local-when-ctrl-c-doesnt-work
