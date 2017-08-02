# screen
"I prefer to use the "screen" command [to nohup].  It is immune to shell issues and is much more stable." - Rob from ML

## Install
```
sudo apt-get install -y screen
```
## Commands
View screen session IDS
```
screen -ls to see the screen session IDs
```

Reattach to a session
```
screen -r <name>
```

Detach an existing session and reattach to it
```
screen -D -R <name> 
```

Start a new named session (with the same title)
```
screen -S <name> -t <name> 
```

Detach a session you are in
```
Ctrl+a then d
```

Kill a session
```
Ctrl+a then k
```

View session title
```
Ctrl+a then N (-t parameter upon creation)
```

Scroll screens up and down
```
Ctrl+a then [ to go into copy mode, then:
  Ctrl+U or Ctrl+D for half screen up and down or
  Ctrl+B or Ctrl+F for full screens up and down
```
