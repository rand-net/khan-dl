# khan-dl

A python script to download courses from  [Khan Academy](https://www.khanacademy.org) using [youtube-dl](https://github.com/ytdl-org/youtube-dl) and [beautifulsoup4](https://pypi.org/project/beautifulsoup4/).

![PyPI](https://img.shields.io/pypi/v/khan-dl?style=flat-square)
![GitHub](https://img.shields.io/github/license/rand-net/khan-dl?style=flat-square)


## Installation

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
 _  __ _   _     _     _   _         ____   _
| |/ /| | | |   / \   | \ | |       |  _ \ | |
| ' / | |_| |  / _ \  |  \| | _____ | | | || |
| . \ |  _  | / ___ \ | |\  ||_____|| |_| || |___
|_|\_\|_| |_|/_/   \_\|_| \_|       |____/ |_____|



Domain: Math
Selected Domain: math

Downloading Courses...

Course: Early math
Selected Course: Early math


Course URL: https://www.khanacademy.org/math/early-math

Generating Path Slugs.....
```

* Download a specific course.

```
$  khan-dl -c "https://www.khanacademy.org/math/early-math"
 _  __ _   _     _     _   _         ____   _
| |/ /| | | |   / \   | \ | |       |  _ \ | |
| ' / | |_| |  / _ \  |  \| | _____ | | | || |
| . \ |  _  | / ___ \ | |\  ||_____|| |_| || |___
|_|\_\|_| |_|/_/   \_\|_| \_|       |____/ |_____|


Looking up https://www.khanacademy.org/math/early-math...

Course URL: https://www.khanacademy.org/math/early-math

Generating Path Slugs...

```

* Download all courses on traditional subjects like Math, Science, Computing, Humanities, Economics-Finance-Domain.

```
$ khan-dl -a

 _  __ _   _     _     _   _         ____   _
| |/ /| | | |   / \   | \ | |       |  _ \ | |
| ' / | |_| |  / _ \  |  \| | _____ | | | || |
| . \ |  _  | / ___ \ | |\  ||_____|| |_| || |___
|_|\_\|_| |_|/_/   \_\|_| \_|       |____/ |_____|


Downloading all Courses from all Domains...
Selected Domain:  math

Downloading Courses...

Selected Domain:  science

Downloading Courses...

Selected Domain:  computing

Downloading Courses...

Selected Domain:  humanities

Downloading Courses...

Selected Domain:  economics-finance-domain

Downloading Courses...

Selected Domain:  ela

Downloading Courses...


Course URL: https://www.khanacademy.org/math/early-math

Generating Path Slugs...
```


## Other solutions

Khan Academy is also available for offline usage through these Open Source projects:

* [Kolibri](https://learningequality.org/kolibri/)
* [Kiwix](https://www.kiwix.org/)
