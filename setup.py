from setuptools import setup, find_packages

setup(
    name='THLT',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'thlt = main:MainApplication',
        ],
    },
    install_requires=[
        # danh sách các thư viện cần thiết cho dự án của bạn
    ],
)
