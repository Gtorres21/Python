from flask_app import app   
from flask import render_template, redirect, request, flash, session
from flask_app.models.user_model import User
from flask_app.models.post_model import Post
from flask_app.models.comment_model import Comment




@app.route('/post/new')
def new_post_form():
    if 'user_id' not in session:
        return redirect('/')
    # Same thing as making the user_data dictionary in our welcome route in user controller, this is the synonymous way
    # logged_user = User.get_by_id({'id':session['user_id']})
    user_data = {
        'id': session['user_id']
    }
    logged_user = User.get_by_id(user_data)
    return render_template("post_new.html", logged_user = logged_user)

@app.route('/post/create', methods =['POST'])
def process_post():
    if 'user_id' not in session:
        return redirect('/')
    if not Post.validator(request.form):
        return redirect('/post/new')

    data = {
        **request.form,
        'user_id':session['user_id']
    }
    Post.create(data)
    
    return redirect('/welcome')



@app.route('/posts/<int:id>')
def show_post(id):
    if 'user_id' not in session:
        return redirect('/')
    user_data = {
        'id': session['user_id']
    }
    logged_user = User.get_by_id(user_data)
    post = Post.get_by_id({'id':id})
    all_post = Post.get_all()
    post_comment = Comment.get_by_id({'id':id})
    # print('***************************************************')
    # print(post_comment[0])
    return render_template('posts_one.html', post = post, logged_user = logged_user, all_post = all_post, post_comment = post_comment)

@app.route('/posts/<int:id>/delete')
def delete_post(id):
    if 'user_id' not in session:
        return redirect('/')
    post = Post.get_by_id({'id': id})
    if not int(session['user_id']) == post.user_id:
        return redirect('/welcome')
    Post.delete({'id': id})
    return redirect('/welcome')

@app.route('/posts/<int:id>/edit')
def edit_post(id):
    if 'user_id' not in session:
        return redirect('/')
    post = Post.get_by_id({'id': id})
    if not int(session['user_id']) == post.user_id:
        return redirect('/welcome')
    post = Post.get_by_id({'id': id})
    return render_template('post_edit.html', post = post)

@app.route('/posts/<int:id>/update', methods=['POST'])
def update_post(id):
    if 'user_id' not in session:
        return redirect('/')
    post = Post.get_by_id({'id':id})
    if not int(session['user_id']) == post.user_id:
        return redirect('/welcome')
    if not Post.validator(request.form):
        return redirect(f'/posts/{id}/edit')
    data = {
        **request.form,
        'id':id
    }
    Post.update(data)
    return redirect('/welcome')


