from setuptools import setup, find_packages
setup(
    name="Ninja_Preview",
    version="0.1",
    packages=find_packages(),
    install_requires=['PyQt5 >= 5.10', 'Qmlview'],
    entry_points={
            'console_scripts': ['Ninja_Preview = Ninja_Preview.Ninja_preview:dummy_run'],
    }
)
