from __future__ import annotations

from app import db


class Inquiry:
    def __init__(
        self, name: str, email: str, subject: str, inquiry: str, _id: str = None
    ):
        self.name = name
        self.email = email
        self.subject = subject
        self.inquiry = inquiry
        self.ID = _id

    def __repr__(self):
        return f"<Inquiry { self.ID }>"

    def to_dict(self) -> dict:
        if self.ID is not None:
            return {
                "name": self.name,
                "email": self.email,
                "subject": self.subject,
                "inquiry": self.inquiry,
                "_id": self.ID,
            }
        return {
            "name": self.name,
            "email": self.email,
            "subject": self.subject,
            "inquiry": self.inquiry,
        }

    def to_json(self) -> dict:
        return self.to_dict()

    @staticmethod
    def from_dict(dictionary: dict) -> Inquiry:
        return Inquiry(**dictionary)

    def add(self) -> bool:
        try:
            self.ID = db.inquiries.insert_one(self.to_dict()).inserted_id
            # TODO: logger
            return True
        except BaseException as e:
            # TODO: logger
            return False
