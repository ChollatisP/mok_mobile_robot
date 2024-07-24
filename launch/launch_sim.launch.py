import os


from ament_index_python.packages import get_package_share_directory


from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node

from launch.actions import DeclareLaunchArgument
from launch.events import matches_action
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():


    # Include the robot_state_publisher launch file, provided by our own package. Force sim time to be enabled
    # !!! MAKE SURE YOU SET THE PACKAGE NAME CORRECTLY !!!

    package_name='mok_mobile_robot' #<--- CHANGE ME

    rsp = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory(package_name),'launch','rsp.launch.py'
                )]), launch_arguments={'use_sim_time': 'true'}.items()
    )

    # Include the Gazebo launch file, provided by the gazebo_ros package
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')
        ]),
        launch_arguments={'world': os.path.join(get_package_share_directory('mok_mobile_robot'), 'worlds', 'room.world')}.items()
    )

    # Run the spawner node from the gazebo_ros package. The entity name doesn't really matter if you only have a single robot.
    spawn_entity = Node(package='gazebo_ros', executable='spawn_entity.py',
                        arguments=['-topic', 'robot_description',
                                   '-entity', 'my_bot'],
                        output='screen')
    rviz_node = Node(
            package='rviz2',
            namespace='',
            executable='rviz2',
            name='rviz2',
            arguments=['-d' + os.path.join(get_package_share_directory('mok_mobile_robot'), 'config', 'config_file.rviz')]
        )
    # use_sim_time = LaunchConfiguration('use_sim_time')
    # slam_params_file = LaunchConfiguration('slam_params_file')

    # declare_use_sim_time_argument = DeclareLaunchArgument(
    #     'use_sim_time',
    #     default_value='true',
    #     description='Use simulation/Gazebo clock')
    # declare_slam_params_file_cmd = DeclareLaunchArgument(
    #     'slam_params_file',
    #     default_value=os.path.join(get_package_share_directory("mok_mobile_robot"),
    #                                'config', 'mapper_params_online_async_local.yaml'),
    #     description='./ros_ws/mobile_robot/src/mok_mobile_robot/config/mapper_params_online_async_local.yaml')

    # start_async_slam_toolbox_node = Node(
    #     parameters=[
    #       slam_params_file,
    #       {'use_sim_time': use_sim_time}
    #     ],
    #     package='slam_toolbox',
    #     executable='async_slam_toolbox_node',
    #     name='slam_toolbox',
    #     output='screen')



    # Launch them all!
    return LaunchDescription([
        rsp,
        gazebo,
        spawn_entity,
        rviz_node,
        # declare_use_sim_time_argument,
        # declare_slam_params_file_cmd,
        # start_async_slam_toolbox_node
    ])


