# khan-dl

A python script to download courses from  [Khan Academy](https://www.khanacademy.org) using [youtube-dl](https://github.com/ytdl-org/youtube-dl) and [beautifulsoup4](https://pypi.org/project/beautifulsoup4/).

## Installation

```
git clone https://github.com/rand-net/khan-dl
cd khan-dl
pip install -r requirements.txt
```

## Usage

```
$ python khan-dl.py -h

usage: khan-dl.py [-h] [-i] [-c COURSE_URL]

optional arguments:
  -h, --help            show this help message and exit
  -i, --interactive     Enter Interactive Course Selection Mode
  -c COURSE_URL, --course_url COURSE_URL
                        Enter Course URL
```

* You can download courses interactively on a prompt, which will list all course
    domains and their respective courses available with tab completion.

```
$ python khan-dl.py -i

Course Domain: Math
Selected Course Domain: Math

Downloading Course List...

Course: Linear algebra

Selected Course Domain: Linear algebra

Generating Path Slugs.....

Downloading Videos....

```

* Download a specific course.

```
$ python khan-dl.py -c https://www.khanacademy.org/science/ap-physics-1

```
