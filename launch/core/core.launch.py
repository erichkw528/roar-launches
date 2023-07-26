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

    """
    Costmap
    """
    costmap_manager_launch_file_path: Path = (
        Path(get_package_share_directory("costmap_node_manager"))
        / "launch"
        / "costmap_node_manager.launch.py"
    )
    assert costmap_manager_launch_file_path.exists(), f"{costmap_manager_launch_file_path} does not exist"
    costmap_manager = IncludeLaunchDescription(PythonLaunchDescriptionSource(costmap_manager_launch_file_path.as_posix()))
    ld.add_action(costmap_manager)

    """ Global Planner """
    global_planner_path = Path(get_package_share_directory("global_planning")) / "launch" / "global_planning.launch.py"
    assert global_planner_path.exists(), f"{global_planner_path} does not exist"
    global_planner_launch = IncludeLaunchDescription(PythonLaunchDescriptionSource(global_planner_path.as_posix()))
    ld.add_action(global_planner_launch)
    
    """ Local Planner """
    local_planner_manager_launch_file_path: Path = (
        Path(get_package_share_directory("local_planner_manager"))
        / "launch"
        / "local_planner_manager.launch.py"
    )
    assert local_planner_manager_launch_file_path.exists(), f"{local_planner_manager_launch_file_path} does not exist"
    local_planner_manager = IncludeLaunchDescription(PythonLaunchDescriptionSource(
            local_planner_manager_launch_file_path.as_posix()
        )
    )
    ld.add_action(local_planner_manager)


    """ Safety Controller """
    return ld
    
