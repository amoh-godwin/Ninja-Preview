from setuptools import setup, find_packages
setup(
    name="Ninja_Preview",
    version="1.1",
    packages=find_packages(),
    install_requires=['PyQt5 >= 5.10', 'Qmlview >= 1.1'],
    entry_points={
            'gui_scripts': ['Ninja_Preview = Ninja_Preview.Ninja_preview:dummy_run'],
    },
    
    author="Amoh - Gyebi Godwin Ampofo Michael",
    author_email="amohgyebigodwin@gmail.com",
    description="A preview for your Qml files",
    keywords="qmlview, qmlscene, qml, pyqt, pyqt5, pyside, pyside2",
    url="https://github.com/amoh-godwin/Ninja-Preview/",   # project home page, if any
    project_urls={
        "Bug Tracker": "https://github.com/amoh-godwin/Ninja-Preview/issues/",
        "Documentation": "https://github.com/amoh-godwin/Ninja-Preview/wiki/",
        "Source Code": "https://github.com/amoh-godwin/Ninja-Preview/",
    },
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    long_description = """\
    Ninja_Preview is a Graphical User Interface that aims at letting you 
    use qmlview, which is just like qmlscene in a more flexible way, since 
    both do not provide with Graphical User Interfaces.
    """
    
)
