DavPy
==================

Simple wrapper to work with Basic Auth webdavs. 
Compatible python 2.6, 2.7, 3

Source code

> [github](https://github.com/dfranganillo/davpy)

# Using API
```python
conf = Config({
  "user":"<-- username -->",
  "password":"<-- password -->",
  "host": "<-- dav host -->"
})


conf.list(u"/") # list files and folder in root folder at remote server

conf.sync(u"local folder", u"remote folder for upload files from local folder")

conf.mkdir(u"path to remote folder, which you need to create")

conf.download(u"path to remote file which your need to download") #function return file in bytearray

conf.downloadTo(u"path to remote file which your need to download", u"local path to save file"):

conf.delete(u"Delete remote file")

conf.upload(u"path to local file", u"remote path for uploading file")

