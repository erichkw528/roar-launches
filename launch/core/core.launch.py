"""
Launches all Carla launch files

"""
import os
import launch
from ament_index_python.packages import get_package_share_directory
import launch_ros
from pathlib import Path
from launch_ros.actions import Node
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import LogInfo
from launch.actions import GroupAction
from launch_ros.actions import SetRemap

def generate_launch_description():
    """ URDF """
    ld = launch.LaunchDescription()
    base_path = Path(get_package_share_directory("roar-urdf"))
    urdf_launch_path = base_path / "launch" / "state_publisher.launch.py"
    assert urdf_launch_path.exists(), f"{urdf_launch_path} does not exist"
    urdf_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(urdf_launch_path.as_posix()),
    )
    ld.add_action(urdf_launch)
    return ld
    
