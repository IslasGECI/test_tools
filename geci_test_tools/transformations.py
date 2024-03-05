import os


def if_exist_remove(output_path: str) -> None:
    if os.path.exists(output_path):
        os.remove(output_path)
