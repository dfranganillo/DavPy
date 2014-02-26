DavPy
=====

Simple wrapper to work with Basic Auth webdavs. Compatible python 2.6,
2.7, 3

Install
=======

    `pip`_ install `davpy`_

Or

    `easy\_install`_ `davpy`_

Or manual way

    python setup.py install

Source code

    `github`_

Using API
=========

    davfs = DavPy({ "user": username, "password": password, "host": dav host, if empty defaults to webdav.yandex.ru, "retry\_limit": if empty defaults to 3 })

    davfs.list(u"/") # list files and folder in root folder at remote server

    davfs.sync(u"local folder", u"remote folder for upload files from local folder")

    davfs.mkdir(u"path to remote folder, which you need to create")

    davfs.download(u"path to remote file which your need to download")
    #function return file in bytearray

    davfs.downloadTo(u"path to remote file which your need to download", u"local path to save file"):

    davfs.delete(u"Delete remote file")

    davfs.upload(u"path to local file", u"remote path for uploading file")

.. _pip: https://pypi.python.org/pypi/pip/
.. _davpy: https://pypi.python.org/pypi/davpy
.. _easy\_install: https://pypi.python.org/pypi/setuptools
.. _github: https://github.com/dfranganillo/davpy
