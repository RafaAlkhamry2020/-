from flask import Flask, render_template ,request ,redirect ,url_for
from store import Post, PostStore

app = Flask(__name__)

dummy_posts = [
    Post(id=1,
         photo_url='https://images.pexels.com/photos/415829/pexels-photo-415829.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=50&w=50',
         name='Sara',
         body='Lorem Ipsum'),
    Post(id=2,
         photo_url='https://images.pexels.com/photos/736716/pexels-photo-736716.jpeg?auto=compress&cs=tinysrgb&dpr=1&h=100&w=100',
         name='John',
         body='Lorem Ipsum'),
]
post_store = PostStore()
post_store.add(dummy_posts[0])
post_store.add(dummy_posts[1])

app.current_id = 3

@app.route('/')
def Home():
    return render_template('index.html',posts=post_store.get_all())

@app.route('/post_add.html',methods=['GET','POST'])
def post_add():
    if request.method=='POST' :
        new_post=Post(id= app.current_id+1,
                      photo_url=request.form['photo_url'],
                      name=request.form['name'],
                      body=request.form['body'])

        post_store.add(new_post)
        return redirect(url_for('Home'))
    elif request.method=='GET' :
        return render_template('post_add.html ')


app.run()


