from data import User, Note, Issue, Book, UserBook
from typing import Dict, Any, Iterator, List, Union, Optional
import time

users = [{'id': 1, 'name': 'vanya', 'surname': 'ivanov'},
         {'id': 2, 'name': 'petya', 'surname': 'petrov'}]

notes = [{'id': 1, 'name': 'qwe', 'author': 'ivanov', 'number_of_likes': 13},
         {'id': 2, 'name': 'qqqq', 'author': 'petrov', 'number_of_likes': 1}]

books = [{'id': 1, 'title': 'qwe', 'author': 'ivanov', 'status': True},
         {'id': 2, 'title': 'qqqq', 'author': 'petrov', 'status': True}]

issues = [{'id': 1, 'title': 'qwe', 'author': 'ivanov', 'executor': 'petya', 'tags': ['fff', 'ggg'],
           'date_of_create': time.time(), 'date_of_update': time.time()},
          {'id': 2, 'title': 'ewq', 'author': 'petrov', 'executor': 'vanya', 'tags': ['aaa', 'sss'],
           'date_of_create': time.time(), 'date_of_update': time.time()}]

user_book = []


class UserStorage:

    def get_users(self, user_id: int) -> Optional[User]:
        for user in users:
            if user['id'] == user_id:
                user: Dict[str, Any]
                return User(**user
                    # id=user['id'],
                    # name=user['name'],
                    # surname=user['surname']
                )
        else:
            return None

    def get_all_users(self) -> List[User]:
        res = []
        for user in users:
            user: Dict[str, Any]
            res.append(User(
                id=user['id'],
                name=user['name'],
                surname=user['surname']
            ))
        return res

    def create_user(self, data: dict):
        data['id'] = int(data['id'])
        users.append(data)

    def update_user(self, user_id: int, data: dict):
        for user in users:
            if user['id'] == user_id:
                for k, v in data.items():
                    user[k] = v

    def update_all_user(self, user_id: int, data: dict):
        for user in users:
            if user['id'] == user_id:
                user.clear()
                user['id'] = user_id
                for k, v in data.items():
                    user[k] = v

    def delete_user(self, user_id: int):
        for user in users:
            if user['id'] == user_id:
                users.remove(user)


class NoteStorage:

    def get_notes(self) -> Iterator[Note]:
        for note in notes:
            note: Dict[str, Any]
            yield Note(
                id=note['id'],
                name=note['name'],
                author=note['author'],
                number_of_likes=note['number_of_likes']
            )

    def get_all_notes(self) -> List[Note]:
        res = []
        for note in notes:
            note: Dict[str, Any]
            res.append(Note(
                id=note['id'],
                name=note['name'],
                author=note['author'],
                number_of_likes=note['number_of_likes'])
            )
        return res

    def create_note(self, data: dict):
        data['id'] = int(data['id'])
        data['number_of_likes'] = int(data['number_of_likes'])
        notes.append(data)

    def update_note(self, note_id: int, data: dict):
        for note in notes:
            if note['id'] == note_id:
                for k, v in data.items():
                    note[k] = v

    def update_all_note(self, note_id: int, data: dict):
        for note in notes:
            if note['id'] == note_id:
                note.clear()
                note['id'] = note_id
                for k, v in data.items():
                    note[k] = v

    def delete_note(self, note_id: int):
        for note in notes:
            if note['id'] == note_id:
                notes.remove(note)


class IssueStorage:

    def get_issue(self) -> Iterator[Issue]:
        for issue in issues:
            issue: Dict[str, Any]
            yield Issue(
                id=issue['id'],
                title=issue['title'],
                author=issue['author'],
                executor=issue['executor'],
                tags=issue['tags'],
                date_of_create=issue['date_of_create'],
                date_of_update=issue['date_of_update']

            )

    def get_all_issues(self) -> List[Issue]:
        res = []
        for issue in issues:
            issue: Dict[str, Any]
            res.append(Issue(
                id=issue['id'],
                title=issue['title'],
                author=issue['author'],
                executor=issue['executor'],
                tags=issue['tags'],
                date_of_create=issue['date_of_create'],
                date_of_update=issue['date_of_update'])
            )
        return res

    def create_issue(self, data: dict):
        data['id'] = int(data['id'])
        issues.append(data)

    def update_issue(self, issue_id: int, data: dict):
        for issue in issues:
            if issue['id'] == issue_id:
                for k, v in data.items():
                    issue[k] = v
                issue['date_of_update'] = time.time()

    def update_all_issue(self, issue_id: int, data: dict):
        for issue in issues:
            if issue['id'] == issue_id:
                issue.clear()
                issue['id'] = issue_id
                for k, v in data.items():
                    issue[k] = v
                issue['date_of_update'] = time.time()

    def delete_issue(self, issue_id: int):
        for issue in issues:
            if issue['id'] == issue_id:
                issues.remove(issue)


class BookStorage:

    def get_book(self) -> Iterator[Book]:
        for book in books:
            book: Dict[str, Any]
            yield Book(
                id=book['id'],
                title=book['title'],
                author=book['author'],
                status=book['status']
            )

    def get_all_books(self) -> List[Book]:
        res = []
        for book in books:
            book: Dict[str, Any]
            res.append(Book(
                id=book['id'],
                title=book['title'],
                author=book['author'],
                status=book['status'])

            )
        return res

    def create_book(self, data: dict):
        data['id'] = int(data['id'])
        books.append(data)

    def update_book(self, book_id: int, data: dict):
        for book in books:
            if book['id'] == book_id:
                for k, v in data.items():
                    book[k] = v

    def update_all_book(self, book_id: int, data: dict):
        for book in books:
            if book['id'] == book_id:
                book.clear()
                book['id'] = book_id
                for k, v in data.items():
                    book[k] = v

    def delete_book(self, book_id: int):
        for book in books:
            if book['id'] == book_id:
                books.remove(book)

    def get_book_status(self, book_id: int) -> bool:
        for book in books:
            if book['id'] == book_id:
                return book['status']

    def set_book_status(self, book_id: int, status: bool):
        for book in books:
            if book['id'] == book_id:
                book['status'] = status


class UserBookStorage:
    def take_book(self, user_id: int, book_id: int):
        bookstrg = BookStorage()
        userstr = UserStorage()
        if bookstrg.get_book_status(book_id=book_id):
            user_book.append({'user_id': user_id, 'book_id': book_id})

            bookstrg.set_book_status(book_id=book_id, status=False)
        else:
            for i in user_book:
                if i['book_id'] == book_id:
                    return userstr.get_users(user_id=user_id)

    def return_book(self, user_id: int, book_id: int):
        for i in user_book:
            if i['user_id'] == user_id and i['book_id'] == book_id:
                bookstrg = BookStorage()
                bookstrg.set_book_status(book_id=book_id, status=True)
                user_book.remove(i)
