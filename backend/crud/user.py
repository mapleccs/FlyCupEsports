from sqlalchemy.orm import Session, joinedload
from backend.models.user import User
from backend.schemas.v1.user import UserCreateRequest, UserInfoResponse, UserLoginRequest


def user_login(db: Session, login_info: UserLoginRequest) -> User | None:
    user = db.query(User).options(joinedload(User.Role)).filter(
        User.Username == login_info.username,
        User.Password == login_info.password
    ).first()
    return user


def get_all_user(db: Session) -> list[UserInfoResponse]:
    users = db.query(User).options(
        joinedload(User.Role)
    ).all()

    return [
        UserInfoResponse(
            id=u.Id,
            username=u.Username,
            photo_path=u.UserPhoto,
            user_role_id=u.RoleId,
            user_role_name=u.Role.Name if u.Role else None
        ) for u in users
    ]


def get_user_by_username(db: Session, username: str) -> User | None:
    return db.query(User).filter(User.Username == username).first()


def create_user(db: Session, user: UserCreateRequest, role_id: int) -> User | None:
    db_user = User(
        Username=user.username,
        Password=user.password,
        UserPhoto=user.photo_path,
        RoleId=role_id,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
