import hashlib
import geci_test_tools as gtt


def test_if_exist_remove():
    output_path = "tests/demofile3.txt"
    write_dummy_file(output_path)
    gtt.assert_exist(output_path)
    gtt.if_exist_remove(output_path)
    gtt.assert_not_exist(output_path)


def test_calculate_hash():
    output_path = "tests/demofile3.txt"
    write_dummy_file(output_path)
    file_content = open(output_path, "rb").read()
    obtained_hash = gtt.calculate_hash()
    assert obtained_hash == "413f18697f9d955c4ffac1e06032721b"


def write_dummy_file(output_path):
    f = open(output_path, "w")
    f.write("Woops! I have deleted the content!")
    f.close()
