import falcon
from dataclasses import asdict
from falcon import Request, Response
from service import UserService, NoteService, IssueService, BookService, UserBookService
from storage import UserStorage, NoteStorage, IssueStorage, BookStorage, UserBookStorage
import json
from exceptions import MyException

USER_SERVICE = UserService(UserStorage())
NOTE_SERVICE = NoteService(NoteStorage())
ISSUE_SERVICE = IssueService(IssueStorage())
BOOK_SERVICE = BookService(BookStorage())
USER_BOOK_SERVICE = UserBookService(UserBookStorage())


class UserController:
    def on_get(self, req: Request, resp: Response, user_id: str):
        if USER_SERVICE.get_user(int(user_id)):
            users = asdict(USER_SERVICE.get_user(int(user_id)))
            print(users)
            resp.body = json.dumps(users)
        else:
            resp.status = falcon.HTTP_502
            raise MyException('Error')

    def on_patch(self, req: Request, resp: Response, user_id: str):

        if USER_SERVICE.get_user(int(user_id)):
            result = req.get_media()
            USER_SERVICE.update_user(int(user_id), result)

        else:
            resp.status = falcon.HTTP_502
            raise MyException('Error')

    def on_put(self, req: Request, resp: Response, user_id: str):

        if USER_SERVICE.get_user(int(user_id)):
            result = req.get_media()
            USER_SERVICE.update_all_user(int(user_id), result)

        else:
            resp.status = falcon.HTTP_502
            raise MyException('Error')

    def on_delete(self, req: Request, resp: Response, user_id: str):

        if USER_SERVICE.get_user(int(user_id)):

            USER_SERVICE.delete_user(int(user_id))

        else:
            resp.status = falcon.HTTP_502
            raise MyException('Error')


class UsersController:
    def on_get(self, req: Request, resp: Response):
        users = USER_SERVICE.get_users()
        users = list(map(asdict, users))
        if req.get_param('limit') and req.get_param('offset'):
            limit = req.get_param_as_int('limit')
            offset = req.get_param_as_int('offset')
            users = users[offset:limit + offset]
            resp.body = json.dumps(users)
        else:
            resp.body = json.dumps(users)

    def on_post(self, req: Request, resp: Response):
        result = req.get_media()
        USER_SERVICE.create_user(result)


class NoteController:
    def on_get(self, req: Request, resp: Response, note_id: str):
        if NOTE_SERVICE.get_note(int(note_id)):
            notes = asdict(NOTE_SERVICE.get_note(int(note_id)))
            resp.status = falcon.HTTP_200
            resp.body = json.dumps(notes)
        else:
            resp.status = falcon.HTTP_404
            raise MyException('Error')

    def on_patch(self, req: Request, resp: Response, note_id: str):

        if NOTE_SERVICE.get_note(int(note_id)):
            result = req.get_media()
            NOTE_SERVICE.update_note(int(note_id), result)
            resp.status = falcon.HTTP_200
        else:
            resp.status = falcon.HTTP_404
            raise MyException('Error')

    def on_put(self, req: Request, resp: Response, note_id: str):

        if NOTE_SERVICE.get_note(int(note_id)):
            result = req.get_media()
            NOTE_SERVICE.update_all_note(int(note_id), result)
            resp.status = falcon.HTTP_200
        else:
            resp.status = falcon.HTTP_404
            raise MyException('Error')

    def on_delete(self, req: Request, resp: Response, note_id: str):

        if NOTE_SERVICE.get_note(int(note_id)):
            NOTE_SERVICE.delete_note(int(note_id))
            resp.status = falcon.HTTP_200

        else:
            resp.status = falcon.HTTP_404
            raise MyException('Error')


class NotesController:
    def on_get(self, req: Request, resp: Response):
        notes = NOTE_SERVICE.get_notes()
        notes = list(map(asdict, notes))
        if req.get_param('limit') and req.get_param('offset'):
            limit = req.get_param_as_int('limit')
            offset = req.get_param_as_int('offset')
            notes = notes[offset:limit + offset]
            resp.body = json.dumps(notes)
        else:
            resp.body = json.dumps(notes)
        resp.status = falcon.HTTP_200

    def on_post(self, req: Request, resp: Response):
        result = req.get_media()
        NOTE_SERVICE.create_note(result)
        resp.status = falcon.HTTP_200


