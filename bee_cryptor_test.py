import bee_cryptor
def test_convert_to_index_list_basic():
    #setup
    expected = [7, 17, 8, 10, 6, 62, 5, 4, 93, 0, 60, 92, 69, 76, 76, 79]
    #invoke
    actual = bee_cryptor.convert_to_index_list("'1(*&^%$} \|ello")
    #analyze
    assert expected==actual