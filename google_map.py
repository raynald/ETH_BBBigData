#!/usr/bin/env python
# coding=utf-8
import flask
from flask import Flask
from flask import render_template, session, request

app = Flask(__name__)
app.debug = True
app.secret_key='this key is very secret indeed'

@app.route('/')
@app.route('/complexshow')
def complexshow(name=None):
    return render_template('complexshow.html', name=name)
@app.route('/mapshow')
def mapshow(name=None):
    # Render the cluster on Google Map
    return render_template('mapshow.html', name=name)

"""
@app.route('/quiz')
def quiz():
    # Render the quiz start page
    return render_template('quiz.html')

@app.route('/question/<step>')
def question(step):
#        Ask the user the question for this step

    if 'begin' in request.args and int(request.args['begin']):
        session.clear()

    step = int(step)
    print 'Step is %d' % step

user = None

    if 'question_list' not in flask.session or \
        'answers' not in flask.session:
        session['question_list'] = migros.GenerateQuestions(user) ## initialize this to a list of categories
        session['answers'] = [ None ] * len(session['question_list'])
    else:
        print 'Resued question list %s' % str(flask.session['question_list'])

if 'question_num' in request.args:
    qn_num = int(request.args['question_num'])
        if qn_num >= 1 and qn_num <= len(session['question_list']):
            if request.args['clicked'] == 'left':
                session['answers'][qn_num - 1] = 0
            elif request.args['clicked'] == 'right':
                session['answers'][qn_num - 1] = 1
            else:
                session['answers'][qn_num - 1] = -1

total_questions = len(flask.session['question_list'])
    country_flag_map = {
        'ES': '/static/images/spain.png',
            'CH': '/static/images/switzerland.svg',
            'DE': '/static/images/germany.gif',
            'AT': '/static/images/austria.gif',
            'IT': '/static/images/italy.gif',
            'FR': '/static/images/france.gif',
    }

if step >= total_questions:
    return results()

    args = {
        'image_left_source': session['question_list'][step][0]['image'],
            #'http://migros-cache.fsi-viewer.com/fsicache/server?type=image&source=images%2Fmigros_api%2Fstaging%2Fproduct_204015800000.jpg',
            'image_right_source': session['question_list'][step][1]['image'],
            #'http://migros-cache.fsi-viewer.com/fsicache/server?type=image&source=images%2Fmigros_api%2Fstaging%2Fproduct_204015800000.jpg',
            'lefthealth': session['question_list'][step][0]['health'],
            'righthealth': session['question_list'][step][1]['health'],
            'leftcountry': country_flag_map[session['question_list'][step][0]['country']],
            'rightcountry': country_flag_map[session['question_list'][step][1]['country']],
            'leftorganic': session['question_list'][step][0]['organic'],
            'rightorganic': session['question_list'][step][1]['organic'],
            'leftenvironment': session['question_list'][step][0]['environment'],
            'rightenvironment': session['question_list'][step][1]['environment'],
            'question_num': step,
            'total_questions': 15,
            'form_action': '/question/%d' % (int(step)+1),
            'leftname': session['question_list'][step][0]['name'],
            'rightname': session['question_list'][step][1]['name'],
            };

# Render the quiz start page
return render_template('question.html', step=step, **args)

return render_template('results.html', **args)
"""

if __name__ == '__main__':
    app.run()