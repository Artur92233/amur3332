import utils


def test_calculate_area_of_a_rectange():
    length = 8
    width = 10
    expected_result = length * width
    actual_result = utils.calculate_area_of_a_rectange(length=length, width=width)
    assert actual_result == expected_result


def test_calculate_area_of_a_rectange_without_length():
    length = 8
    width = 10
    expected_result = length * length
    actual_result = utils.calculate_area_of_a_rectange(length=length, width=width)
    assert actual_result == expected_result


def test_calculate_area_of_a_rectange_whithout_width():
    length = 8
    width = 10
    expected_result = width * width
    actual_result = utils.calculate_area_of_a_rectange(length=length, width=width)
    assert actual_result == expected_result
