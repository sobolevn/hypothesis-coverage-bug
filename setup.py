from setuptools import setup

setup(
    name='to_cover',
    version='0.1.0',
    packages=['to_cover'],
    entry_points={
        'hypothesis': ['_ = to_cover.entrypoint']
    },
)
