from setuptools import setup

setup(
    name='stockserver',
    packages=['stockserver'],
    include_package_data=True,
    install_requires=[
	'flask',
    ],
)
