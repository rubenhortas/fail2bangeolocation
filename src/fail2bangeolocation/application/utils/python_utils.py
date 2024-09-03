from sys import version_info


def get_python_interpreter_version() -> str:
    major, minor, micro, release_level, serial = version_info

    return major
