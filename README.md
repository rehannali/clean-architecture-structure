# Clean Architecture Structure
This script create basic Clean Architecture folder structure for Flutter app.

> You could create basic folder struction for Clean Architecture by making script

1. First you need to make it executable by executing
> `$ chmod +x clean-architecture-structure.py`

2. Second you can add it to local bin folder by executiing
> `$ cp clean-architecture-structure.py /usr/local/bin/clean-architecture-structure`

> You can also change name while coping script to bin.

## Usage

**After adding it to bin folder, you can use it by simply type `$ clean-architecture-structure` or whatever you choose name for script**

There are some parameters required for creating structure.

1. You need to enter project directory (By default current working directory will be used).
2. You need to enter feature folder name (By default `feature` will be used or you can use relative directory like `ui/feature` etc.)
3. Enter feature name (Required)
4. Enter TDD (Test Driven Development) value (`True` or `False` By default `False` will be used). this value indicate if you want test folder structure or not.
