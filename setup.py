import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="khan-dl",
    version="1.2.5",
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
    packages=["khan_dl"],
    include_package_data=True,
    entry_points={"console_scripts": ["khan-dl = khan_dl.__init__:main"]},
    install_requires=[
        "art",
        "beautifulsoup4",
        "prompt-toolkit",
        "requests",
        "lxml",
    ],
    keywords=["khan academy", "khan academy downloader", "video downloader"],
)
