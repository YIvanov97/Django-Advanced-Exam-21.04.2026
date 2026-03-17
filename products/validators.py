from re import fullmatch
from typing import Optional
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class InputFieldValidator:
    PATTERN = r"[A-Za-z0-9\s,\-\.\(\)\+']+"

    def __init__(self, message: Optional[str] = 'This field contains invalid characters.'):
        self.message = message

    def __call__(self, value: str):
        if value and not fullmatch(self.PATTERN, value.strip()):
            raise ValidationError(self.message)

@deconstructible
class DigitFieldValidator:
    def __call__(self, value):
        if value and not str(value).isdigit():
            raise ValidationError('This field must contain only digits.')