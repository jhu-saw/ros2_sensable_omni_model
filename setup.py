import os
import glob
import setuptools

package_name = 'sensable_omni_model'

setuptools.setup(
    name = package_name,
    version = '0.0.0',
    packages = [package_name],
    data_files = [
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob.glob('launch/*.py')),
        (os.path.join('share', package_name), glob.glob('urdf/*')),
        (os.path.join('share', package_name), glob.glob('rviz/*')),
        (os.path.join('share', package_name, 'meshes'), glob.glob('meshes/*.stl')),
    ],
    install_requires = ['setuptools'],
    zip_safe = True,
    maintainer = 'Anton Deguet',
    maintainer_email = 'anton.deguet@jhu.edu',
    description = 'URDF and STL files for Sensable Omni',
    license = 'MIT',
    entry_points = {
        'console_scripts': [
            'pretend_omni_joint_state_publisher = sensable_omni_model.pretend_omni_joint_state_publisher:main'
        ],
    },
)
