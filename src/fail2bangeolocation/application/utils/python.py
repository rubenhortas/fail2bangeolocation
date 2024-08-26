from sys import version_info


def get_interpreter_version():
    major, minor, micro, release_level, serial = version_info

    return major
