"""
Launches all GoKart launch files

"""
import os
import launch
from ament_index_python.packages import get_package_share_directory
import launch_ros
from pathlib import Path
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import TimerAction

def generate_launch_description():
    ld = LaunchDescription()
    base_path = Path(get_package_share_directory("roar-indy-launches"))
    rviz_path: Path = base_path / "config" / "core" / "core.rviz"
    assert rviz_path.exists(), f"{rviz_path} does not exist"
    rviz_node = launch_ros.actions.Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2",
        output="screen",
        arguments=["-d", rviz_path.as_posix()],
    )
    
    should_launch_manual_control = DeclareLaunchArgument('manual_control', default_value="False", description="Launch manual control")
    ld.add_action(should_launch_manual_control)
    
    manual_control_launch_path: Path = Path(get_package_share_directory("roar_manual_control")) / "launch" / "manual_control.launch.py"
    assert (
        manual_control_launch_path.exists()
    ), f"[{manual_control_launch_path}] does not exist"
    manual_control_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(manual_control_launch_path.as_posix()),
        condition=IfCondition(LaunchConfiguration('manual_control', default=False))
        )

    delayed_nodes = TimerAction(period=1.0, actions=[rviz_node, manual_control_launch])

    ld.add_action(delayed_nodes)
    return ld
    
