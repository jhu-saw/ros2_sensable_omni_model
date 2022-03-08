# launchOmni
This code is written to launch a ros node with the urdf robot description as a parameter. It is based on this tutorial: https://docs.ros.org/en/foxy/Tutorials/URDF/Using-URDF-with-Robot-State-Publisher.html

Steps: 

1. Create a ros2 workspace with the src code inside
2. Run the following: 

```
colcon build --symlink-install --packages-select omni 
source install/setup.bash
ros2 launch omni demo.launch.py # To launch the ros node and parameters
rviz2 -d ~/<workspace_name>/install/omni/share/omni/omni.rviz # to launch rviz with the omni frames

```


