import utils


def test_calculate_area_of_a_rectange_with_int_numbers():  # int
    length = 8
    width = 10
    expected_result = 80
    actual_result = utils.calculate_area_of_a_rectange(length=length, width=width)
    assert actual_result == expected_result


def test_calculate_area_of_a_rectange_with_float_numbers():  # float
    length = 2.5
    width = 3.4
    expected_result = 8.5
    actual_result = utils.calculate_area_of_a_rectange(length=length, width=width)
    assert actual_result == expected_result


def test_calculate_area_of_a_rectange_with_float_and_int_numbers():  # float with int
    length = 7
    width = 5.3
    expected_result = 37.1
    actual_result = utils.calculate_area_of_a_rectange(length=length, width=width)
    assert actual_result == expected_result
