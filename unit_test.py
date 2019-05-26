from .converter import translate_cirilica, translate_latinica
from collections import namedtuple

class Args(object):
    def __init__(self, text, output=''):
        self.text = text
        self.output = output

latinica = "Njegoš se ljulja na ljuljaški. Čamac plovi na vodi!"
cirilica = "Његош се љуља на љуљашки. Чамац плови на води!"

latinica_file = "latinica_example.txt"
cirilica_file = "cirilica_example.txt"

def test_latinica_to_cirilica_str():
    assert cirilica == translate_latinica(Args(latinica))

def test_cirilica_to_latinica_str():
    assert latinica == translate_cirilica(Args(cirilica))

def test_latinica_to_cirilica_file():
    with open(cirilica_file, 'r', encoding='utf8') as fp:
        cir = fp.read()
    assert cir == translate_latinica(Args(latinica_file))

def test_cirilica_to_latinica_file():
    with open(latinica_file, 'r', encoding='utf8') as fp:
        lat = fp.read()
    assert lat == translate_cirilica(Args(cirilica_file))