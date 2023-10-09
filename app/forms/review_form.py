from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange, Length

class ReviewForm(FlaskForm):
    communication_rating = IntegerField('communication_rating', validators=[DataRequired(), NumberRange(1, 5)])
    knowledgability_rating = IntegerField('knowledgability_rating', validators=[DataRequired(), NumberRange(1, 5)])
    professionalism_rating = IntegerField('professionalism_rating', validators=[DataRequired(), NumberRange(1, 5)])
    review_body = StringField('review_body', validators=[DataRequired(), Length(max=500)])
    submit = SubmitField('Submit')