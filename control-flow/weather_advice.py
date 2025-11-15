weather = ['sunny', 'rainy', 'cold']
weather_today = input("What's the weather like today? (sunny/rainy/cold): ")

if weather_today == weather[0]:
    print("Wear a t-shirt and sunglasses.")
elif weather_today == weather[1]:
    print("Don't forget your umbrella and a raincoat.")
elif weather_today == weather[2]:
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")