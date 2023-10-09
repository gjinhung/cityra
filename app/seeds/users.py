from app.models import db, User, City, Date, Review, Booking, TourGuide, Specialty, environment, SCHEMA
from sqlalchemy.sql import text
import datetime

# Adds a demo user, you can add other users here if you want
def seed_users():
    print('demo start')
    demo = User(
        username='Demo', 
        email='demo@aa.io', 
        password='password', 
        first_name='Demo',
        last_name="Stration",
        profile_pic="https://publichealth.uga.edu/wp-content/uploads/2020/01/Thomas-Cameron_Student_Profile.jpg",
        joined_on=datetime.datetime.now(),
        student=True,
        graduation_date=datetime.date(2024, 5, 24),
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now())
    print('demo1 complete')
    
    demo2 = User(
        username='Demo2', 
        email='demo2e@aa.io', 
        password='password',
        first_name='Demo',
        last_name="Lition",
        profile_pic="https://png.pngtree.com/background/20230426/original/pngtree-young-professional-asian-college-man-with-glasses-picture-image_2489385.jpg",
        joined_on=datetime.datetime.now(),
        student=True,
        graduation_date=datetime.date(2024, 5, 24),
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now())
    
    demo3 = User(
        username='Demo3', 
        email='demo3@aa.io', 
        password='password',
        first_name='Demo',
        last_name="Lition",
        profile_pic="https://3.bp.blogspot.com/-uXdYwoAZnDM/W1dzL3uLkoI/AAAAAAAADY0/RVbd3BlqORsT_aUNHVHDEIxxxNIaspLrwCLcBGAs/s1600/IMG_6141.JPG",
        joined_on=datetime.datetime.now(),
        student=False,
        graduation_date=None,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now())

    new_york = City(
        city="New York",
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now())
    los_angeles = City(
        city="Los Angeles",
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now())
    seattle = City(
        city="Seatle",
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now())

    review1 = Review(
        reviewer_id=3, 
        guide=demo,
        communication_rating=5,
        knowledgability_rating=4,
        professionalism_rating=5,
        average_rating=round(((5+4+5)/3), 2),
        review_body='Demo was a very friendly person with lots of knowledge of the city',
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now())
    review2 = Review(
        reviewer_id=3, 
        guide_id=2,
        communication_rating=5,
        knowledgability_rating=4,
        professionalism_rating=5,
        average_rating=round(((5+4+5)/3), 2),
        review_body='Demo2 was a very friendly person with lots of knowledge of the city',
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now())
    review3 = Review(
        reviewer_id=1, 
        guide_id=2,
        communication_rating=5,
        knowledgability_rating=4,
        professionalism_rating=5,
        average_rating=round(((5+4+5)/3), 2),
        review_body='Demo3 was a very friendly person with lots of knowledge of the city',
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now())
    
    booking1 = Booking(
        tour_guide_id=1, 
        date=datetime.date(2024, 1, 1),
        start_time=datetime.time(9),
        duration=2,
        tourist=demo3,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now())
    
    booking2 = Booking(
        tourist_id=3, 
        date=datetime.date(2024, 2, 1),
        start_time=datetime.time(9),
        duration=3,
        tour_guide=2,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now())
    booking3 = Booking(
        tourist_id=1, 
        tour_guide_id=2, 
        date=datetime.date(2024, 1, 15),
        start_time=datetime.time(13),
        duration=2,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now())

    tour1 = TourGuide(
        guide_id=1, 
        city_id=1,
        language="English",
        price=40,
        about='Born and raised in NYC. I"ve spent a lot of money and time, traveling around, taking pictures and eating all over New York. Come with me on a journey to explore New York',
        # dates=[monday],
        # specialties=[food],
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now())
    # tour2 = TourGuide(
    #     language="English",
    #     price=20,
    #     about='Born and raised in LA. I"ve spent a lot of money and time, traveling around, taking pictures and eating all over New York. Come with me on a journey to explore Los Angeles.',
    #     guide=demo2,
    #     cities=los_angeles,
    #     # specialties=[other],
    #     # dates=[wednesday],
    #     created_at=datetime.datetime.now(),
    #     updated_at=datetime.datetime.now())
    # tour3 = TourGuide(
    #     guide_id=2, 
    #     city_id=3,
    #     language="Chinese",
    #     price=50,
    #     about='Born and raised in Seattle. I"ve spent a lot of money and time, traveling around, taking pictures and eating all over New York. Come with me on a journey to explore Seattle',
    #     # specialties=[adventure],
    #     # dates=[friday],
    #     created_at=datetime.datetime.now(),
    #     updated_at=datetime.datetime.now())
    

    food = Specialty(
        specialty="Food",
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now())
    
    history = Specialty(
        specialty="History",
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now())
    
    adventure = Specialty(
        specialty="Adventure",
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now())

    other = Specialty(
        specialty="Other",
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now())
    
        
    monday = Date(
        date="Monday",
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now())
    # tuesday = Date(
    #     date="Tuesday",
    #     created_at=datetime.datetime.now(),
    #     updated_at=datetime.datetime.now())
    # wednesday = Date(
    #     date="Wednesday",
    #     created_at=datetime.datetime.now(),
    #     updated_at=datetime.datetime.now())
    # thursday = Date(
    #     date="Thursday",
    #     created_at=datetime.datetime.now(),
    #     updated_at=datetime.datetime.now())
    # friday = Date(
    #     date="Friday",
    #     created_at=datetime.datetime.now(),
    #     updated_at=datetime.datetime.now())
    # saturday = Date(
    #     date="Saturday",
    #     created_at=datetime.datetime.now(),
    #     updated_at=datetime.datetime.now())
    # sunday = Date(
    #     date="Sunday",
    #     created_at=datetime.datetime.now(),
    #     updated_at=datetime.datetime.now()) 
    
    tour1.dates.append(monday)


    db.session.add[tour1, 
                #    tour2, tour3, 
                   demo, demo2, demo3, 
                   seattle, new_york, los_angeles, 
                   monday, tuesday, wednesday, thursday, friday, saturday, sunday,
                   booking1, booking2, booking3,
                   review1, review2, review3,
                   adventure, history, food, other
                   ]
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM users"))
        
    db.session.commit()