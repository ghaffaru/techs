from app import create_app
import requests
from os.path import exists
import sqlalchemy
from app.database import engine,SessionLocal
import pandas as pd
from app.schools import models

app = create_app()
celery = app.celery_app


@celery.task
def import_dataset():
    if not exists('data.csv'):
        r = requests.get('https://data.cityofnewyork.us/api/views/7yc5-fec2/rows.csv?accessType=DOWNLOAD',
                         allow_redirects=True)
        open('data.csv', 'wb').write(r.content)

    # check if schema exist
    if sqlalchemy.inspect(engine).has_table('schools'):

        # make sure schools table is empty
        schools_count = SessionLocal().query(models.School).count()

        if schools_count == 0:
            # read data.csv and populate schools table
            # try:
            db = SessionLocal()
            data = pd.read_csv('data.csv')
            for index, row in data.iterrows():
                school = models.School(dbn=row['DBN'],
                                       name=row['School Name'],
                                       category=row['Category'],
                                       year=row['Year'],
                                       total_enrollment=row['Total Enrollment'],
                                       grade_k_number=row['#Grade K'],
                                       grade_1_number=row['#Grade 1'],
                                       grade_2_number=row['#Grade 2'],
                                       grade_3_number=row['#Grade 3'],
                                       grade_4_number=row['#Grade 4'],
                                       grade_5_number=row['#Grade 5'],
                                       grade_6_number=row['#Grade 6'],
                                       grade_7_number=row['#Grade 7'],
                                       grade_8_number=row['#Grade 8'],
                                       female_number=row['#Female'],
                                       female_percentage=row['%Female'],
                                       male_number=row['#Male'],
                                       male_percentage=row['%Male'],
                                       asian_number=row['#Asian'],
                                       asian_percentage=row['%Asian'],
                                       black_number=row['#Black'],
                                       black_percentage=row['%Black'],
                                       hispanic_number=row['#Hispanic'],
                                       hispanic_percentage=row['%Hispanic'],
                                       other_number=row['#Other'],
                                       other_percentage=row['%Other'],
                                       white_number=row['#White'],
                                       white_percentage=row['%White '],
                                       spanish_number=row['#ELL Spanish '],
                                       spanish_percentage=row['%ELL Spanish'],
                                       chinese_number=row['#ELL Chinese'],
                                       chinese_percentage=row['%ELL Chinese'],
                                       bengali_number=row['#ELL Bengali'],
                                       bengali_percentage=row['%ELL Bengali'],
                                       arabic_number=row['#ELL Arabic'],
                                       arabic_percentage=row['%ELL Arabic'],
                                       haitian_number=row['#ELL Haitian Creole'],
                                       haitian_percentage=row['%ELL Haitian Creole'],
                                       french_percentage=row['%ELL French'],
                                       french_number=row['#ELL French'],
                                       russian_number=row['#ELL Russian'],
                                       russian_percentage=row['%ELL Russian'],
                                       korean_number=row['#ELL Korean'],
                                       korean_percentage=row['%ELL Korean'],
                                       urdu_number=row['#ELL Urdu'],
                                       urdu_percentage=row['%ELL Urdu']
                                       )
                db.add(school)
            db.commit()
                # db.refresh(school)
            # except:
            #     print('Something went wrong')
            pass


import_dataset.delay()
