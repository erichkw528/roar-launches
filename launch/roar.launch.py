"""
main ROAR launch file
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

def generate_launch_description():
    ld = launch.LaunchDescription()

    """
    Gokart section
    """
    should_launch_gokart = DeclareLaunchArgument('gokart', default_value="False", description="Launches gokart drivers") 
    ld.add_action(should_launch_gokart)

    gokart_launch_path: Path = (
        Path(get_package_share_directory("roar-indy-launches"))
        / "launch" / "gokart"
        / "gokart.launch.py"
    )
    assert (
        gokart_launch_path.exists()
    ), f"[{gokart_launch_path}] does not exist"
    hardware_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(gokart_launch_path.as_posix()),
        condition=IfCondition(LaunchConfiguration('gokart', default=False))  
    )
    ld.add_action(hardware_launch)
    ld.add_action(LogInfo(msg=["Gokart launched"], condition=IfCondition(LaunchConfiguration('gokart', default=False))))

    """
    Carla section
    """
    should_launch_carla_client = DeclareLaunchArgument('carla', default_value="False", description="Launches carla client") 
    ld.add_action(should_launch_carla_client)

    carla_launch_path: Path = (
        Path(get_package_share_directory("roar-indy-launches"))
        / "launch" / "carla"
        / "carla.launch.py"
    )
    assert (
        carla_launch_path.exists()
    ), f"[{carla_launch_path}] does not exist"
    carla_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(carla_launch_path.as_posix()),
        condition=IfCondition(LaunchConfiguration('carla', default=False))  
    )
    ld.add_action(carla_launch)
    ld.add_action(LogInfo(msg=["carla launched"], condition=IfCondition(LaunchConfiguration('carla', default=False))))

    """
    Core auto drive section
    """
    should_launch_core = DeclareLaunchArgument('core', default_value="False", description="Launches core auto drive logics")
    ld.add_action(should_launch_core)

    core_launch_path: Path = (
        Path(get_package_share_directory("roar-indy-launches"))
        / "launch" / "core"
        / "core.launch.py"
    )
    assert (
        core_launch_path.exists()
    ), f"[{core_launch_path}] does not exist"
    core_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(core_launch_path.as_posix()),
        condition=IfCondition(LaunchConfiguration('core', default=False))  
    )
    ld.add_action(core_launch)
    ld.add_action(LogInfo(msg=["Core launched"], condition=IfCondition(LaunchConfiguration('core', default=False))))

    """
    Visualization section
    """
    should_launch_visualization = DeclareLaunchArgument('visualization', default_value="False", description="Launch visualization")
    ld.add_action(should_launch_visualization)

    should_launch_manual_control = DeclareLaunchArgument('manual_control', default_value="False", description="Launch manual control")
    ld.add_action(should_launch_manual_control)

    visualization_launch_path: Path = (
        Path(get_package_share_directory("roar-indy-launches"))
        / "launch" / "visualization"
        / "visualization.launch.py"
    )
    assert (
        visualization_launch_path.exists()
    ), f"[{visualization_launch_path}] does not exist"
    visualization_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(visualization_launch_path.as_posix()),
        condition=IfCondition(LaunchConfiguration('visualization', default=False))
    )
    ld.add_action(visualization_launch)
    ld.add_action(LogInfo(msg=["Visualization launched"], condition=IfCondition(LaunchConfiguration('visualization', default=False))))

    """
    Manual control section
    """
    manual_control_launch_path: Path = Path(get_package_share_directory("roar_manual_control")) / "launch" / "roar_manual_control.launch.py"
    assert (
        manual_control_launch_path.exists()
    ), f"[{manual_control_launch_path}] does not exist"
    manual_control_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(manual_control_launch_path.as_posix()),
        condition=IfCondition(LaunchConfiguration('manual_control', default=False))
        )
    ld.add_action(LogInfo(msg=["manual_control launched"], condition=IfCondition(LaunchConfiguration('manual_control', default=False))))
    ld.add_action(manual_control_launch)
    return ld
    
