from flask import Blueprint

teacher = Blueprint('teacher', __name__, static_folder='static',
                    template_folder='templates', url_prefix='/teacher')


from . import routes, forms