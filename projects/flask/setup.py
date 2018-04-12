from setuptools import setup

requires = [
    'Flask',
    'zeptrionAirApi',
    'aiohttp'
]

setup(
    name='Swissglider Apps',
    include_package_data=True,
    zip_safe=False,
    install_requires=requires
)
