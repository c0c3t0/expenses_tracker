from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


def only_letters_validator(value):
    for letter in value:
        if not letter.isalpha():
            raise ValidationError("Ensure this value contains only letters.")


@deconstructible
class MaxImageSizeInMB:
    def __init__(self, max_size):
        self.max_size = max_size

    def __call__(self, value):
        filesize = value.file.size
        if filesize > self.max_size * 1024 * 1024:
            raise ValidationError(f'Max file size is {self.max_size:.2f} MB')


# def image_validator(value, IMAGE_MAX_SIZE=5):
#     filesize = value.file.size
#     if filesize > IMAGE_MAX_SIZE * 1024 * 1024:
#         raise ValidationError(f"Max file size is {IMAGE_MAX_SIZE}MB")
