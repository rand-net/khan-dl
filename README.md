# khan-dl

A python script to download courses from  [Khan Academy](https://www.khanacademy.org) using [youtube-dl](https://github.com/ytdl-org/youtube-dl) and [beautifulsoup4](https://pypi.org/project/beautifulsoup4/).

[![Generic badge](https://img.shields.io/badge/Status-Development-<COLOR>.svg)](https://shields.io/)
![PyPI](https://img.shields.io/pypi/v/khan-dl?style=flat-square)
![GitHub](https://img.shields.io/github/license/rand-net/khan-dl?style=flat-square)


## ⚠ Caution
* Each Unit webpage(https://www.khanacademy.org/math/cc-1st-grade-math/cc-1st-place-value) currently contains more youtube ids than the lessons themselves.
* In order to resolve the wrong file name issue, titles of lessons from the webpage
    and the youtube video have to be matched against one another

* In matching those titles, few of the lesson titles from webpage are quite
divergent from their respective youtube tiles

* Eg., webpage_lesson_title = "Addition and subtraction word problems:gorillas", youtube_id_titles = ["Exercising gorillas", "Comparison word problems: marbles"]. The latter youtube title is more similar, but it is an entirely different video.

* If there is a solution to match these titles, submit a pull request.

* TL;DR Few videos will be saved with wrong file name.


## Installation

* Some videos for certain courses were mixed with different output slugs prior to version 0.1.5
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
