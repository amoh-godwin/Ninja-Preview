from setuptools import setup, find_packages
setup(
    name="Ninja_Preview",
    version="0.3beta",
    packages=find_packages(),
    install_requires=['PyQt5 >= 5.10', 'Qmlview'],
    entry_points={
            'gui_scripts': ['Ninja_Preview = Ninja_Preview.Ninja_preview:dummy_run'],
    },
    
    author="Amoh - Gyebi Godwin Ampofo Michael",
    author_email="amohgyebigodwin@gmail.com",
    description="An alternative to qmlscene",
    keywords="qmlview, qmlscene, qml, pyqt, pyqt5, pyside, pyside2",
    url="http://example.com/HelloWorld/",   # project home page, if any
    project_urls={
        "Bug Tracker": "https://bugs.example.com/HelloWorld/",
        "Documentation": "https://docs.example.com/HelloWorld/",
        "Source Code": "https://code.example.com/HelloWorld/",
    },
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    long_description = """\
    Qmlview is a command line utility. But sort of to replace the non-existent
    qmlscene, which was used to preview qml source code before it is loaded
    by any C++, Java, or python code.
    """
    
)
