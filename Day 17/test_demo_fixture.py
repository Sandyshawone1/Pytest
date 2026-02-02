#Fixture : Resuable function
import pytest
@pytest.fixture
def setup():
    print("setup browser.....")

def test_one(setup):
    print("this is a test one")

def test_two():
    print("this is a test two")

def test_three():
    print("this is a test three")

