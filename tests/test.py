from src.main import hello_world

def test_hello_world():
    asd = hello_world()
    assert asd == "Hello world!"
    assert len(asd)==12