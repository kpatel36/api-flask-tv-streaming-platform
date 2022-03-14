import requests as r

sitcom_short_list = {'Arrested Development':321, 'Parks and Recreation':174, 'Brooklyn Nine-Nine':49, 'Friends':431, 'The Office':526, 'Young and Hungry':1745}
reality_show_short_list = {'Keeping Up with the Kardashians': 575, 'Love is Blind': 46167, 'The Bachelor': 914, 'Married at First Sight': 2709, '90 Day Fiance':3139}

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

