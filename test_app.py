from app import change

def test_change():
    assert [{1: 'Oa Euro'}, {1: 'Zwanzgerl'}, {1: 'Zehnerl'}, {2: 'Zwoa Cent'}] == change(1.34)