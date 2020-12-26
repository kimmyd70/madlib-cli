import pytest
from madlib_cli.madlib_cli import read_template, parse_template, merge

    
# # test read_template on wrong path --passes and prints error on CLI
# def test_read_template_returns_stripped_string():
#     actual = read_template("yellow.txt")
#     expected = None
#     assert actual == expected



# def test_parse_template():
#     actual_stripped, actual_parts = parse_template(
#         "It was a {Adjective} and {Adjective} {Noun}."
#     )
#     expected_stripped = "It was a {} and {} {}."
#     expected_parts = ("Adjective", "Adjective", "Noun")

#     assert actual_stripped == expected_stripped
#     assert actual_parts == expected_parts


# def test_merge():
#     actual = merge("It was a {} and {} {}.", ("dark", "stormy", "night"))
#     expected = "It was a dark and stormy night."
#     assert actual == expected


# test read_template on short example
# def test_read_template_returns_stripped_string():
#     actual = read_template('./madlib_cli/dark_and_stormy_night.txt')
#     expected = "It was a {Adjective} and {Adjective} {Noun}."
#     assert actual == expected
