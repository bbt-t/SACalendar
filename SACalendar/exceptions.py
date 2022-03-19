class SACalendarError(Exception):
    pass


class UnsupportedLanguageError(SACalendarError):
    def __init__(self, language, message: str = 'You can choose only RU or EN') -> None:
        self.language = language
        self.message = message
        super().__init__(self.message)

    def __str__(self) -> str:
        return f':: --> {self.language} <-- {self.message} ::'


class UnsupportedTimeZone(SACalendarError):
    message = ('You can choose only available timezones!\n'
               'more info > https://docs.python.org/3/library/zoneinfo.html#zoneinfo.available_timezones')

    def __init__(self, time_zone) -> None:
        self.language = time_zone
        super().__init__(self.message)

    def __str__(self) -> str:
        return f':: --> {self.language} <-- {self.message} ::'
