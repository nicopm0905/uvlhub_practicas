from app.features.notepad.repositories import NotepadRepository
from splent_framework.services.BaseService import BaseService


class NotepadService(BaseService):
    def __init__(self):
        super().__init__(NotepadRepository())
