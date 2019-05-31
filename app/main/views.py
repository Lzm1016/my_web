#!/usr/bin/env python3

# @FileName : views.py
# @作者 : Liu
# @日期 : 2019年05月13日
# @时间 : 18时05分

from flask import render_template, redirect, url_for, request
from flask_login import login_required, current_user

from app import db
from app.model import Post, Comment, User
from . import main
from .forms import CommentForm, PostForm


@main.route("/")
@main.route("/id=<int:id>")
def index(id=0):
    if id != 0:
        page_index = request.args.get('page', 1, type=int)
        quer = Post.query.filter_by(users_id=id)
        pagination = quer.paginate(page_index, per_page=20, error_out=False)
        post = pagination.items
        user = User.query.get(id)
        title = '欢迎来到%s的博客' % user.name
    else:
        # post = Post.query.all()
        page_index = request.args.get('page', 1, type=int)
        quer = Post.query.order_by(Post.created.desc())
        pagination = quer.paginate(page_index, per_page=20, error_out=False)
        post = pagination.items
        title = '欢迎'

    return render_template('index.html', title=title, post=post, pagination=pagination)


@main.route("/about")
def about():
    return render_template('about.html', title='关于')


# @main.route("/admin")
# def admin():
#     return 'Admin'

@main.route("/post/<int:id>", methods=['GET', 'POST'])
def post(id):
    # Detail 详情
    post = Post.query.get_or_404(id)

    # 评论窗体
    form = CommentForm()

    # 保存评论
    if form.validate_on_submit():
        comment = Comment(body=form.body.data, posts=post, users=current_user)
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('main.post', id=post.id))
    # 评论列表

    return render_template('detail.html', title=post.title,
                           form=form, post=post)


@main.route('/edit', methods=['GET', 'POST'])
@main.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id=0):
    form = PostForm()
    if id == 0:
        # 新增
        post = Post(users=current_user)
    else:
        # 修改
        post = Post.query.get_or_404(id)
        form.title.data = post.title
        form.body.data = post.body

    if form.validate_on_submit():
        form = PostForm()
        post.title = form.title.data
        post.body = form.body.data

        # post = Post(title=form.title.data, body=form.body.data)

        db.session.add(post)
        db.session.commit()
        return redirect(url_for('main.post', id=post.id))

    title = '添加新文章'
    if id > 0:
        title = '编辑 - %s' % post.title
    return render_template('edit.html', title=title,
                           form=form, post=post)


@main.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@main.app_template_filter()
def format_time(time):
    # astimezone() linux 服务上回报错
    new_time = time.strftime('%Y-%m-%d %H:%M:%S')
    return new_time
