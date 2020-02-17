import vox
from vox import linty, flaggy
from ..base_linter import BaseLinter


class Coala(BaseLinter):
    COMMAND = (
        vox .FlagsBuilder()
            .sugar(program='coala --json --files')
    )
    DEPENDENCIES = ['coala-bears']
    FORMAT = None
    NAME = 'coala'
    extract_errors = linty.from_str.echo
