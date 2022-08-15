from app import apply_filter

dict_array = [{
    '_id': '1',
    'title': 'title 1',
    'description': 'description 1',
    'release_year': '2000'
}, {
    '_id': '2',
    'title': 'title 2',
    'description': 'description 2',
    'release_year': '2001'
}]

def test_apply_filter_with_empty_filter():
    filter = []
    assert apply_filter(filter, dict_array) == dict_array

def test_apply_filter_with_title_only():
    filter = ['title']
    assert apply_filter(filter, dict_array) == [{'title': 'title 1'}, {'title': 'title 2'}]

def test_apply_filter_with_invalid_filter_argument():
    filter = ['title', 'age']
    assert apply_filter(filter, dict_array) == [
        {'title': 'title 1'},
        {'title': 'title 2'}
    ]


def test_apply_filter_with_several_arguments():
    filter = ['title', 'description', 'release_year']
    assert apply_filter(filter, dict_array) == [
        {'title': 'title 1', 'description': 'description 1', 'release_year': '2000'}, 
        {'title': 'title 2', 'description': 'description 2', 'release_year': '2001'}
    ]

   