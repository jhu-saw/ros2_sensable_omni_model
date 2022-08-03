# Sensable Omni models

This package can be used to launch a `robot_state_publisher` ROS 2 node with the URDF robot description loaded as a parameter.  STL meshes can be found in the `meshes` directory.  It also provides a Python script to publish a joint state and animate a pretend Omni.

# Requirements

ROS 2 is required.  This package has been tested on Ubuntu 20.04 with ROS 2 Galactic.  You will also need a couple of extra packages that might not be installed by default:
```sh
sudo apt install ros-galactic-joint-state-publisher ros-galactic-xacro
```

# Compilation

1. Create a ROS 2 workspace if you don't have one already: `mkdir ~/ros2_ws`
1. Create a source directory in your workspace if needed: `mkdir ~/ros2_ws/src`
1. Clone this repository under `src`: `cd ~/ros2_ws/src; git clone https://github.com/jhu-saw/ros2_sensable_omni_model`
1. Compile this package using `colcon` in the workspace:
  ```sh
  cd ~/ros2_ws; colcon build --packages-select sensable_omni_model
  ```

# Usage

```sh
# don't forget to source after first compilation
source ~/ros2_ws/install/setup.bash
# launch robot state publisher and load the robot description as a parameter
ros2 launch sensable_omni_model omni.launch.py
# to visualize the Omni in rviz...
rviz2 -d ~/ros2_ws/install/sensable_omni_model/share/sensable_omni_model/omni.rviz
```

To create a joint state trajectory from a pretend Omni dancing around, one can use the `pretend_omni` script provided in this repository
```sh
ros2 run sensable_omni_model pretend_omni_joint_state_publisher
```

At that point, the Omni in RViz should be moving around.

# Todo:

* Support namespace.  `--ros-args --remap __ns:=/arm` seems to work for pretend Omni`
