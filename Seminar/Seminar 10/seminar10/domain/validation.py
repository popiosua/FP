class ValidationException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class PlayerValidator:
    def validate(self, player):
        # matches played, won >=0
        # matches_won<matches_played
        errors = []
        if player.matches_played < 0:
            errors.append("Numarul de meciuri jucate trebuie sa fie mai mare de 0.")
        if player.matches_won < 0:
            errors.append("Numarul de meciuri castigate trebuie sa fie mai mare de 0.")
        if player.matches_won > player.matches_played:
            errors.append("Numarul de meciuri castigate trebuie sa fie mai mic sau egal cu numarul de meciuri jucate.")

        if len(errors) > 0:
            errors_str = '\n'.join(errors)
            raise ValidationException(errors_str)
