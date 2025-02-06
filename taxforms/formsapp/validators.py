from django.core.exceptions import ValidationError

def validate_file_size(value):
    max_size = 4 * 1024 * 1024  # 4 MB
    if value.size > max_size:
        raise ValidationError("File size must be no more than 4 MB.")