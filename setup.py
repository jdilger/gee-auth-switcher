# setup.py
from setuptools import setup

# The directory containing this file
# HERE = pathlib.Path(__file__).parent

# # The text of the README file
# README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name='ee_auth_switcher',
    version='0.0.11',
    description="Simple cli for switching between gee accounts ",
    # long_description=README,
    # long_description_content_type="text/markdown",
    # url="https://github.com/realpython/reader",
    author="John Dilger",
    author_email="johnjdilger@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["ee_auth_switcher"],
    include_package_data=True,
    install_requires=["typer", "earthengine-api"],
    entry_points={
        "console_scripts": [
            "ee_auth=ee_auth_switcher.gee_auth_switcher:app",
        ]
    },
)
