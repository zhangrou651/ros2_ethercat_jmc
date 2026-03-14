from setuptools import find_packages, setup
import glob
import os
package_name = 'jobot_protocol_bringup'

setup(
        name=package_name,
        version='0.0.0',
        packages=find_packages(exclude=['test']),
        data_files=[
            ('share/ament_index/resource_index/packages',
             ['resource/' + package_name]),
            ('share/' + package_name, ['package.xml']),
            (os.path.join('share', package_name, 'launch'), glob.glob('launch/*.py')),
            # 3. 安装 config 目录（包含所有 .yaml 和 .xacro 文件）
            (os.path.join('share', package_name, 'config'),  # 目标路径：install/share/<包名>/config
             [os.path.join('config', f) for f in os.listdir('config')
              if f.endswith(('.yaml', '.xacro'))]),  # 匹配 config 下所有 yaml/xacro 文件

             # 4. 安装 description 目录（包含所有子目录和 .xacro/.xml/.yaml 文件）
             (os.path.join('share', package_name, 'description/config'),  # 目标路径：install/share/<包名>/description/config
              [os.path.join('description/config', f) for f in os.listdir('description/config')
               if f.endswith(('.xacro', '.xml', '.yaml'))]),  # description/config 下的文件

              (os.path.join('share', package_name, 'description/ros2_control'),  # 目标路径：install/share/<包名>/description/ros2_control
               [os.path.join('description/ros2_control', f) for f in os.listdir('description/ros2_control')
                if f.endswith(('.xacro', '.xml', '.yaml'))]),  # description/ros2_control 下的文件

               ],
        install_requires=['setuptools'],
    zip_safe=True,
    maintainer='bianbu',
    maintainer_email='zhaoqi.chen@spacemit.com',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
