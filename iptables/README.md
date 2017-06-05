# iptables-notes
Notes on using iptables

## Mega basic usage just to access a local port on a public ip
Set iptable to accept traffic on a specific port. NOTE: this does not persist across reboots
```
iptables -A INPUT -p tcp -m tcp --dport <port> -j ACCEPT
```
Hit the api by going to 
```
http://<ip>:<port>
```
