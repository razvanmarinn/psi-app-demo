import sys
import os

# Get the parent directory of the current file (test.py)
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)

# Add the parent directory to sys.path
sys.path.insert(0, parent_dir)

from app.src.main import hello_world

def test_hello_world():
    asd = hello_world()
    assert asd == "Hello world!"
    assert len(asd)==12