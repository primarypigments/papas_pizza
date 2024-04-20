from django.core.exceptions import ValidationError
import re


def validate_customer_phone_number(value):
    """
    Validates that the input is a valid phone number format.
    Accepts phone numbers with optional country code, up to 17 digits.
    """
    phone_number_validate = r'^\+?(49)?0?\d{9,17}$'
    if not re.match(phone_number_validate, value):
        raise ValidationError(
            "Phone number must be entered in the format "
            "'+111111111'. Maximum 17 digits.")


def validate_customer_street_address(value):
    """
    Validates that the input is a valid street address using common address characters.
    Limits address length to between 10 and 100 characters.
    """
    if not re.match(r'^[\w\s.,\'-]{10,100}$', value):
        raise ValidationError(
            "Enter a valid street address. Only common address"
            "characters are allowed.")


def validate_customer_city(value):
    """
    Validates that the input is a valid city name.
    Allows letters, spaces, hyphens, and periods, with a length of 2 to 50 characters.
    """
    if not re.match(r'^[\w\s.-]{2,50}$', value):
        raise ValidationError(
        "Enter a valid city name. Only letters, spaces,"
        "hyphens, and periods are allowed.")

def validate_customer_zip_code(value):
    """
    Validates that the input is a valid zip or postal code.
    Supports US formats '12345' or '12345-6789' and UK formats like 'A1B 2CD'.
    """
    if not re.match(r'^\d{5}(-\d{4})?$', value) and not re.match(
        r'^[A-Z0-9 ]{6,7}$', value):
        raise ValidationError("Enter a valid zip code. For US, use '12345' or" 
        "'12345-6789'. For UK, use alphanumeric formats like 'A1B 2CD'.")