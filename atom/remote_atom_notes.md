# remote-atom-notes
Notes on editing files locally that are stored on a remote device. See https://atom.io/packages/remote-atom

## Install
```
sudo curl -o /usr/local/bin/rmate https://raw.githubusercontent.com/aurora/rmate/master/rmate && sudo chmod +x /usr/local/bin/rmate && sudo mv /usr/local/bin/rmate /usr/local/bin/ratom
```

## Usage
Start server from local machine
```
Packages --> Remote Atom --> Start Server
```
SSH into remote device with port forwarding and X11 forwarding (useful when hacking on gui on remote device)
```
ssh -XR 52698:localhost:52698 user@example.com
```
SSH into remote device with port forwarding only
```
ssh -R 52698:localhost:52698 user@example.com
```
Open file on remote device
```
ratom file.txt
```
