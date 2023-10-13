from flask import Blueprint, jsonify, request
from ..models import db , Review, TourGuide
from flask_login import current_user, login_required
from ..forms.review_form import ReviewForm
import datetime
from .auth_routes import validation_errors_to_error_messages

review_routes = Blueprint('reviews', __name__)

@review_routes.route('/')
def get_all_reviews():
    reviews = Review.query.all()
    reviews_data = []
    for review in reviews:
        reviews_data.append(review.to_dict())
    return jsonify(reviews_data)

@review_routes.route('/<int:id>')
def get_one_review(id):
    review = Review.query.get_or_404(id)

    if not review:
        return jsonify({"errors": "Review not found"}), 404
    
    review_dict = review.to_dict()
    return review_dict


@review_routes.route('/tour/<int:tourId>', methods=['POST'])
@login_required
def add_review(tourId):
    form = ReviewForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    tour = TourGuide.query.get_or_404(tourId)  

    if not tour:
        return jsonify({"errors": "Tour not found"}), 404
    
    if current_user.id is tour.guide_id:
        return jsonify({"errors": "Cannot review your own tour"})

    if form.validate_on_submit():
        average = (form.communication_rating.data + 
                   form.knowledgability_rating.data + 
                   form.professionalism_rating.data)/3
        review = Review(
            reviewer_id=current_user.id,
            tour_id=tour.id,
            communication_rating=form.communication_rating.data,
            knowledgability_rating=form.knowledgability_rating.data,
            professionalism_rating=form.professionalism_rating.data,
            average_rating=round(average, 2),
            review_body=form.review_body.data,
            created_at=datetime.datetime.utcnow(),
            updated_at=datetime.datetime.utcnow()
        )

        db.session.add(review)
        db.session.commit()
        return review.to_dict()
    else:
        return {"errors": validation_errors_to_error_messages(form.errors)}
    

@review_routes.route('/<int:id>', methods=['PUT'])
@login_required
def edit_review(id):
    form = ReviewForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    review = Review.query.get(id)
    if current_user.id != review.reviewer_id:
        return jsonify({"errors": "Unauthorized to edit this review"}), 403

    if form.validate_on_submit():
        attributes_to_update = ['communication_rating', 'knowledgability_rating', 'professionalism_rating', 'review_body']
        for attr in attributes_to_update:
            if hasattr(form, attr):
                setattr(review, attr, getattr(form, attr).data)


        review.updated_at = datetime.datetime.utcnow()
        average = (form.communication_rating.data + 
                   form.knowledgability_rating.data + 
                   form.professionalism_rating.data)/3
        
        review.average_rating = round(average, 2)

        db.session.commit()
        
        return review.to_dict()
    else:
        return {"errors": validation_errors_to_error_messages(form.errors)}
    

@review_routes.route('/<int:id>/', methods=['DELETE'])
def delete_review(id):
    review = Review.query.get(id)

    if not review:
        return jsonify({"errors": "Review not found"}), 404

    if current_user.id != review.reviewer_id:
        return jsonify({"errors": "Unauthorized to delete this review"}), 403

    try:
        db.session.delete(review)
        db.session.commit()

        response = {
            "message": "Review successfully deleted."
        }

        return jsonify(response)

    except Exception as e:
        db.session.rollback()
        return jsonify({"errors": "An error occurred while deleting the Review", "message": str(e)}), 500