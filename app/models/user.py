from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column, ForeignKey, Table

Base = declarative_base()


tour_specialties = db.Table(
    "tour_specialties",
    Base.metadata,
    Column("specialty_id", db.Integer, ForeignKey(add_prefix_for_prod("specialties.id")), primary_key=True),
    Column("specialty_tour_id", db.Integer, ForeignKey(add_prefix_for_prod("tour_guides.id")), primary_key=True))

tour_dates = db.Table(
    "tour_dates",
    Base.metadata,
    Column("date_id", db.Integer, ForeignKey(add_prefix_for_prod("dates.id")), primary_key=True),
    Column("tour_id", db.Integer, ForeignKey(add_prefix_for_prod("tour_guides.id")), primary_key=True))

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    joined_on = db.Column(db.DateTime(), nullable=False)
    student = db.Column(db.Boolean(50), nullable=False)
    graduation_date = db.Column(db.DateTime(), nullable=True)
    profile_pic = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime(), nullable=False)
    updated_at = db.Column(db.DateTime(), nullable=False)

    tours_given = db.relationship("TourGuide", back_populates='guide')
    reviews = db.relationship("Review", back_populates='reviewer')
    tourist_tours = db. relationship("Booking", back_populates='tourist')

    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'last_name': self.last_name,
            'first_name': self.first_name,
            'joined_on': self.joined_on,
            'student': self.student,
            'graduation_date': self.graduation_date,
            "profile_pic": self.profile_pic,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'reviews': self.reviews,
            'tourist_tours': self.tourist_tours,

        }
    
class Booking(db.Model):
    __tablename__ = 'bookings'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer,autoincrement=True, primary_key=True)
    tourist_id = db.Column(db.Integer,db.ForeignKey(add_prefix_for_prod("users.id")))
    tour_guide_id = db.Column(db.Integer,db.ForeignKey(add_prefix_for_prod("tour_guides.id")))
    date = db.Column(db.DateTime(), nullable=False)
    start_time = db.Column(db.DateTime(), nullable=False)
    duration = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False)
    updated_at = db.Column(db.DateTime(), nullable=False)

    tourist = db. relationship("User", back_populates='tourist_tours')
    tour_guide = db.relationship("TourGuide", back_populates='bookings')

    def to_dict(self):
        return {
            'id': self.id,
            'tour_guide_id': self.tour_guide_id,
            'tourist_id': self.tourist_id,
            'date': self.date,
            'start_time': self.start_time,
            'duration': self.duration,
            'tourist': self.tourist,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }
    
class City(db.Model):
    __tablename__ = 'cities'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.Integer, nullable=False, unique=True)

    tours_given = db.relationship("TourGuide", back_populates="cities")

    def to_dict(self):
        return {
            'id': self.id,
            'city': self.city,
            'tours_given': self.tours_given
        }
    
class Date(db.Model):
    __tablename__ = 'dates'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(255), nullable=False, unique=True)

    tours = db.relationship("TourGuide", secondary=tour_dates, back_populates="dates", cascade='all, delete')

    def to_dict(self):
        return {
            'id': self.id,
            'date': self.date,
            'tours': self.tours
        }
    
class Review(db.Model):
    __tablename__= 'reviews'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}


    id = db.Column(db.Integer,primary_key=True)
    reviewer_id = db.Column(db.Integer,db.ForeignKey(add_prefix_for_prod("users.id")))
    tour_id = db.Column(db.Integer,db.ForeignKey(add_prefix_for_prod("tour_guides.id")))
    average_rating = db.Column(db.Float, nullable=False)
    communication_rating = db.Column(db.Integer, nullable=False)
    knowledgability_rating = db.Column(db.Integer, nullable=False)
    professionalism_rating = db.Column(db.Integer, nullable=False)
    review_body = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now())

    reviewer = db.relationship("User", back_populates="reviews")
    tour = db.relationship("TourGuide", back_populates="reviews")

    def to_dict(self):
        return {
            'id': self.id,
            'reviewer_id': self.reviewer_id,
            'average_rating': self.average_rating,
            'communication_rating': self.communication_rating,
            'knowledgeability_rating': self.knowledgability_rating,
            'professionalism_rating': self.professionalism_rating,
            'review_body': self.review_body,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'guide': self.guide
        }

class Specialty(db.Model):
    __tablename__ = 'specialties'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer,autoincrement=True, primary_key=True)
    specialty = db.Column(db.String(50), nullable=False)

    tours = db.relationship("TourGuide", secondary=tour_specialties, back_populates='specialties', cascade='all, delete')

    def to_dict(self):
        return {
            'id': self.id,
            'specialty': self.specialty,
            'tours': self.tours
        }

class TourGuide(db.Model):
    __tablename__ = 'tour_guides'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    guide_id = db.Column(db.Integer,db.ForeignKey(add_prefix_for_prod("users.id")), nullable=False)
    city_id = db.Column(db.Integer,db.ForeignKey(add_prefix_for_prod('cities.id')), nullable=False)
    language = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    about = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False)
    updated_at = db.Column(db.DateTime(), nullable=False)

    guide = db.relationship("User", back_populates='tours_given')
    cities = db.relationship("City", back_populates="tours_given")
    bookings = db.relationship("Booking", back_populates='tour_guide')
    reviews = db.relationship("Review", back_populates="tour")

    specialties = db.relationship("Specialty", secondary=tour_specialties, back_populates='tours', cascade='all, delete')
    dates = db.relationship("Date", secondary=tour_dates, back_populates='tours', cascade='all, delete')

    def to_dict(self):
        return {
            'id': self.id,
            'guide_id': self.guide_id,
            'city_id': self.city_id,
            'language': self.language,
            'price': self.price,
            'about': self.about,
            'bookings': self.bookings,
            'guide': self.guide,
            'specialties': self.specialties,
            'dates': self.dates,
            'reviews': self.reviews,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }