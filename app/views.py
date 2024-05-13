import os
from app import app
from flask import render_template, request, flash, redirect, url_for, jsonify, send_from_directory
from werkzeug.utils import secure_filename
from app.forms import SearchForm, UploadForm


import json
###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')

# @app.route('/translator', methods=['GET', 'POST'])
@app.route('/translator', methods=['GET'])
def translator():

    # filename = secure_filename(profile_photo.filename)
    # profile_photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        

    formSearch = SearchForm()
    formSearch.select_field.choices = getSearchChoices()  
    
    formUpload = UploadForm()
   
    return render_template('translator.html', searchForm=formSearch, uploadForm=formUpload,translation=request.args.get('translation'))

@app.route('/processUpload', methods=['POST'])
def processUpload():

    form = UploadForm()

    if form.validate_on_submit():
        
        # Get file data and save to your uploads folder
        vid = form.video.data
        filename = secure_filename(vid.filename)
        vid.save(os.path.join(
            app.config['UPLOAD_FOLDER'], filename
        ))

        #query model here
        translation = filename #test
        
        return redirect(url_for('translator', translation=translation))
    
    return 'An error occurred with submitting the form'  


     

@app.route('/processSearch', methods=['POST'])
def processSearch():
    form = SearchForm()
    form.select_field.choices = getSearchChoices() 

    if form.validate_on_submit():
        
        selected_text = form.select_field.data
        #mak query with selected text

        #query database here
        if selected_text == 'Hello How Are You':
            translation = "pets"
        elif selected_text == 'What is your Name':
            translation = "snacks"
        else:
            translation = """no"""
            
        return redirect(url_for('translator', translation=translation))
    
    return 'An error occurred with submitting the form'
         


@app.route('/resources')
def resources():
    return render_template('resources.html')


@app.route('/about')
def about():
    return render_template('about.html')

def getSearchChoices():
    # Example: Fetch state choices from database
    # dbFetch = ['Alabama', 'Alaska', 'Alaska']
    # choices = [('', 'Select a state...')]

    # for choice in dbFetch:
    #     choices.append((choice, choice))


    choices = ["Hello How Are You", "What is your name", "no"]
    return choices
###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
