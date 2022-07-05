
from turtle import color
from flask import Flask, render_template, request, redirect, jsonify
from flask_cors import CORS, cross_origin

from utils import logger
from utils.Check_ratings import ratings
import os
import pandas as pd



log = logger.log(log_for=__name__, log_file= 'app.log')

app = Flask(__name__)

@app.route('/')
@cross_origin()
def index():
    return render_template('index.html')



@app.route('/upload', methods=['POST', 'GET'])
@cross_origin()
def upload():
    if request.method == 'POST':
        log.write('upload page is being accessed', 'info')
        
        file = ''.join([file for file in os.listdir("uploads")])
        
        if len(file)!=0:
            
            file_path = "uploads/"+file 
            os.remove(file_path)
            log.write('old file has been deleted', 'info')
            #new file read
            f = request.files['file']
            f.save(os.path.join('uploads', f.filename))
            log.write('file has been uploaded', 'info')
            
            
        else:
            file_path = "uploads/" 
            log.write('old file has been deleted', 'info')
            #new file read
            f = request.files['file']
            f.save(os.path.join('uploads', f.filename))
            log.write('file has been uploaded', 'info')
        
        # filename = f.filename

        # upload_csv_file(db = 'test', collection = 'test', filename=filename)
        log.write('csv file has been uploaded', 'info')
        return redirect("/check_ratings")
    else:
        log.write('upload page is being accessed --> rendering the upload.html template', 'info')
        return render_template('index.html')


@app.route('/check_ratings', methods = ['GET', 'POST'])
@cross_origin()
def check_ratings():
    if request.method == 'POST':
        try:
            rating = int(request.form['rating'])
            name = str(request.form['name'])
        
            data = ratings.check_rating(name=name, rating=rating)
            # print(data)
            number_of_Ratings = len(data)
            
            return f"<h1> Number of {rating} star ratings {name} got: {number_of_Ratings} </h1>\n"
        except Exception as e:
            log.write(e, 'error processing')
            print ('error processing errors \n',e)

    else:
        return render_template('form.html')


            


if __name__ == '__main__':
    app.run(debug=True)
