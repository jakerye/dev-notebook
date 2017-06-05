# Robot Operating System (ROS) Notes

## List Dependencies (supported by ros)
Typical packages run
```
rosdep resolve python-<mypackage>
```
Or
```
rosdep resolve python-<mypackage>-pip
```

## Install Dependencies
```
rosdep install --from-paths src --ignore-src --rosdistro indigo -y -r --os=debian:jessie
```

## Contribute Python Dependencies to ROS
- http://docs.ros.org/independent/api/rosdep/html/contributing_rules.html
- See link below

## Dependency Sources
- https://wiki.openag.media.mit.edu/ros/dependencies#python_dependencies
