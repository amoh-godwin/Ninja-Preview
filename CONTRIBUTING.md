# Contributing
To contribute you should fork the repository.
Then you should make your changes to either the development, develop-linux, develop-win, setuptools branch
according to your system.

- development: general
- develop-linux: for unix systems
- develop-win: for win systems
- setuptools: for pypi.org


## Dependencies

### PyQt5
```pip install PyQt5```

### Qmlview
Please use a Qmlview release for mac or one that you have built yourself.
Doing pip install Qmlview will download Qmlview alright, but can cause conflict with path system.
In a develop-... branch:
you can have it in the App folder, see the README.md in that folder for more, nonetheless, developing without it, is recommemded.


## Test Build
To Build you will need to instsall pyinstaller or setuptools or both
```pip install pyinstaller```
```pip install setuptools```

### Edit the spec, setup.py file

Now change the Ninja-preview.spec or setup.py file to reflect you local mac path.

For PyInstaller:
```pyinstaller ./Ninja-preview.spec```

For Setuptools
```python setup.py sdist```

Add all the contents of Qmlview to the contents of the
/dist/Ninja-Preview folder, 
so that Ninja-Preview will contain Qmlview
Please accept to overwrite the conflicting files.
