crawler
=======
Crawler for recursively reading web page and loading photos.

================
Installing Beautiful Soup
If you’re using a recent version of Debian or Ubuntu Linux, you can install Beautiful Soup with the system package manager:

$ apt-get install python-bs4

Beautiful Soup 4 is published through PyPi, so if you can’t install it with the system packager, you can install it with easy_install or pip. The package name is beautifulsoup4, and the same package works on Python 2 and Python 3.

$ easy_install beautifulsoup4

$ pip install beautifulsoup4

(The BeautifulSoup package is probably not what you want. That’s the previous major release, Beautiful Soup 3. Lots of software uses BS3, so it’s still available, but if you’re writing new code you should install beautifulsoup4.)

If you don’t have easy_install or pip installed, you can download the Beautiful Soup 4 source tarball and install it with setup.py.

$ python setup.py install

If all else fails, the license for Beautiful Soup allows you to package the entire library with your application. You can download the tarball, copy its bs4 directory into your application’s codebase, and use Beautiful Soup without installing it at all.

I use Python 2.7 and Python 3.2 to develop Beautiful Soup, but it should work with other recent versions.

Problems after installation
Beautiful Soup is packaged as Python 2 code. When you install it for use with Python 3, it’s automatically converted to Python 3 code. If you don’t install the package, the code won’t be converted. There have also been reports on Windows machines of the wrong version being installed.

If you get the ImportError “No module named HTMLParser”, your problem is that you’re running the Python 2 version of the code under Python 3.

If you get the ImportError “No module named html.parser”, your problem is that you’re running the Python 3 version of the code under Python 2.

In both cases, your best bet is to completely remove the Beautiful Soup installation from your system (including any directory created when you unzipped the tarball) and try the installation again.

If you get the SyntaxError “Invalid syntax” on the line ROOT_TAG_NAME = u'[document]', you need to convert the Python 2 code to Python 3. You can do this either by installing the package:

$ python3 setup.py install

or by manually running Python’s 2to3 conversion script on the bs4 directory:

$ 2to3-3.2 -w bs4
