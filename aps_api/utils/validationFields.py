from django.core.validators import RegexValidator


letters_validator = RegexValidator(
    regex=r'^[a-zA-Z\s]*$',
    message='Solo se permiten letras y espacios.'
)

numbers_validator=RegexValidator(
    regex=r'^[0-9]+$',
    message='Este campo solo debe contener números.'
)