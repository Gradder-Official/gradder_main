import os
from datetime import datetime

from flask import redirect, url_for, render_template, flash, current_app, request
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename

from .forms import (
    ContactUsForm,
    CareersForm,
    SubscriberForm,
    InquiryForm,
    UnsubscribeForm,
)
from app.email import send_email
from . import main
from app.modules._classes import (
    Message,
    Application,
    Assignment,
    User,
    Inquiry,
    Subscriber,
)
from app import db
from app.decorators import required_access
from app.logger import logger

from google.cloud import storage


@main.route("/", methods=["GET", "POST"])
@main.route("/index", methods=["GET", "POST"])
def index():
    # logger.info("Page was accessed")

    subscription_form = SubscriberForm()
    inquiry_form = InquiryForm()

    if subscription_form.submit1.data and subscription_form.validate():
        subscriber = Subscriber(email=subscription_form.email.data)
        status = subscriber.add()

        send_email(
            to=[subscriber.email],
            subject="Subscribed to updates",
            template="mail/subscription",
            ID=subscriber.ID,
        )

        logger.info(f"Subscriber added - {subscription_form.email.data}")

        return redirect(url_for("main.status", success=status, next="main.index"))

    if inquiry_form.submit2.data and inquiry_form.validate():
        inquiry = Inquiry(
            name=inquiry_form.name.data,
            email=inquiry_form.email.data,
            subject=inquiry_form.subject.data,
            inquiry=inquiry_form.inquiry.data,
        )
        try:
            status = inquiry.add()

            send_email(
                to=[current_app._get_current_object().config["GRADDER_EMAIL"]],
                subject=f"Inquiry #{inquiry.ID}",
                template="mail/inquiry_admin",
                name=inquiry.name,
                email=inquiry.email,
                inquiry_subject=inquiry.subject,
                inquiry=inquiry.inquiry,
                date=datetime.today().strftime("%Y-%m-%d-%H:%M:%S"),
            )
            send_email(
                to=[inquiry.email],
                subject=f"Inquiry #{inquiry.ID}",
                template="mail/inquiry_user",
                name=inquiry.name,
                inquiry_subject=inquiry.subject,
                inquiry=inquiry.inquiry,
                ID=inquiry.ID,
            )

            logger.info(f"Inquiry made - {inquiry_form.email.data}")

            return redirect(
                url_for(
                    "main.status", success=True, next="main.index", _anchor="footer"
                )
            )
        except BaseException as e:
            logger.exception(e)
            return redirect(
                url_for(
                    "main.status", success=False, next="main.index", _anchor="footer"
                )
            )

    return render_template(
        "main/index.html",
        subscription_form=subscription_form,
        inquiry_form=inquiry_form,
    )


@main.route("/status/<string:success>/<path:next>", methods=["GET"])
def status(success: str, next: str):
    return render_template("status.html", success=success, next=next)


@main.route("/unsubscribe/<string:ID>", methods=["GET", "POST"])
def unsubscribe(ID: str):
    unsubscribe_form = UnsubscribeForm()

    if unsubscribe_form.validate_on_submit():
        if Subscriber.remove_by_id(ID):
            logger.info(f"Subscriber removed")

            return render_template(
                "main/unsubscribe.html", form=unsubscribe_form, unsubscribed=True
            )

    return render_template(
        "main/unsubscribe.html", form=unsubscribe_form, unsubscribed=False
    )


@main.route("/dashboard")
@login_required
def dashboard():
    if current_user.USERTYPE == "Student":
        return redirect(url_for("student.index"))
    elif current_user.USERTYPE == "Parent":
        return redirect(url_for("parent.index"))
    elif current_user.USERTYPE == "Teacher":
        return redirect(url_for("teacher.index"))
    elif current_user.USERTYPE == "Admin":
        return redirect(url_for("admin.index"))
    else:
        return redirect(url_for("main.index"))


@main.route("/profile")
@login_required
def profile():
    if current_user.USERTYPE == "Student":
        return redirect(url_for("student.profile"))
    elif current_user.USERTYPE == "Parent":
        return redirect(url_for("parent.profile"))
    elif current_user.USERTYPE == "Teacher":
        return redirect(url_for("teacher.profile"))
    elif current_user.USERTYPE == "Admin":
        return redirect(url_for("admin.profile"))
    else:
        return redirect(url_for("main.index"))
