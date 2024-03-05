import geci_test_tools as gtt
import os


def test_if_exist_remove():
    output_path = "tests/demofile3.txt"
    write_dummy_file(output_path)
    assert_not_exist(output_path)
    gtt.if_exist_remove(output_path)
    assert_not_exist(output_path)


def write_dummy_file(output_path):
    f = open(output_path, "w")
    f.write("Woops! I have deleted the content!")
    f.close()


def assert_not_exist(output_path):
    assert not (os.path.exists(output_path))
