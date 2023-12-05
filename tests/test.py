from .. import main

def test_hello_world():
    asd = main.hello_world()
    assert asd == "Hello world!"
    assert len(asd)==12