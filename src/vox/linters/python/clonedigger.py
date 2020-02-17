import vox
from vox import linty, flaggy
from ..base_linter import BaseLinter


class Clonedigger(BaseLinter):
    COMMAND = (
        vox .FlagsBuilder()
            .sugar(program='clonedigger')
    )
    DEPENDENCIES = ['clonedigger']
    FORMAT = None
    NAME = 'clonedigger'
    PYTHON = '2.7'
    extract_errors = linty.from_str.echo
