from django.core.exceptions import ValidationError


def validate_non_negative(value):
    """
    Validates that the provided value is non-negative (i.e., greater than or equal to 0).
    Raises a ValidationError if the condition is not met.
    """
    if value < 0:
        raise ValidationError(f'{value} is not a non-negative number')


def validate_positive(value):
    """
    Validates that the provided value is positive (i.e., greater than 0).
    Raises a ValidationError if the condition is not met.
    """
    if value <= 0:
        raise ValidationError(f'{value} must be a positive number')
