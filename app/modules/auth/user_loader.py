from app import login_manager
from app.modules.db.classes import User


@login_manager.user_loader
def load_user(id: str):
    return User.from_dict(User.get_by_id(id))
