from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

class CustomMinimumLengthValidator:
    def __init__(self, min_length=8):
        self.min_length = min_length

    def validate(self, password, user=None):
        if len(password) < self.min_length:
            raise ValidationError(
                f"Esta senha é muito curta. Ela deve conter pelo menos {self.min_length} caracteres.",
                code='password_too_short',
            )

    def get_help_text(self):
        return f"Sua senha deve conter pelo menos {self.min_length} caracteres."


class CustomCommonPasswordValidator:
    def validate(self, password, user=None):
        from django.contrib.auth.password_validation import CommonPasswordValidator
        validator = CommonPasswordValidator()
        try:
            validator.validate(password, user)
        except ValidationError:
            raise ValidationError(
                "Esta senha é muito comum.",
                code='password_too_common',
            )

    def get_help_text(self):
        return "Sua senha não pode ser uma senha muito comum."


class CustomNumericPasswordValidator:
    def validate(self, password, user=None):
        if password.isdigit():
            raise ValidationError(
                "Esta senha é inteiramente numérica.",
                code='password_entirely_numeric',
            )

    def get_help_text(self):
        return "Sua senha não pode ser inteiramente numérica."


class CustomUserAttributeSimilarityValidator:
    def __init__(self, user_attributes=('username', 'email'), max_similarity=0.7):
        self.user_attributes = user_attributes
        self.max_similarity = max_similarity

    def validate(self, password, user=None):
        from django.contrib.auth.password_validation import UserAttributeSimilarityValidator
        validator = UserAttributeSimilarityValidator(user_attributes=self.user_attributes, max_similarity=self.max_similarity)
        try:
            validator.validate(password, user)
        except ValidationError:
            raise ValidationError(
                "A senha é muito semelhante aos seus dados pessoais.",
                code='password_too_similar',
            )

    def get_help_text(self):
        return "Sua senha não pode ser muito semelhante às suas outras informações pessoais."
