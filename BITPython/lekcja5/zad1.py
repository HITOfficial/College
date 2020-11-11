# Wirtualny Dziekanat i USOS jak działają, każdy widzi. W związku z tym twoim zadaniem jest przepisanie takiego systemu na solidnie zaprojektowaną obiektową architekturę.

# Wymagania:
# studenci mają imię, nazwisko, adres zamieszkania, numer legitymacji i wydział, na którym studiuje; każdy student ma także zbiór kursów, na które jest zapisany
# pracownicy mają imię, nazwisko, adres zamieszkania i numer identyfikatora; każdy pracownik ma także zbiór kursów, które prowadzi oraz jest zatrudniony przez konkretny wydział
# wydział ma nazwę, wewnętrzny numer, syllabus z kursami które ma w swojej ofercie, kursy aktualnie prowadzone oraz zbiór pracowników, którzy w nim pracują
# kurs ma nazwę, liczbę punktów ECTS, opis, jest prowadzony przez konkretny wydział
# aktualnie prowadzony kurs ma zbiór studentów, którzy na niego uczęszczają oraz zbiór prowadzących, którzy go prowadzą
# zdarza się, że pracownicy mogą nie mieć tymczasowo żadnego wydziału (np. świeżo po zatrudnieniu, albo podczas reorganizacji)
# niektórzy prowadzący są wykładowcami i tym samym członkami rady wydziału, w związku z czym posiadają dodatkowo określoną liczbę głosów w sprawach organizacyjnych

# Chcemy móc:
# tworzyć nowych studentów, zapisywać ich na kursy, usuwać studentów na koniec studiów
# tworzyć nowych prowadzących, zatrudniać ich na wydziałach, zwalniać ich
# nadawać prowadzącemu status wykładowcy (można założyć, że raz przyznany nie jest usuwany)
# przypisywać studentów / prowadzących do kursów i ich z nich usuwać
# tworzyć i usuwać wydziały
# tworzyć i usuwać kursy, tworzyć aktualne edycje kursów z oferty (zacząć prowadzić kurs z syllabusa)
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Set, Optional


@dataclass
class Person:
    first_name: str
    last_name: str
    address: str

@dataclass
class Course:
    name: str
    ects_points: int
    description: str
    faculty: Faculty


@dataclass
class Employee(Person):
    employee_id: str
    courses: Set[Course]
    faculty: Optional[Faculty] = None

@dataclass
class Lectuler(Employee):
    votes_count: int = 0


@dataclass
class Faculty:
    name: str
    id_number: str
    syllabus: Set[Course] = field(default_factory=set)
    active_courses: Set[Course] = field(default_factory=set)
    employess: Set[Employee] = field(default_factory=set)


@dataclass
class Student(Person):
    student_id: str
    faculty: Faculty
    coursers: Set[Course] = field(default_factory=set)

    def enroll(self, course: Course):
        self.coursers.add(course)


@dataclass
class System:
    students: Set[Student] = field(default_factory=set)

    def add_student(self, student: Student):
        self.students.add(student)

    def remove_student(self, student: Student):
        self.students.remove(student)

    
system= System()


if __name__ == '__main__':    
    w1 = Faculty('WIEiT', '1', )
    s1 = Student('Arthur', 'Blob', 'Sepa 51B', '1234', w1)
    l1 = Lectuler('Morty', 'Blob', 'Doom 13', '12', votes_count=60)


