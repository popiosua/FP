class EvaluationError(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class PlayerTournamentEvaluation:
    RESULT_RATE = {'w': 1, 'f': 1 / 2, 'sf': 1 / 4, 'qf': 1 / 8, 'r16': 1 / 16}

    def __init__(self, player, points, result):
        self.__player = player
        self.__points = points
        self.__result = result

    @property
    def player(self):
        return self.__player

    def get_number_of_points(self):
        """
        Calculeaza numarul de puncte
        :return: numarul de puncte modificat, luand in considerare rezultatul
        :raises: EvaluationError daca rezultatul nu este unul recunoscut
        """
        previous_points = self.__player.points
        try:
            previous_points += self.__points * PlayerTournamentEvaluation.RESULT_RATE[self.__result.lower()]
            return previous_points
        except KeyError:
            raise EvaluationError("Result in tournament not recognized.")
