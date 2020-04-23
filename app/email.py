from threading import Thread
from flask import current_app, render_template
from flask_mail import Message
from typing import List, Tuple
from . import mail


fileList = List[Tuple]


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(to: str, subject: str, template: str, files: fileList = None, **kwargs):
    app = current_app._get_current_object()
    msg = Message(app.config['MAIL_SUBJECT_PREFIX'] + ' ' + subject,
                  sender=app.config['MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)

    if files is not None:
        for filename, file_content in files:
            msg.attach(filename,
                       'application/octect-stream', file_content)

    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr
