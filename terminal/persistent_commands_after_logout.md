# Persistent commands after logoout

## Nohup
"When using the command shell, prefixing a command with nohup prevents the command from being aborted if you log out or exit the shell." - https://www.computerhope.com/unix/unohup.htm

## Example usage
SSH into a raspi remotely, launch a ros node to output to a text file and run in the background. Without the nohup command, the node would stop running upon logout. With it, the node will persist after logout.
```
nohup roslaunch my_node > output.txt &
```
To see the node's console output in real time, tail (with follow) the output file.
```
tail -f output.txt
```
