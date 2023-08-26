import pytest

from utils import dicts

@pytest.fixture
def our_fixture():
    return {"vcs": "mercurial"}

def test_get_val(our_fixture):
      assert dicts.get_val(our_fixture, "vcs") == "mercurial" # no default
      assert dicts.get_val(our_fixture, "vcs", "git") == "mercurial" # with default
      assert dicts.get_val({}, "vcs", "git") == "git" # no value
      assert dicts.get_val({}, "vcs", "bazaar") == "bazaar"  # other default
