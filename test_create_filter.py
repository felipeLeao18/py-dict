from app import create_filter

def test_create_filter_with_no_arguments():
    assert create_filter() == []

def test_create_filter_with_one_argument():
    assert create_filter('_id') == ['_id']

def test_create_filter_with_several_arguments():
    assert create_filter('_id;title;description') == ['_id', 'title', 'description']

def test_create_filter_with_arguments_and_empy_spaces():
    assert create_filter('  _id ; title ; description ; release_year') == ['_id', 'title', 'description', 'release_year']

   