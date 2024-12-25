import utils


def test_calculate_area_of_a_rectange():#intr
    length = 8
    width = 10
    expected_result = 80
    actual_result = utils.calculate_area_of_a_rectange(length=length, width=width)
    assert actual_result == expected_result


def test_calculate_area_of_a_rectange_without_length():#float
    length = 8
    width = 10
    expected_result = width * width
    actual_result = utils.calculate_area_of_a_rectange(length=length, width=width)
    assert actual_result == expected_result


def test_calculate_area_of_a_rectange_without_width():#float with intr
    length = 8
    width = 10
    expected_result = length * length
    actual_result = utils.calculate_area_of_a_rectange(length=length, width=width)
    assert actual_result == expected_result
