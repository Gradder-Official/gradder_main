from __future__ import annotations

from typing import Optional


class CalendarEvent:
    _title: str
    _start: str
    _end: str
    _color: str
    _url: str

    def __init__(
        self, title: str, start: str, end: str, color: Optional[str], url: Optional[str]
    ):
        self.title = title
        self.start = start
        self.end = end
        self.color = color or ""
        self.url = url or ""

    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "start": self.start,
            "end": self.end,
            "color": self.color,
            "url": self.url,
        }

    @classmethod
    def from_dict(cls, dictionary: dict) -> CalendarEvent:
        return cls(**dictionary)

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, title: str):
        self._title = title

    @property
    def start(self) -> str:
        return self._start

    @start.setter
    def start(self, start: str):
        self._start = start

    @property
    def end(self) -> str:
        return self._end

    @end.setter
    def end(self, end: str):
        self._end = end

    @property
    def color(self) -> str:
        return self._color

    @color.setter
    def color(self, color: str):
        self._color = color

    @property
    def url(self) -> str:
        return self._url

    @url.setter
    def url(self, url: str):
        self._url = url
