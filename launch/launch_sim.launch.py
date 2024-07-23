import os


from ament_index_python.packages import get_package_share_directory


from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node

# from launch.actions import (DeclareLaunchArgument, EmitEvent, LogInfo,
#                             RegisterEventHandler)
# from launch.conditions import IfCondition
# from launch.events import matches_action
# from launch.substitutions import (AndSubstitution, LaunchConfiguration,
#                                   NotSubstitution)
# from launch_ros.actions import LifecycleNode
# from launch_ros.event_handlers import OnStateTransition
# from launch_ros.events.lifecycle import ChangeState
# from lifecycle_msgs.msg import Transition

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
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')]) ,
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
    # autostart = LaunchConfiguration('autostart')
    # use_lifecycle_manager = LaunchConfiguration("use_lifecycle_manager")
    # use_sim_time = LaunchConfiguration('use_sim_time')
    # slam_params_file = LaunchConfiguration('slam_params_file')

    # declare_autostart_cmd = DeclareLaunchArgument(
    #     'autostart', default_value='true',
    #     description='Automatically startup the slamtoolbox. '
    #                 'Ignored when use_lifecycle_manager is true.')
    # declare_use_lifecycle_manager = DeclareLaunchArgument(
    #     'use_lifecycle_manager', default_value='false',
    #     description='Enable bond connection during node activation')
    # declare_use_sim_time_argument = DeclareLaunchArgument(
    #     'use_sim_time',
    #     default_value='true',
    #     description='Use simulation/Gazebo clock')
    # declare_slam_params_file_cmd = DeclareLaunchArgument(
    #     'slam_params_file',
    #     default_value=os.path.join(get_package_share_directory("slam_toolbox"),
    #                                'config', './ros2_ws/mobile_robot/src/mok_mobile_robot/config/mapper_params_online_async_local.yaml'),
    #     description='Full path to the ROS2 parameters file to use for the slam_toolbox node')

    # start_async_slam_toolbox_node = LifecycleNode(
    #     parameters=[
    #       slam_params_file,
    #       {
    #         'use_lifecycle_manager': use_lifecycle_manager,
    #         'use_sim_time': use_sim_time
    #       }
    #     ],
    #     package='slam_toolbox',
    #     executable='async_slam_toolbox_node',
    #     name='slam_toolbox',
    #     output='screen',
    #     namespace=''
    # )

    # configure_event = EmitEvent(
    #     event=ChangeState(
    #       lifecycle_node_matcher=matches_action(start_async_slam_toolbox_node),
    #       transition_id=Transition.TRANSITION_CONFIGURE
    #     ),
    #     condition=IfCondition(AndSubstitution(autostart, NotSubstitution(use_lifecycle_manager)))
    # )

    # activate_event = RegisterEventHandler(
    #     OnStateTransition(
    #         target_lifecycle_node=start_async_slam_toolbox_node,
    #         start_state="configuring",
    #         goal_state="inactive",
    #         entities=[
    #             LogInfo(msg="[LifecycleLaunch] Slamtoolbox node is activating."),
    #             EmitEvent(event=ChangeState(
    #                 lifecycle_node_matcher=matches_action(start_async_slam_toolbox_node),
    #                 transition_id=Transition.TRANSITION_ACTIVATE
    #             ))
    #         ]
    #     ),
    #     condition=IfCondition(AndSubstitution(autostart, NotSubstitution(use_lifecycle_manager)))
    # )



    # Launch them all!
    return LaunchDescription([
        rsp,
        gazebo,
        spawn_entity,
        rviz_node,
        # autostart,
        # use_lifecycle_manager,
        # use_sim_time,
        # slam_params_file,
        # declare_autostart_cmd,
        # declare_use_lifecycle_manager,
        # declare_use_sim_time_argument,
        # declare_slam_params_file_cmd,
        # configure_event,
        # activate_event
    ])


