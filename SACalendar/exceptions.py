from dataclasses import dataclass
from typing import Sequence
from zoneinfo import available_timezones


class SACalendarError(Exception):
    pass


class UnsupportedLanguageError(SACalendarError):
    """
    Custom exception class to help with invalid "lang" parameter.
    """
    def __init__(self, language, message: str = 'You can choose only RU or EN') -> None:
        self.language = language
        self.message = message
        super().__init__(self.message)

    def __str__(self) -> str:
        return f':: --> {self.language} <-- {self.message} ::'


class UnsupportedTimeZone(SACalendarError):
    """
    Custom exception class to help with invalid "time_zone" parameter.
    """
    message = ('You can choose only available timezones!\n'
               'more info > https://docs.python.org/3/library/zoneinfo.html#zoneinfo.available_timezones')

    def __init__(self, time_zone) -> None:
        self.language = time_zone
        super().__init__(self.message)

    def __str__(self) -> str:
        return f':: --> {self.language} <-- {self.message} ::'


@dataclass(eq=False)
class EnableCalendarValidate:
    """
    Parameter Check.
    """
    displayed_years: Sequence[int]
    row_width: int

    def __post_init__(self):
        if not isinstance(self.row_width, int):
            raise TypeError('Type must be integer !')
        if not isinstance(self.displayed_years, Sequence):
            raise TypeError('Type must be list/tuple/set !')
        elif not all(isinstance(num, int) and num > 0 for num in self.displayed_years):
            raise TypeError('The passed sequence contains invalid elements !')
        elif len(self.displayed_years) != 2:
            raise ValueError('Length must be 2 !')


@dataclass(eq=False)
class CalendarParamValidate:
    """
    Parameter Check.
    """
    language: str
    time_zone: str

    def __post_init__(self):
        if self.time_zone not in available_timezones():
            raise UnsupportedTimeZone(time_zone=self.time_zone)
        if self.language.lower() not in ('ru', 'en'):
            raise UnsupportedLanguageError(language=self.language)
