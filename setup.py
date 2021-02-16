import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="khan-dl",
    version="0.0.1",
    description="Download courses from khanacademy.org",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/rand-net/khan-dl",
    author="rand-net",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["khan-dl"],
    include_package_data=True,
    install_requires=["feedparser", "html2text"],
)
