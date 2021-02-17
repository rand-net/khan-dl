# khan-dl

A python script to download courses from  [Khan Academy](https://www.khanacademy.org) using [youtube-dl](https://github.com/ytdl-org/youtube-dl) and [beautifulsoup4](https://pypi.org/project/beautifulsoup4/).

## Installation

* Some videos for certain courses were mixed with different output slugs prior to version 0.1.4.
* ⚠ Update to the latest version using pip.

```
pip install khan-dl -U

```


## Usage

```
$ khan-dl -h

usage: khan-dl [-h] [-i] [-c COURSE_URL]

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
$ khan-dl -a

```


## Other solutions

Khan Academy is also available for offline usage through these Open Source projects:

* [Kolibri](https://learningequality.org/kolibri/)
* [Kiwix](https://www.kiwix.org/)
