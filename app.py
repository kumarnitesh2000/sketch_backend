from flask import Flask,render_template,make_response,url_for,redirect
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify,request
import os
from flask_cors import CORS,cross_origin
app = Flask(__name__)
CORS(app)
UploadFolder = '/home/ubuntu/sketch_backend/static/'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['UPLOAD_FOLDER'] =UploadFolder
app.config['CORS_HEADERS'] = 'Content-Type'
db = SQLAlchemy(app)


class Card(db.Model):
    id = db.Column(db.Integer ,primary_key=True)
    head = db.Column(db.String(30),nullable=False)
    title = db.Column(db.String(50) ,nullable=False )
    image = db.Column(db.String(30),nullable=False,default='default.jpeg' )

    def serialize(self):
        return {
            "id":self.id,
            "title":self.title,
            "head":self.head,
            "image_link":self.image
        }

    def __repr__(self):
        return f'{self.id} -> {self.title}'


@app.route('/api',methods= ['GET'])
@cross_origin()
def get_info_card():
    n=request.args.get('n')
    count = Card.query.count()
    try:
        if int(n) > int(count):
            return jsonify({'code':404})
    except:
        n=count

    d = Card.query.all()
    res= []
    i=0
    while i<int(n):
        res.append(d[i].serialize())
        i=i+1
    dic={'code':200,'result':res}
    response =jsonify(dic)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/api/upload',methods=['POST'])
def post_info_card():
    if request.method=='POST':
        print(request.form)
        file = request.files['file']
        head = request.form['head']
        title = request.form['title']
        image = file.filename
        c = Card(id=int(Card.query.count())+1, head=head, title=title,image=str(image))
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        db.session.add(c)
        db.session.commit()
    return redirect("https://www.flyploader.live/media/files/index_VP2zbo2.html")



#testing purpose ka liya tha

@app.route('/upload',methods=['GET','POST'])
def upload():
    if request.method=='POST':
         res=make_response(jsonify({"msg":f"tatti uploaded"}),200)
         return res



if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
