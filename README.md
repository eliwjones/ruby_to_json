Ruby To JSON
============

This is a brutish approach I've used when replacing an existing system written in Ruby.
If the new system is being written in python, one just needs to write out py.tests
that run both the Ruby and the Python processes using the same arguments and then asserts
that the output matches.


Example usage:
```
sudo pip install pytest
git checkout ruby_to_json
cd ruby_to_json
py.test example
```

Example output:
```
mrz@mrzsss:~/eliwjones/repos/ruby_to_json$ py.test -v example
=================================== test session starts ===================================
platform linux2 -- Python 2.7.6, pytest-3.0.2, py-1.4.31, pluggy-0.3.1 -- /usr/bin/python
cachedir: .cache
rootdir: /home/mrz/eliwjones/repos/ruby_to_json, inifile:
collected 3 items

example/test_the_big_thing.py::test_do_the_thing PASSED
example/test_the_big_thing.py::test_do_the_thing_failure PASSED
example/test_the_big_thing.py::test_do_the_thing_exception PASSED

================================ 3 passed in 0.13 seconds =================================
mrz@mrzsss:~/eliwjones/repos/ruby_to_json$
```
