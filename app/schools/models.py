from app.database import Base
from sqlalchemy import Column,Integer,String, Float


class School(Base):
    __tablename__ = 'schools'
    id = Column(Integer, primary_key=True, autoincrement=True)
    dbn = Column(String)
    name = Column(String)
    category = Column(String)
    year = Column(String)
    total_enrollment = Column(Integer, nullable=True)
    grade_k_number = Column(Integer, nullable=True)
    grade_1_number = Column(Integer, nullable=True)
    grade_2_number = Column(Integer, nullable=True)
    grade_3_number = Column(Integer, nullable=True)
    grade_4_number = Column(Integer, nullable=True)
    grade_5_number = Column(Integer, nullable=True)
    grade_6_number = Column(Integer, nullable=True)
    grade_7_number = Column(Integer, nullable=True)
    grade_8_number = Column(Integer, nullable=True)
    female_number = Column(Integer, nullable=True)
    female_percentage = Column(Float, nullable=True)
    male_number = Column(Integer, nullable=True)
    male_percentage = Column(Float, nullable=True)
    black_number = Column(Integer, nullable=True)
    black_percentage = Column(Float, nullable=True)
    asian_number = Column(Integer, nullable=True)
    asian_percentage = Column(Float, nullable=True)
    hispanic_number = Column(Integer, nullable=True)
    hispanic_percentage = Column(Float, nullable=True)
    other_number = Column(Integer, nullable=True)
    other_percentage = Column(Float, nullable=True)
    white_number = Column(Integer, nullable=True)
    white_percentage = Column(Float, nullable=True)
    spanish_number = Column(Integer, nullable=True)
    spanish_percentage = Column(Float, nullable=True)
    chinese_number = Column(Integer, nullable=True)
    chinese_percentage = Column(Float, nullable=True)
    bengali_number = Column(Integer, nullable=True)
    bengali_percentage = Column(Float, nullable=True)




