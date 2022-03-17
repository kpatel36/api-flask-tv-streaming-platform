import requests as r

sitcom_short_list = {'Arrested Development':321, 'The Simpsons': 83, 'Parks and Recreation':174, 'Brooklyn Nine-Nine':49, 'Friends':431, 'Community':318, 'The Office':526, 'Young and Hungry':1745, 'It\'s Always Sunny in Philadelphia':347, 'The Standups':29821}
reality_show_short_list = {'Real Housewives of Beverly Hills':745, 'Keeping Up with the Kardashians': 575, 'Love is Blind': 46167, 'The Bachelor': 914, 'Married at First Sight': 2709, '90 Day Fiance':3139}
dramas_short_list = {'24':167, 'Breaking Bad':169, 'Dirty John':34649, 'Pieces of Her':40864,'CSI: Miami':576, 'Squid Game': 43687, 'Grey\'s Anatomy':67, 'How to Get Away with Murder':52, 'Scandal':98, 'American Crime Story': 2029}
supernatural_short_list = {'Game of Thrones': 82, 'The Flash':13, 'A Discovery of Witches': 31339, 'The Boys':15299, 'The Magicians': 3083, 'The Vampire Diaries':63, 'Stranger Things':2993, 'Shadowhunters':2158 , 'The Umbrella Academy': 30386, }
action_short_list = {'Blindspot': 1855, 'Vikings':29, 'Burn Notice': 667, 'Money Heist':27436, 'Arrow':4, 'The Flash':13, 'CSI: NY': 749, 'Chuck':168, 'Covert Affairs':345}
docuseries_short_list = {'Restaurants on the Edge':46285, 'Chef\'s Table':3252, 'Anthony Bourdain: Parts Unknown':255, 'Night on Earth': 46002, 'Attenborough: Life in Colour':53687, 'Our Planet':17868,'Formula 1: Drive to Success': 41074, 'My Next Guest': 34258, 'Making a Murderer':7989, 'Wild Wild Country': 35097, 'Explained':36901}
romance_short_list = {'Bridgerton':42966, 'Younger': 623, 'Emily in Paris': 41632, 'Sweet Magnolias':38894, 'This is Us': 17128, 'Jane the Virgin':128, 'The Bold Type': 15324, 'Virgin River':38893, 'Hart of Dixie': 301, 'Gilmore Girls':525}
dramas_list1 = {'24':167, 'Breaking Bad':169, 'Dirty John':34649, 'Pieces of Her':40864,'CSI: Miami':576, 'Dead to Me':35846, 'Squid Game': 43687, 'Grey\'s Anatomy':67, 'How to Get Away with Murder':52, 'Scandal':98, 'American Crime Story': 2029}
dramas_list2 = {'The Morning Show':41524, 'This is Us':17128,'Stay Close':48185,'Succession':23470, 'Inventing Anna':44818,'The Wire':179, 'One of Us is Lying':43878, 'Billions':3606, 'The Sopranos':527, 'The Newsroom':151}
dramas_list3 = {'Yellowstone':2848, 'The Dropout':41736,'The Path':6392, 'The Fosters':198, 'Mad Men':385, 'The Handmaid\'s Tale':16579, 'Ozark':13417, 'Suits':172, 'Psych':517}
dramas_list4= {'The OC':776, 'Manifest':31365,'StartUp':12323,'Good Girls':23542,'Orange is the New Black':170, 'Mare of Easttown':40546, 'Animal Kingdom':9993, 'One Tree Hill':560, 'White Collar':323}
medical_dramas = {}
fantasy_shows={}
sci_fi_shows={}
crime_docuseries={'Making a Murderer': 7989, 'Worst Roommate Ever': 60061,'Surviving R Kelly':40280, 'Don\t F With Cats':45322, 'The Jinx': 1542, 'Evil Genius':36280, 'Tiger King':46381, 'The Staircase':13645, 'The Keepers':27435}
food_docuseries = {'Chef\'s Table':3252, 'Restaurants on the Edge':46285, 'School of Chocolate': 58165, 'Taco Chronicles':43010, 'Anthony Bourdain: Parts Unknown':255, 'Salt Fat Acid Heat':38024, 'Stanley Tucci: Searching for Italy':53444}
travel_docuseries = {'Salt Fat Acid Heat':38024, 'Restaurants on the Edge':46285, 'Street Food: Latin America':49108, 'Stanley Tucci: Searching for Italy':53444}    
nature_docuseries = {'Night on Earth': 46002, 'Attenborough: Life in Colour':53687, 'Our Planet':17868}    
learning_docuseries={'Formula 1: Drive to Success': 41074, 'My Next Guest': 34258,  'Wild Wild Country': 35097, 'Explained':36901, 'The Mind, Explained': 43577 }
romance_shows={'Bridgerton':42966, 'Outlander':43, 'How I Met Your Mother':171, 'Younger': 623, 'The Bold Type':15324, 'Emily in Paris': 41632, 'The Fosters':198, 'Sweet Magnolias':38894, 'This is Us': 17128, 'Jane the Virgin':128, 'The Bold Type': 15324, 'Virgin River':38893, 'Hart of Dixie': 301, 'Gilmore Girls':525, 'Hart of Dixie':301, 'When Calls the Heart': 2091}
reality_romances ={'Love is Blind': 46167, 'The Bachelor': 914, 'Married at First Sight': 2709, '90 Day Fiance':3139}
reality_shows1={'Real Housewives of Beverly Hills':745, 'Real Housewives of New York City':750, 'Keeping Up with the Kardashians': 575, 'Love is Blind': 46167, 'The Bachelor': 914, 'Married at First Sight': 2709, '90 Day Fiance':3139, 'The Real Housewives of Orange County': 846, 'The Real Housewives of New Jersey':521, 'The Real Housewives of Atlanta':597}
reality_cooking_shows={'The Great British Baking Show':2950, 'Iron Chef':7459, 'Top Chef': 295, 'Cupcake Wars':529, 'Taste the Nation': 46600, 'Beat Bobby Flay':1145}
supernatural_shows = {'Game of Thrones': 82, 'The Flash':13, 'A Discovery of Witches': 31339, 'The Boys':15299, 'The Magicians': 3083, 'The Vampire Diaries':63, 'Stranger Things':2993, 'Shadowhunters':2158 , 'The Umbrella Academy': 30386}
thrillers_series1 = {'WHAT / IF': 38271, 'Orphan Black': 61, 'Revenge': 9, 'Prison Break':541, 'Killing Eve':22904, 'StartUp':12323, 'Pieces of Her':40864, 'Squid Game':43687, 'Pretty Little Liars': 177}
thrillers_series2 = {'The Path':6392, 'House of Cards':175, 'Scorpion':44, 'Money Heist':27436, 'The Blacklist':69, 'Homeland': 7, 'You':26856, '13 Reasons Why': 7194, 'Dirty John':34649, 'Stay Close':48185}

def show_info(show_dict):
    a1 = []
    for key in show_dict.keys():
        response = r.get(f'https://api.tvmaze.com/shows/{show_dict[key]}')
        if response.status_code == 200:
            show_name = response.json()
            a1.append([show_name['name'],', '.join(show_name['genres']), show_name['image']['medium'] ]) #, show_name['summary']
        else:
            print( response.status_code)
    return a1

