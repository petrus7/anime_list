from validators.base_validator import Validator
import re


class IsDigitValidator(Validator):

    def validate(self):
        if re.match('^[0-9]*$', self.data):
            return True
        return False
