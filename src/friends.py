
def get_name(person):
	return person["name"]
	
def get_favourite_tv_show(person):
	return person["favourites"]["tv_show"]
	
def likes_to_eat(person, food):
	return True if food in person["favourites"]["snacks"] else False

def add_friend(person, friend):
	person["friends"].append(person)
	
def remove_friend(person, friend):
	person["friends"].remove(person)
	
def total_money(people):
	return sum([x["monies"] for x in people])
	
def lend_money(p1, p2, amount):
	if p1["monies"] >= amount:
		p1["monies"] -= amount
		p2["monies"] += amount

def all_favourite_foods(people):
#	allfavs = []
#	for person in people:
#		allfavs.extend(person["favourites"]["snacks"])
#	return allfavs
	return [snacks for p in people for snacks in p["favourites"]["snacks"]]	

def find_no_friends(people):
	return [p for p in people if len(p["friends"]) == 0]

def unique_favourite_tv_shows(people):
	allshows = []
	for person in people:
		show = person["favourites"]["tv_show"]
		if show not in allshows:
			allshows.append(show)
	return allshows

def unique_favourite_tv_shows_set(people):
	allshows = set()
	for person in people:
		allshows.add(person["favourites"]["tv_show"])
	return allshows	
