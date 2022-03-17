from app import app
from flask import render_template, request
from .services import show_info, sitcom_short_list, reality_show_short_list, dramas_short_list, supernatural_short_list, action_short_list, docuseries_short_list, romance_short_list, dramas_list1, dramas_list2, dramas_list3, dramas_list4, medical_dramas, crime_docuseries, food_docuseries, travel_docuseries, nature_docuseries, learning_docuseries, romance_shows, reality_romances, reality_shows1, reality_cooking_shows, supernatural_shows, fantasy_shows, sci_fi_shows, thrillers_series1, thrillers_series2
from .forms import ShowSearch

import requests as r




@app.route('/')
def home():
    homepage_romances = show_info(romance_short_list)
    homepage_docuseries= show_info(docuseries_short_list)
    homepage_sitcoms = show_info(sitcom_short_list)
    homepage_reality = show_info(reality_show_short_list)
    homepage_dramas = show_info(dramas_short_list)
    homepage_supernatural = show_info(supernatural_short_list)
    homepage_action= show_info(action_short_list)
    return render_template('mainlandingpage.html', homepage_romance_reel = homepage_romances, homepage_docuseries_reel=homepage_docuseries, homepage_action_reel=homepage_action, homepage_supernatural_reel=homepage_supernatural, homepage_reality_reel=homepage_reality, homepage_sitcom_reel=homepage_sitcoms, homepage_dramas_reel=homepage_dramas)

@app.route('/action')
def action_shows():
    action_show_list= {'Blindspot': 1855, 'Vikings':29, 'Burn Notice': 667, 'Money Heist':27436, 'Arrow':4, 'The Flash':13, 'CSI: NY': 749, 'Chuck':168, 'Covert Affairs':345}
    action_shows=show_info(action_show_list)
    return render_template ('action.html', actions=action_shows)

@app.route('/comedy')
def comedy_shows():
    sitcom_list1 = {'The Marvelous Mrs. Maisel':19807, 'The Big Bang Theory': 66, 'Silicon Valley':143, 'The Good Place':2790, 'Rules of Engagement':720, 'Community': 318, 'Brooklyn Nine-Nine':49, 'Modern Family': 80, 'Friends':431, 'The Office':526, '2 Broke Girls': 124}
    sitcoms1 = show_info(sitcom_list1)
    sitcom_list2 = {'It\'s Always Sunny in Philadelphia': 347, 'Young and Hungry': 1745, 'Schitt\'s Creek': 1775, 'Arrested Development': 321, 'Seinfeld':530, 'Parks and Recreation': 174, 'Younger':623, 'Superstore': 1864, 'Space Force': 40445, 'Kim\'s Convenience':17312, '8 Simple Rules':984}
    sitcom2= show_info(sitcom_list2)
    animated_series = {'The Simpsons':83, 'Bob\'s Burgers':107, 'South Park':112, 'BoJack Horseman':184, 'Disenchantment':30715, 'Rick and Morty': 216, 'Futuruma': 538, 'Paradise PD':35820}
    animateds= show_info(animated_series)
    #live_specials = {'The Standups':29821, 'The Comedy Lineup':37695, 'Comedians in Cars Getting Coffee': 1645}
    return render_template ('comedy.html', sitcom1=sitcoms1, sitcom2=sitcom2, animated=animateds)


@app.route('/drama')
def drama_shows():
    dramas1 = show_info(dramas_list1)
    dramas2 = show_info(dramas_list2)
    dramas3 = show_info(dramas_list3)
    dramas4 = show_info(dramas_list4)
    return render_template ('drama.html', dramas1=dramas1, dramas2=dramas2, dramas3=dramas3, dramas4=dramas4)

@app.route('/docuseries')
def docuseries():
    crimes = show_info(crime_docuseries)
    food = show_info(food_docuseries)
    travel=show_info(travel_docuseries)
    nature=show_info(nature_docuseries)    
    learnings=show_info(learning_docuseries)
    return render_template ('docuseries.html', crimes=crimes, food=food, travel=travel, nature=nature,learning=learnings)

@app.route('/reality')
def reality_shows():
    reality_show1=show_info(reality_shows1)
    reality_cooking=show_info(reality_cooking_shows)
    return render_template ('reality.html', reality_show1=reality_show1, reality_cooking=reality_cooking)

@app.route('/romance')
def romance():
    romances=show_info(romance_shows)    
    reality_romance = show_info(reality_romances)
    return render_template ('romance.html', romances=romances, reality_romance=reality_romance)

@app.route('/supernatural')
def supernatural():
    supernatural=show_info(supernatural_shows)
    return render_template ('supernatural.html', supernatural=supernatural)

@app.route('/thriller')
def thriller():
    thrillers1 = show_info(thrillers_series1)
    thrillers2 = show_info(thrillers_series2)
    return render_template ('thriller.html', thrillers1=thrillers1, thrillers2=thrillers2)

@app.route('/search', methods=['GET','POST'])
def search():
    search_form = ShowSearch() # instantiation of ShowSearch class; will be used in both Get and Post sides of this route
    if request.method =="POST":
        results={}
        if (search_form.showname.data).strip().count(' ') > 0:
            new_string="+".join((search_form.showname.data).split(' '))
            datapick=r.get(f'https://api.tvmaze.com/search/shows?q={new_string}').json()
            print(f'type1 + {type(datapick)}, {len(datapick)}')
            print ([datapick[i]['show']['name'] for i in range(len(datapick))])
        elif (search_form.showname.data).strip().count(' ') == 0:
            print(search_form.showname.data)
            datapick =r.get(f'https://api.tvmaze.com/search/shows?q={search_form.showname.data}').json()
            listindeces = [datapick[i]['show']['name'] for i in range(len(datapick)) if type(datapick)==list ]
            print(type(datapick))
            print(listindeces)
            print ('type2')
        else:
            datapick = r.get(f'https://api.tvmaze.com/search/shows?q={search_form.showname.data}').json()
        for i in range(len(datapick)):
            results[datapick[i]['show']['name']]=datapick[i]['show']['id']
        search_form=show_info(results)
        return render_template('search.html', search_form=search_form)
    return render_template('search.html', search_form=search_form) # works for our get requests



