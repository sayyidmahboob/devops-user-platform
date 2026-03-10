from sqlalchemy import Column, Integer, String, Boolean
from database import Base


class FeatureFlag(Base):

    __tablename__ = "feature_flags"

    id = Column(Integer, primary_key=True)

    feature_name = Column(String, unique=True)

    enabled = Column(Boolean)






