
def get_name(person):
	return person["name"]
	
def get_favourite_tv_show(person):
	return person["favourites"]["tv_show"]
	
def likes_to_eat(person, food):
	return True if food in person["favourites"]["snacks"] else False


