from models import Dog

def create_table(base, engine):
    base.metadata.create_all(bind=engine)

def save(session, dog):
    session.add(dog)
    session.commit()


def get_all(session):
    return session.query(Dog).all()


def find_by_name(session, name):
    return session.query(Dog).filter_by(name=name).first()


def find_by_id(session, id):
    return session.query(Dog).filter_by(id=id).first()

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter_by(name=name, breed=breed).first()


def update_breed(session, dog, breed):
    dog.breed = breed
    session.commit()

from sqlalchemy import create_engine, orm

# engine = create_engine('your_database_url')  # Replace 'your_database_url' with the actual database URL.
# Session = orm.sessionmaker(bind=engine)
# session = Session()
# Example usage:



#!
# dog1 = Dog(name='Buddy', breed='Golden Retriever')
# save(session, dog1)

# all_dogs = get_all(session)
# print(all_dogs)

# dog_by_name = find_by_name(session, 'Buddy')
# print(dog_by_name)

# ... (use other functions as needed)
