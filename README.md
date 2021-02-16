# khan-dl

A python script to download courses from  [Khan Academy](https://www.khanacademy.org) using [youtube-dl](https://github.com/ytdl-org/youtube-dl) and [beautifulsoup4](https://pypi.org/project/beautifulsoup4/).

## Installation

* Using pip

```
pip install khan-dl

```

* From Source
```
git clone https://github.com/rand-net/khan-dl
cd khan-dl
pip install -r requirements.txt
```

## Usage

```
$ khan-dl -h

usage: khan-dl.py [-h] [-i] [-c COURSE_URL]

optional arguments:
  -h, --help            show this help message and exit
  -i, --interactive     Enter Interactive Course Selection Mode
  -c COURSE_URL, --course_url COURSE_URL
                        Enter Course URL
  -a, --all             Download all Courses from all Domains
```

* You can download courses interactively on a prompt, which will list all course
    domains and their respective courses available with tab completion.

```
$ khan-dl -i

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
$  khan-dl -c https://www.khanacademy.org/science/ap-physics-1

```

* Download all courses on traditional subjects like Math, Science, Computing, Humanities, Economics-Finance-Domain.

```
$ khan-dl.py -a

```

* Download all courses on traditional subjects like Math, Science, Computing, Humanities, Economics-Finance-Domain.

```
$ python khan-dl.py -a

```
