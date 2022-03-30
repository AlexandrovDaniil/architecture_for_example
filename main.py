import falcon
from views import UserController, UsersController, NotesController, NoteController, IssueController, IssuesController, \
    BookController, BooksController, TakeBookController, ReturnBookController
from exceptions import MyException

app = falcon.App()
app.add_error_handler(MyException)
app.add_route('/users/{user_id}', UserController())
app.add_route('/users/', UsersController())
app.add_route('/notes/{note_id}', NoteController())
app.add_route('/notes/', NotesController())
app.add_route('/issues/{issue_id}', IssueController())
app.add_route('/issues/', IssuesController())
app.add_route('/books/{book_id}/status', BookController())
app.add_route('/books/', BooksController())
app.add_route('/books/take', TakeBookController())
app.add_route('/books/return', ReturnBookController())
