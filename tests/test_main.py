
from wasp.main import WaspTest

def test_wasp(tmp):
    with WaspTest() as app:
        res = app.run()
        print(res)
        raise Exception

def test_command1(tmp):
    argv = ['command1']
    with WaspTest(argv=argv) as app:
        app.run()
