from flask_app import app   
from flask import render_template, redirect, request, flash, session
from flask_app.models.user_model import User
from flask_app.models.post_model import Post
from flask_app.models.comment_model import Comment




@app.route('/comment/create/<int:post_id>', methods =['POST'])
def post_comment(post_id):
    if 'user_id' not in session:
        return redirect('/')
        # Make a new Validator for Comments
    # if not Post.validator(request.form):
    #     return redirect('/post/new')

    data = {
        **request.form,
        'user_id':session['user_id'],
        'post_id':post_id
    }
    Comment.create(data)
    
    return redirect(f'/posts/{post_id}')







