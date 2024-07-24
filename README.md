## Robot Package Template

This is a GitHub template. You can make your own copy by clicking the green "Use this template" button.

It is recommended that you keep the repo/package name the same, but if you do change it, ensure you do a "Find all" using your IDE (or the built-in GitHub IDE by hitting the `.` key) and rename all instances of `mok_mobile_robot` to whatever your project's name is.

Note that each directory currently has at least one file in it to ensure that git tracks the files (and, consequently, that a fresh clone has direcctories present for CMake to find). These example files can be removed if required (and the directories can be removed if `CMakeLists.txt` is adjusted accordingly).

## How to run this project

### First open 3 terminal and run these command

```
ros2 launch mok_mobile_robot launch_sim.launch.py use_sim_time:=true
```

```
ros2 launch mok_mobile_robot slam_toolbox.launch.py use_sim_time:=true
```

```
ros2 launch nav2_bringup bringup_launch.py use_sim_time:=true

```