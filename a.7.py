city= dict(zip(["tehran","esfahan","fars"],["tehran","esfahan","shiraz"]))
a= input("what is your city?")
Y= "{:} oscoli pas".format(city.get(a.capitalize(), "iran"))
print(Y)
