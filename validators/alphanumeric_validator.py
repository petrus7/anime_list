import re

from validators.base_validator import Validator


class IsAlphanumericValidator(Validator):

    def validate(self):
        if re.match('^[0-9a-zA-Z]*$', self.data):
            return True
        return False
