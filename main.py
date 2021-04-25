from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
api = Api(app)

### Database Setup
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tmp/database.db'
db = SQLAlchemy(app)

class ReviewModel(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    brand = db.Column(db.Text, nullable=False)
    variety = db.Column(db.Text, nullable=False)
    style = db.Column(db.Text, nullable=False)
    country = db.Column(db.Text, nullable=False)
    stars = db.Column(db.Float, nullable=False)
    top_ten = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"Review(brand = {brand}, variety = {variety}, style = {style}, country = {country}, stars = {stars}, top_ten = {top_ten})"

# db.create_all() # only first time

review_post_args = reqparse.RequestParser()
review_post_args.add_argument("brand", type=str, help="Required Field(s) is Missing", required=True)
review_post_args.add_argument("variety", type=str, help="Required Field(s) is Missing", required=True)
review_post_args.add_argument("style", type=str, help="Required Field(s) is Missing", required=True)
review_post_args.add_argument("country", type=str, help="Required Field(s) is Missing", required=True)
review_post_args.add_argument("stars", type=float, help="Required Field(s) is Missing", required=True)
review_post_args.add_argument("top_ten", type=str)

review_put_args = reqparse.RequestParser()
review_put_args.add_argument("brand", type=str)
review_put_args.add_argument("variety", type=str)
review_put_args.add_argument("style", type=str)
review_put_args.add_argument("country", type=str)
review_put_args.add_argument("stars", type=float)
review_put_args.add_argument("top_ten", type=str)

resource_fields = {
    'id': fields.Integer,
    'brand': fields.String,
    'variety': fields.String,
    'style': fields.String,
    'country': fields.String,
    'stars': fields.Float,
    'top_ten': fields.String
}

def abort_if_records_does_not_exist(review_id):
    if review_id not in reviews:
        abort(404, message="Could not find review...")

def abort_if_records_exist(review_id):
    if review_id not in reviews:
        abort(409, message="Could not find review...")

class Review(Resource):
    @marshal_with(resource_fields)
    def post(self):
        args = review_post_args.parse_args()
        review = ReviewModel(
            brand=args['brand'], 
            variety=args['variety'], 
            style=args['style'], 
            country=args['country'], 
            stars=args['stars'], 
            top_ten=args['top_ten'],
        )
        
        db.session.add(review)
        db.session.commit()
        return review, 201

class ManageReview(Resource):

    @marshal_with(resource_fields)
    def put(self, review_id):
        result = ReviewModel.query.filter_by(id=review_id).first()
        if not result:
            abort(404, message="Review does not exist, cannot update")

        args = review_put_args.parse_args()
        
        if args['brand']:
            result.brand = args['brand']
        if args['variety']:
            result.variety = args['variety']
        if args['style']:
            result.style = args['style']
        if args['country']:
            result.country = args['country']
        if args['stars']:
            result.stars = args['stars']
        if args['top_ten']:
            result.top_ten = args['top_ten']

        db.session.commit()
        return result

    def delete(self, review_id):
        result = ReviewModel.query.filter_by(id=review_id).first()

        if not result:
            abort(404, message="Review does not exist, cannot delete")

        db.session.delete(result)
        db.session.commit()
        return '', 204

class ReviewFilterByCountry(Resource):
    def get(self, country):
        result = ReviewModel.query.filter_by(country=country).all()
        return { 'result': [result] }

api.add_resource(Review, "/reviews")
api.add_resource(ManageReview, "/reviews/<int:review_id>")
api.add_resource(ReviewFilterByCountry, "/reviews/<string:country>")
# api.add_resource(SearchReviewBy, "/reviews/<string:country>")

if __name__ == "__main__":
    app.run(debug=True)