from datetime import datetime
from typing import Optional
from sqlalchemy import DateTime, Engine, ForeignKey, String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, relationship

engine: Engine= create_engine("sqlite:///app.db")

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]]
    posts: Mapped[list["Post"]] = relationship("Post", back_populates="user", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"{self.id} -> {self.name} -> {self.fullname}"

class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(30), default="Untitled")
    description: Mapped[Optional[str]]
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship("User", back_populates="posts")

    def __repr__(self) -> str:
        return f"{self.id} -> {self.title}"

Base.metadata.create_all(bind=engine)

session: Session = Session(engine)

user1 = User(name="joshua", fullname="joseph")
session.add(user1)

stmt = select(User).where(User.name == "joshua")
joshua = session.scalars(stmt).one()
print(joshua)


