## What is this Repository about?
This repo is a ported version of the Omnidirectional Robot model from PAL ROBOTICS.
As the original PAL robotics implemented this in **Gazebo Classic 11** which is now moved to newer generations of Gazebo, this is the transition.

## How to use this Repository?
This repo contains a simple structure which is **compatible with ROS2 Pkg system** this repo only has `src` bcz when you clone this repo on the local device you can run **Colcon build** to build this package.

## Pre-requisties
1. Ubuntu 22.04
2. ROS2 Humble
3. Gazebo Fortress - Also known as **Ignition** [Gazebo was in Transition to new gen].

## Steps to Follow
### Step - 1
Clone the repo
``` bash
git clone https://github.com/Alien-A9/pal_omnidirectional_fortress.git
```

### Step - 2
Extract the folder
``` bash
# Normal Extraction in File Manager or by using Ubuntu's tar
```

### Step - 3
Open terminal and navigate to the extracted folder and on step inside
``` bash
cd ~/<path to extracted folder>
cd pal_omnidirectional_fortress
```

Verify you are in correct location and you have the `src` folder
``` bash
pwd # Will give a path, it should end with pal_omnidirectional_fortress
ls -l # Should give only 'src' folder
```

### Step - 4
Source ROS2
``` bash
source /opt/ros/humble/setup.bash
```

Build using **Colcon**
``` bash
colcon build --symlink-install
```

### Step - 5
Source the Package
``` bash
source install/setup.bash
```

## Now, the packages are built and ready to control the Robot
### Terminal 1 [Follow these if the Terminal in `NEW`]
1. Source ROS2
``` bash
source /opt/ros/humble/setup.bash
```
2. Source the Package after making sure you are in the ..pal_omnidirectional_fortress directory
``` bash
pwd # Should return a path ending with ../pal_omnidirectional_fortress
source install/setup.bash
```
3. Launch the Gazebo with the **world** and **model**
``` bash
ros2 launch pal_omni_fortress sim.launch.py     # Yes the package name is different
# Gazebo will get launched
```

> NOTE: Verify that Gazebo Fortress is installed before hand.

### Terminal 2
1. Source ROS2 [Same as in Terminal 1]
2. Navigate to the package directory and source the package [Same as in Terminal 1]
3. Now, **Spawn an obstacle**
``` bash
ros2 run pal_omni_fortress spawn_obstacle <obstacle_x>,<obstacle_y>,<obstacle_radius>
# Don't worry if you pressed ENTER
# It will consider the data as INVALID and ask again
```
> For another obstacle you need to **Terminate** the current script & Run again!

### Terminal 3
1. Source ROS2 [Same as in Terminal 1 & 2]
2. Navigate to the package directory and source the package [Same as in Terminal 1 & 2]
3. Run the control script to send the **Target x,y locations**
``` bash
ros2 run pal_omni_fortress safe_controller <x_desired> <y_desired>
# You will see a "Dynamic UI" on terminal for multi target assignment and clearing logs and Plotting plots.
```
