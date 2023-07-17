"""
Launches all GoKart launch files

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

def generate_launch_description():
    gokart_sensor_bringup_path: Path = (
        Path(get_package_share_directory("gokart_hardware_launches"))
        / "launch"
        / "gokart_sensor_bringup.launch.py"
    )
    assert (
        gokart_sensor_bringup_path.exists()
    ), f"[{gokart_sensor_bringup_path}] does not exist"
    gokart_sensor_bringup = IncludeLaunchDescription(PythonLaunchDescriptionSource(
            gokart_sensor_bringup_path.as_posix()
        )
    )
    ld = launch.LaunchDescription()
    ld.add_action(gokart_sensor_bringup)
    return ld
    
