import vox
from vox import linty, flaggy
from ..base_linter import BaseLinter


class Pylama(BaseLinter):
    COMMAND = (
        vox .FlagsBuilder()
            .sugar(program='pylama')
    )
    DEPENDENCIES = ['pylama']
    FORMAT = linty.to_str.PYLAMA
    NAME = 'pylama'
    extract_errors = linty.from_str.pylama
