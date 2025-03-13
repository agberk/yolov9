from setuptools import setup

packages = [
    'yolov9',
    'yolov9.classify',
    'yolov9.models',
    'yolov9.panoptic',
    'yolov9.segment',
    'yolov9.tools',
    'yolov9.utils'
]

setup(
    name='yolov9',
    version='0.0.1',
    description='YOLOv9',
    author='',
    author_email='',
    url='https://github.com/agberk/yolov9.git',
    packages=packages,
)
