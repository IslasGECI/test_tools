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
    obtained_hash = hashlib.md5(file_content).hexdigest()
    assert obtained_hash == "345"


def write_dummy_file(output_path):
    f = open(output_path, "w")
    f.write("Woops! I have deleted the content!")
    f.close()
