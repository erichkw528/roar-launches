from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from launch.actions import DeclareLaunchArgument, LogInfo, ExecuteProcess
from launch.conditions import IfCondition #1
from launch.substitutions import LaunchConfiguration
from launch.actions import IncludeLaunchDescription
import launch

import os
from pathlib import Path

def generate_launch_description():
    print("entered pointonenav launch")
    ld = LaunchDescription()
    pointonenav_base = Path(get_package_share_directory("point_one_gps_driver"))
    pointonenav_launch_path = (pointonenav_base / "launch" / "point_one_gps_driver.launch.py").as_posix()
    ld.add_action(LogInfo(msg=f"pointonenav_launch_path: {pointonenav_launch_path}"))
    ld.add_action(ExecuteProcess(cmd=['curl', '-X', 'POST', 'http://10.0.0.2/api/v1/application/start'],
                                 output='screen',
                                 condition=LaunchConfigurationEquals("pointonenav", "true") 
                                 ))
    pointonenav_launch = IncludeLaunchDescription(
        launch.launch_description_sources.PythonLaunchDescriptionSource(pointonenav_launch_path),
    )
    delayed_actions = launch.actions.TimerAction(
        period=5.0,
        actions=[pointonenav_launch],
        condition=LaunchConfigurationEquals("pointonenav", "true") 
    )
    ld.add_action(delayed_actions)

    return ld
# start_navigation = IncludeLaunchDescription(condition=LaunchConfigurationEquals("pointonenav", "true"))
        
