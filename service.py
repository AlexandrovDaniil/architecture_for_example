from typing import List, Union, Optional
from exceptions import MyException
from data import User, Note, Issue, Book
from storage import UserStorage, NoteStorage, IssueStorage, BookStorage, UserBookStorage


class UserService:
    def __init__(self, user_storage: UserStorage):
        self.user_storage = user_storage

    def get_users(self) -> List[User]:
        users = self.user_storage.get_all_users()
        return users

    def get_user(self, user_id: int) -> Optional[User]:
        return self.user_storage.get_users(user_id=user_id)

    def create_user(self, data: dict):
        self.user_storage.create_user(data)

    def update_user(self, user_id: int, data: dict):
        self.user_storage.update_user(user_id, data)

    def update_all_user(self, user_id: int, data: dict):
        self.user_storage.update_all_user(user_id, data)

    def delete_user(self, user_id: int):
        self.user_storage.delete_user(user_id)


class NoteService:
    def __init__(self, note_storage: NoteStorage):
        self.note_storage = note_storage

    def get_notes(self) -> List[Note]:
        note = self.note_storage.get_all_notes()
        return note

    def get_note(self, note_id: int) -> Union[Note, bool]:
        for i in self.note_storage.get_notes():
            if i.id == note_id:
                return i
        else:
            return False

    def create_note(self, data: dict):
        self.note_storage.create_note(data)

    def update_note(self, note_id: int, data: dict):
        self.note_storage.update_note(note_id, data)

    def update_all_note(self, note_id: int, data: dict):
        self.note_storage.update_all_note(note_id, data)

    def delete_note(self, note_id: int):
        self.note_storage.delete_note(note_id)


class IssueService:
    def __init__(self, issue_storage: IssueStorage):
        self.issue_storage = issue_storage

    def get_issues(self) -> List[Issue]:
        issue = self.issue_storage.get_all_issues()
        return issue

    def get_issue(self, issue_id: int) -> Union[Issue, bool]:
        for i in self.issue_storage.get_issue():
            if i.id == issue_id:
                return i
        else:
            return False

    def create_issue(self, data: dict):
        self.issue_storage.create_issue(data)

    def update_issue(self, issue_id: int, data: dict):
        self.issue_storage.update_issue(issue_id, data)

    def update_all_issues(self, issue_id: int, data: dict):
        self.issue_storage.update_all_issue(issue_id, data)

    def delete_issue(self, issue_id: int):
        self.issue_storage.delete_issue(issue_id)


class BookService:
    def __init__(self, book_storage: BookStorage):
        self.book_storage = book_storage

    def get_books(self) -> List[Book]:
        book = self.book_storage.get_all_books()
        return book

    def get_book(self, book_id: int) -> Union[Book, bool]:
        for i in self.book_storage.get_book():
            if i.id == book_id:
                return i
        else:
            return False

    def create_book(self, data: dict):
        self.book_storage.create_book(data)

    def update_book(self, book_id: int, data: dict):
        self.book_storage.update_book(book_id, data)

    def update_all_books(self, book_id: int, data: dict):
        self.book_storage.update_all_book(book_id, data)

    def delete_book(self, book_id: int):
        self.book_storage.delete_book(book_id)

    def get_book_status(self, book_id: int):
        return self.book_storage.get_book_status(book_id)


class UserBookService:
    def __init__(self, user_book_storage: UserBookStorage):
        self.user_book_storage = user_book_storage

    def take_book(self, user_id: int, book_id: int) -> Union[User, None]:
        return self.user_book_storage.take_book(user_id=user_id, book_id=book_id)

    def return_book(self, user_id: int, book_id: int):
        self.user_book_storage.return_book(user_id=user_id, book_id=book_id)
