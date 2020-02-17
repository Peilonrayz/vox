import vox
from vox import linty, flaggy
from ..base_linter import BaseLinter


class RadonCC(BaseLinter):
    COMMAND = (
        vox .FlagsBuilder()
            .sugar(program='radon cc -nc')
    )
    DEPENDENCIES = ['radon']
    FORMAT = linty.to_str.RADON
    NAME = 'radon-cc'
    extract_errors = linty.from_str.radon
