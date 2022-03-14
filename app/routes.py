from app import app
from flask import render_template
from .services import show_info



@app.route('/')
def home():
    sitcom_short_list = {'Arrested Development':321, 'The Simpsons': 83, 'Parks and Recreation':174, 'Brooklyn Nine-Nine':49, 'Friends':431, 'Community':318, 'The Office':526, 'Young and Hungry':1745, 'It\'s Always Sunny in Philadelphia':347, 'The Standups':29821}
    reality_show_short_list = {'Keeping Up with the Kardashians': 575, 'Love is Blind': 46167, 'The Bachelor': 914, 'Married at First Sight': 2709, '90 Day Fiance':3139}
    dramas_short_list = {'24':167, 'Breaking Bad':169, 'Dirty John':34649, 'Pieces of Her':40864,'CSI: Miami':576, 'Squid Game': 43687, 'Grey\'s Anatomy':67, 'How to Get Away with Murder':52, 'Scandal':98, 'American Crime Story': 2029}
    supernatural_short_list = {'Game of Thrones': 82, 'The Flash':13, 'A Discovery of Witches': 31339, 'The Boys':15299, 'The Magicians': 3083, 'The Vampire Diaries':63, 'Stranger Things':2993, 'Shadowhunters':2158 , 'The Umbrella Academy': 30386, }
    action_short_list = {'Blindspot': 1855, 'Vikings':29, 'Burn Notice': 667, 'Money Heist':27436, 'Arrow':4, 'The Flash':13, 'CSI: NY': 749, 'Chuck':168, 'Covert Affairs':345}
    docuseries_short_list = {'Restaurants on the Edge':46285, 'Chef\'s Table':3252, 'Anthony Bourdain: Parts Unknown':255, 'Night on Earth': 46002, 'Attenborough: Life in Colour':53687, 'Our Planet':17868,'Formula 1: Drive to Success': 41074, 'My Next Guest': 34258, 'Making a Murderer':7989, 'Wild Wild Country': 35097, 'Explained':36901}
    romance_short_list = {'Bridgerton':42966, 'Younger': 623, 'Emily in Paris': 41632, 'Sweet Magnolias':38894, 'This is Us': 17128, 'Jane the Virgin':128, 'The Bold Type': 15324, 'Virgin River':38893, 'Hart of Dixie': 301, 'Gilmore Girls':525}
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
    dramas_list1 = {'24':167, 'Breaking Bad':169, 'Dirty John':34649, 'Pieces of Her':40864,'CSI: Miami':576, 'Dead to Me':35846, 'Squid Game': 43687, 'Grey\'s Anatomy':67, 'How to Get Away with Murder':52, 'Scandal':98, 'American Crime Story': 2029}
    dramas1=show_info(dramas_list1)
    dramas_list2 = {'The Morning Show':41524, 'This is Us':17128,'Stay Close':48185,'Succession':23470, 'Inventing Anna':44818,'The Wire':179, 'One of Us is Lying':43878, 'Billions':3606, 'The Sopranos':527, 'The Newsroom':151}
    dramas2 = show_info(dramas_list2)
    dramas_list3 = {'Yellowstone':2848, 'The Dropout':41736,'The Path':6392, 'The Fosters':198, 'Mad Men':385, 'The Handmaid\'s Tale':16579, 'Ozark':13417, 'Suits':172, 'Psych':517}
    dramas3 = show_info(dramas_list3)
    dramas_list4= {'The OC':776, 'Manifest':31365,'StartUp':12323,'Good Girls':23542,'Orange is the New Black':170, 'Mare of Easttown':40546, 'Animal Kingdom':9993, 'One Tree Hill':560, 'White Collar':323}
    dramas4 = show_info(dramas_list4)
    return render_template ('drama.html', dramas1=dramas1, dramas2=dramas2, dramas3=dramas3, dramas4=dramas4)

@app.route('/docuseries')
def docuseries():
    crime_docuseries={}
    crimes = show_info(crime_docuseries)
    food_docuseries = {}
    food = show_info(food_docuseries)
    travel_docuseries = {}
    travel=show_info(travel_docuseries)
    return render_template ('docuseries.html', crimes=crimes, food=food, travel=travel)

@app.route('/reality')
def reality_shows():
    print('reality jsdf')
    return render_template ('reality.html')

@app.route('/romance')
def romance():
    print('romance')
    return render_template ('romance.html')

@app.route('/supernatural')
def supernatural():
    print('suuuuupernatural')
    return render_template ('supernatural.html')

@app.route('/thriller')
def thriller():
    thrillers_series1 = {'WHAT / IF': 38271, 'Orphan Black': 61, 'Revenge': 9, 'Prison Break':541, 'Killing Eve':22904, 'StartUp':12323, 'Pieces of Her':40864, 'Squid Game':43687, 'Pretty Little Liars': 177}
    thrillers1 = show_info(thrillers_series1)
    thrillers_series2 = {'The Path':6392, 'House of Cards':175, 'Scorpion':44, 'Money Heist':27436, 'The Blacklist':69, 'Homeland': 7, 'You':26856, '13 Reasons Why': 7194, 'Dirty John':34649, 'Stay Close':48185}
    thrillers2 = show_info(thrillers_series2)
    return render_template ('thriller.html', thrillers1=thrillers1, thrillers2=thrillers2)