class IssueController:
    def on_get(self, req: Request, resp: Response, issue_id: str):
        if ISSUE_SERVICE.get_issue(int(issue_id)):
            issue = asdict(ISSUE_SERVICE.get_issue(int(issue_id)))
            resp.status = falcon.HTTP_200
            resp.body = json.dumps(issue)
        else:
            resp.status = falcon.HTTP_404
            raise MyException('Error')

    def on_patch(self, req: Request, resp: Response, issue_id: str):

        if ISSUE_SERVICE.get_issue(int(issue_id)):
            result = req.get_media()
            ISSUE_SERVICE.update_issue(int(issue_id), result)
            resp.status = falcon.HTTP_200
        else:
            resp.status = falcon.HTTP_404
            raise MyException('Error')

    def on_put(self, req: Request, resp: Response, issue_id: str):

        if ISSUE_SERVICE.get_issue(int(issue_id)):
            result = req.get_media()
            ISSUE_SERVICE.update_all_issues(int(issue_id), result)
            resp.status = falcon.HTTP_200
        else:
            resp.status = falcon.HTTP_404
            raise MyException('Error')

    def on_delete(self, req: Request, resp: Response, issue_id: str):

        if ISSUE_SERVICE.get_issue(int(issue_id)):
            ISSUE_SERVICE.delete_issue(int(issue_id))
            resp.status = falcon.HTTP_200

        else:
            resp.status = falcon.HTTP_404
            raise MyException('Error')


class IssuesController:
    def on_get(self, req: Request, resp: Response):
        issues = ISSUE_SERVICE.get_issues()
        issues = list(map(asdict, issues))
        if req.get_param('limit') and req.get_param('offset'):
            limit = req.get_param_as_int('limit')
            offset = req.get_param_as_int('offset')
            issues = issues[offset:limit + offset]
            resp.body = json.dumps(issues)
        else:
            resp.body = json.dumps(issues)
        resp.status = falcon.HTTP_200

    def on_post(self, req: Request, resp: Response):
        result = req.get_media()
        ISSUE_SERVICE.create_issue(result)
        resp.status = falcon.HTTP_200


class BookController:
    def on_get(self, req: Request, resp: Response, book_id: str):
        if BOOK_SERVICE.get_book(int(book_id)):
            book_status = BOOK_SERVICE.get_book_status(int(book_id))
            resp.status = falcon.HTTP_200
            resp.body = json.dumps(book_status)
        else:
            resp.status = falcon.HTTP_404
            raise MyException('Error')

    def on_patch(self, req: Request, resp: Response, book_id: str):

        if BOOK_SERVICE.get_book(int(book_id)):
            result = req.get_media()
            BOOK_SERVICE.update_book(int(book_id), result)
            resp.status = falcon.HTTP_200
        else:
            resp.status = falcon.HTTP_404
            raise MyException('Error')

    def on_put(self, req: Request, resp: Response, book_id: str):

        if BOOK_SERVICE.get_book(int(book_id)):
            result = req.get_media()
            BOOK_SERVICE.update_all_books(int(book_id), result)
            resp.status = falcon.HTTP_200
        else:
            resp.status = falcon.HTTP_404
            raise MyException('Error')

    def on_delete(self, req: Request, resp: Response, book_id: str):

        if BOOK_SERVICE.get_book(int(book_id)):
            BOOK_SERVICE.delete_book(int(book_id))
            resp.status = falcon.HTTP_200

        else:
            resp.status = falcon.HTTP_404
            raise MyException('Error')


class BooksController:
    def on_get(self, req: Request, resp: Response):
        books = BOOK_SERVICE.get_books()
        books = list(map(asdict, books))
        if req.get_param('limit') and req.get_param('offset'):
            limit = req.get_param_as_int('limit')
            offset = req.get_param_as_int('offset')
            books = books[offset:limit + offset]
            resp.body = json.dumps(books)
        else:
            resp.body = json.dumps(books)
        resp.status = falcon.HTTP_200

    def on_post(self, req: Request, resp: Response):
        result = req.get_media()
        BOOK_SERVICE.create_book(result)
        resp.status = falcon.HTTP_200


class TakeBookController:
    def on_post(self, req: Request, resp: Response):
        result = req.get_media()
        user_id = int(result['user_id'])
        book_id = int(result['book_id'])
        if USER_BOOK_SERVICE.take_book(user_id=user_id, book_id=book_id):
            resp.body = json.dumps(asdict(USER_BOOK_SERVICE.take_book(user_id=user_id, book_id=book_id)))
        else:
            USER_BOOK_SERVICE.take_book(user_id=user_id, book_id=book_id)


class ReturnBookController:
    def on_post(self, req: Request, resp: Response):
        result = req.get_media()
        user_id = int(result['user_id'])
        book_id = int(result['book_id'])
        if not BOOK_SERVICE.get_book_status(book_id):
            USER_BOOK_SERVICE.return_book(user_id=user_id, book_id=book_id)
        else:
            raise MyException
