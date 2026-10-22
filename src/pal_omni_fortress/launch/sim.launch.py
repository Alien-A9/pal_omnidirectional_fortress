from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess, SetEnvironmentVariable
from launch.substitutions import EnvironmentVariable, LaunchConfiguration
from launch_ros.actions import Node
from pathlib import Path


def generate_launch_description():
    pkg = Path(get_package_share_directory('pal_omni_fortress'))
    world = pkg / 'worlds' / 'empty.sdf'
    model = pkg / 'models' / 'omni_base' / 'model.sdf'
    gazebo_models_path = str(pkg / 'models')

    x_arg = DeclareLaunchArgument('x', default_value='0.0', description='Initial X position')
    y_arg = DeclareLaunchArgument('y', default_value='0.0', description='Initial Y position')
    yaw_arg = DeclareLaunchArgument('yaw', default_value='0.0', description='Initial Yaw (rad)')

    return LaunchDescription([
        x_arg,
        y_arg,
        yaw_arg,
        SetEnvironmentVariable(
            name='IGN_GAZEBO_RESOURCE_PATH',
            value=[
                gazebo_models_path,
                ':',
                EnvironmentVariable('IGN_GAZEBO_RESOURCE_PATH', default_value=''),
            ],
        ),
        SetEnvironmentVariable(
            name='GZ_SIM_RESOURCE_PATH',
            value=[
                gazebo_models_path,
                ':',
                EnvironmentVariable('GZ_SIM_RESOURCE_PATH', default_value=''),
            ],
        ),
        ExecuteProcess(
            cmd=['ign', 'gazebo', '-r', str(world)],
            output='screen',
            shell=False,
        ),
        Node(
            package='ros_gz_sim',
            executable='create',
            arguments=[
                '-world', 'empty_fortress',
                '-file', str(model),
                '-name', 'omni_base',
                '-x', LaunchConfiguration('x'),
                '-y', LaunchConfiguration('y'),
                '-z', '0.01',
                '-Y', LaunchConfiguration('yaw'),
            ],
            output='screen',
        ),
        Node(
            package='ros_gz_bridge',
            executable='parameter_bridge',
            arguments=[
                '/cmd_vel@geometry_msgs/msg/Twist@ignition.msgs.Twist',
                '/odom@nav_msgs/msg/Odometry[ignition.msgs.Odometry',
                '/scan@sensor_msgs/msg/LaserScan[ignition.msgs.LaserScan',
                '/tf@tf2_msgs/msg/TFMessage[ignition.msgs.Pose_V',
                '/clock@rosgraph_msgs/msg/Clock[ignition.msgs.Clock',
            ],
            output='screen',
        ),
    ])