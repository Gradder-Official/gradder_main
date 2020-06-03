from threading import Thread
from flask import current_app, render_template
from flask_mail import Message
from typing import List, Tuple
from . import mail


# A type the defines a list of files contained in tuples as (filename, file_content)
fileList = List[Tuple]


def send_async_email(app, msg: Message):
    r"""Sends an email in the context of the current app.

    Parameters
    ----------
    app : A Flask app instance
        A current Flask app.
    msg : flask_mail.Message
        Defines a message to be sent.
    """
    with app.app_context():
        mail.send(msg)


def send_email(to: List[str], subject: str, template: str, files: fileList = None, **kwargs):
    r"""Sends an email in another thread.

    Compiles a flask_mail.Message object from the arguments, and passes it to send_asyn_mail in a new thread.

    Parameters
    ----------
    to : str
        An email address the message should be send to (a single argument, not a list--to not overload the threads).
    subject : str
        Email's subject line.
    template : str
        Html/txt template's name without the extension, should be saved in templates/mail.
    files : fileList, optional
        A list of tuples, each of which defines a file to attach as (filename, file_content), the default is None.
    \**kwargs : Any types
        Keyword arguments that would be passed to the html/txt template and would be rendered in there. 
    """
    app = current_app._get_current_object()

    msg = Message(app.config['MAIL_SUBJECT_PREFIX'] + ' ' + subject,
                  sender=app.config['MAIL_SENDER'], recipients=to)
    # msg.body is used if html cannot be rendered properly
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)

    if files is not None:
        for filename, file_content in files:
            msg.attach(filename,
                       'application/octect-stream', file_content)

    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()

    return thr
