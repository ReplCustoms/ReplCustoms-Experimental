from app import loginM
from app.models import User

@loginM.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

