import os.path
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), "readme.md")) as f:
    long_description = f.read()

about = {}
with open(os.path.join(os.path.dirname(__file__), "khan_dl", "__version__.py")) as f:
    exec(f.read(), about)

setup(
    name=about["__title__"],
    packages=["khan_dl"],
    version=about["__version__"],
    description=about["__description__"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    license=about["__license__"],
    author=about["__author__"],
    author_email=about["__author_email__"],
    url=about["__url__"],
    download_url="https://github.com/rand-net/khan-dl/archive/2021.02.15.tar.gz",
    keywords=[
        "khan academy",
        "khan academy downloader",
        "course downloader",
        "video downloader",
    ],
    install_requires=["beautifulsoup4", "youtube_dl", "prompt-toolkit", "requests"],
    classifiers=[
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    entry_points={"console_scripts": ["khan-dl = khan_dl.cli:main"]},
    project_urls={
        "Source": "https://github.com/rand-net/khan-dl",
        "Tracker": "https://github.com/rand-net/khan-dl/issues",
    },
)
