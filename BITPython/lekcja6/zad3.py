# W krajach anglojęzycznych często przyznaje się oceny literowe, a nie numeryczne, np. A, B, C, D, E, F. Możliwe są też oceny pośrednie: B+, C+, D+, E+ i F+.
# Średnia ocen z listy ocen danego ucznia jest zaokrąglana do "najbliższej liczby". Aby obliczyć średnią, oceny literowe mapuje się na liczby.
from enum import Enum

class Grade(Enum):
    A = 6
    B = 5
    C = 4
    D = 3
    E = 2
    F = 1


class GradeLog:

    def __init__(self):
        self.log = []

    def add(self, grade):
        self.log.append(grade)
    
    def get_avg_grade(self):
        return Grade(round(
            sum(
                [grade.value for grade in self.log])
                / len(self.log)
            ))