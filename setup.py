from setuptools import find_packages, setup


setup(
    name=#"nifty-cmap",
    version=#"0.1",
    description=#"A nifty description.",
    author=#"Me",
    author_email=#"my@email.address",
    url=#"https://my.url",
    license=#"MIT",
    py_modules=#["nifty"],
    package_dir={"": "lib"},
    install_requires=["matplotlib"],
)
