import vox
from vox import linty, flaggy
from ..base_linter import BaseLinter


class DetectSecrets(BaseLinter):
    COMMAND = (
        vox .FlagsBuilder()
            .sugar(program='detect-secrets scan --all-files')
    )
    DEPENDENCIES = ['detect-secrets']
    FORMAT = None
    NAME = 'detect-secrets'
    extract_errors = linty.from_str.detect_secrets
