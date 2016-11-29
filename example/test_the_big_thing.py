import sys
import os
path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(path))

from rubytojson import ruby_to_json
from json import loads

import pytest


def test_do_the_thing():
    result = ruby_to_json("require '%s/the_big_thing.rb'; TheBigThing.do_the_thing({lawyers: true})" % path)
    assert result == 'true'


def test_do_the_thing_failure():
    result = ruby_to_json("require '%s/the_big_thing.rb'; TheBigThing.do_the_thing()" % path)
    assert result == '"Send lawyers, guns or money!"'


def test_do_the_thing_exception():
    result = ruby_to_json("require '%s/the_big_thing.rb'; TheBigThing.do_the_thing({lawyers: true}, 'extra_arg')" % path)
    assert result == '"wrong number of arguments (2 for 1)"'
