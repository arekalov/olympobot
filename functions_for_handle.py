from orm_data.review import Review


def is_marked(db_sess, user_id, new_mark):
    if db_sess.query(Review).filter(Review.user_id == user_id, Review.mark == None).first():

