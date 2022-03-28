# Sensable Omni URDF

This code is written to launch a ros node with the urdf robot
description as a parameter. It is based on this tutorial:
https://docs.ros.org/en/foxy/Tutorials/URDF/Using-URDF-with-Robot-State-Publisher.html

It also provides a Python script to publish a joint state and animate the Omni.

# Compilation

1. Create a ros2 workspace with the src code inside
2. Run the following in the workspace:
```sh
colcon build --symlink-install --packages-select sensable_omni_urdf
```

# Usage

```sh
# don't forget to source after first compilation
source install/setup.bash
# launch script with robot state publisher and our python script to animate the Omni
ros2 launch omni demo.launch.py
# to visualize the Omni in rviz...
rviz2 -d ~/<workspace_name>/install/sensable_omni_urdf/share/sensable_omni_urdf/omni.rviz # to launch rviz with the omni frames
```
