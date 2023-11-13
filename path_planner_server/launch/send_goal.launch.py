from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='path_planner_server',
            executable='initial_pose_pub',
            output='screen'),
    ])