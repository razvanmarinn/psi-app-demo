from main import main

def test_main():
    asd = main()
    assert asd == "Hello world!"
    assert len(asd)==12