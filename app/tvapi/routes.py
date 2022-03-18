# initial blueprint setup

import json
from flask import Blueprint, jsonify, request

from app.models import db, TelevisionSeries

api=Blueprint('api',__name__, url_prefix='/api')


# @api.route('/test')
# def test():
#     # jsonify? transforms python dict or list into json data
#     return jsonify({'datadatadata': 'its actually working'})

# route for getting all series info
@api.route('/series', methods=(['GET']))
def getAllSeries():
    """
    [GET] return json data on all of the series in our database
    """
    # 1. query all series
    #allseries = TelevisionSeries.query.all()
    #for a in TelevisionSeries.query.all():
        # allseries.append(a.to_dict())
#        print(allseries,allseries[0].to_dict())
    allseries=[a.to_dict() for a in TelevisionSeries.query.all()]
    # 2. jsonify the results of .to_dict() for each series in that query
    return jsonify(allseries)
# route for getting one series info


# route for creating a new series
@api.route('/add/series', methods=['POST'])
def create_series():
    """
    [POST] creates a new instance in our database with data provided in the request body expected format:
    {
        'show_title': <str>
        'seasons': <int>
        'genre': <str>
        'network':<str>
        'language':<str>
        'status':<str>
        'description':<str>
    }   

    """
     # grab any json data from body of request made to this route
    # depending on how specific we want our data to be - may want to build out some checks on the data coming in
    # does it actually make sense? is it something we want in our database?
    # otherwise, create the new series in the database

    # check= TelevisionSeries.query.filter_by(genre=data.get('genre').first()
    # if check:
    #     return jsonify({'Create Series Rejected':'Series already exists or improper request'})
    
    try:
        data= request.get_json()
        new_series = TelevisionSeries(data)
        db.session.add(new_series)
        db.session.commit()
        return jsonify({'New Series Added': new_series.to_dict() }), 201
    except:
        return jsonify({'Create Series Rejected.': 'Series already exists or improper input'}), 400


# route for getting one new show - dynamic route
# func for route will expect input coming through via url
@api.route('/series/show_title/<string:show_title>', methods=['GET'])
def getOneSeries(show_title):
    """
    [GET] that accepts a series name through the url and either gets the series in our database or return that we dont have that series in our database
    """
    tv = TelevisionSeries.query.filter_by(show_title=show_title.title()).first()
    if tv:
        return jsonify(tv.to_dict()),200
    else:
        return jsonify({'Request failed':'No series with that name in our database'})

@api.route('/series/remove/<string:id>', methods=['DELETE'])
def removeSeries(id):
        # check if show exists in database
    series= TelevisionSeries.query.get(id)
    if not series: # if no series with that id in the database
        # tell user remove failed
        return jsonify({'There was no series in that database to remove'})
    db.session.delete(series)
    db.session.commit()
    return jsonify({'Removed series from database': series.to_dict()}), 200

@api.route('/series/update/<string:id>', methods=['PUT']) # put requests include data being 
def updateSeries(id):
    try:
    # grab the request body and query the database for a series with that ID
    # update the animal object
    # recommit it to the database
        series=TelevisionSeries.query.get(id)
        data=request.get_json()
        series.from_dict(data)
        db.session.commit()
        return jsonify({'Updated Series Info:': series.to_dict()}),200
    except:
        return jsonify({'Request failed': 'Invalid ID'}), 400
