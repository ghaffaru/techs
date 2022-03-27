from pydantic import BaseModel


class SchoolBase(BaseModel):
    id: int
    dbn: str
    name: str
    category: str
    year: str
    total_enrollment: str
    grade_k_number: str
    grade_1_number: str
    grade_2_number: str
    grade_3_number: str
    grade_4_number: str
    grade_5_number: str
    grade_6_number: str
    grade_7_number: str
    grade_8_number: str
    female_number: str
    female_percentage: str
    male_number: str
    male_percentage: str
    black_number: str
    black_percentage: str
    asian_number: str
    asian_percentage: str
    hispanic_number: str
    hispanic_percentage: str
    other_number: str
    other_percentage: str
    white_number: str
    white_percentage: str
    spanish_number: str
    spanish_percentage: str
    chinese_number: str
    chinese_percentage: str
    bengali_number: str
    bengali_percentage: str
    arabic_number: str
    arabic_percentage: str
    haitian_number: str
    haitian_percentage: str
    french_number: str
    french_percentage: str
    russian_number: str
    russian_percentage: str
    korean_number: str
    korean_percentage: str
    urdu_number: str
    urdu_percentage: str


class School(SchoolBase):

    class Config:
        orm_mode = True
