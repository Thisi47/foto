from django.core.exceptions import ValidationError

class ContainsLettersValidator:
    def validate(self, password, user=None):
        if not any(char.is_alpha for char in password):
            raise ValidationError('Le mot de passe doit contenir une lettre', code="password_no_letters")

    def get_help_text(self):
        return "Le mot de passe doit contenir au mois une lettre majuscule ou minicule"
    
class ContainsDigitsValidator:
    def validate(self, password, user=None):
        if not any(digit.is_digit for digit in password):
            raise ValidationError("Le mot de passe doit contenir un nombre", code='password_no_digit')
    def get_help_text(self):
        return 'Le mot de passe doit contenir au mois un chiffre'