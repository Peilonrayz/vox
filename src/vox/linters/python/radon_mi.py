import vox
from vox import linty, flaggy
from ..base_linter import BaseLinter


class RadonMI(BaseLinter):
    COMMAND = (
        vox .FlagsBuilder()
            .sugar(program='radon mi -nb')
    )
    DEPENDENCIES = ['radon']
    FORMAT = linty.to_str.RADON_MI
    NAME = 'radon-mi'
    extract_errors = linty.from_str.radon_mi
