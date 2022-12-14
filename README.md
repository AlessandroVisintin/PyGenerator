# PyGenerator
> Small class that eases the generation of a new Python project

PyGenerator is a utility class that automatizes the creation of a new Python project.

## Installation
Clone the project inside your working directory.
You can use it right away by adding the cloned folder into sys.path.
You can also install the package locally by running pip at the root level.
```sh
pip install /path/to/root/level
```

## Usage examples
Create a project template
```py

from PyGenerator.PyGenerator import project
from config.PyGenerator.metadata import META


# generate folder structure for project and add to sys.path
project(META, 'code', overwrite=True, syspath=True)

```


## Meta
Alessandro Visintin - alevise.public@gmail.com

Find me: [@ Twitter](https://twitter.com/analog_cs) [@ Medium](https://medium.com/@analog_cs)

Distributed under the MIT license. See ``LICENSE.txt``.
