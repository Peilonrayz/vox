import vox
from vox import linty, flaggy
from ..base_linter import BaseLinter


class Pyroma(BaseLinter):
    COMMAND = (
        vox .FlagsBuilder()
            .sugar(program='pyroma', files='.')
    )
    DEPENDENCIES = ['pyroma']
    FORMAT = None
    NAME = 'pyroma'
    extract_errors = linty.from_str.pyroma
