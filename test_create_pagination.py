from app import create_pagination


def test_pagination():
    assert create_pagination() == {'start_range': 0, 'final_range': 9}
    assert create_pagination(2,10) == {'start_range': 10, 'final_range': 19}
    assert create_pagination(3,10) == {'start_range': 20, 'final_range': 29}
    assert create_pagination(4,10) == {'start_range': 30, 'final_range': 39}
