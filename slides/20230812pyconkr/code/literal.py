match beer_style:  # "Pilsner" / "IPA" / "Ale"
   case "Pilsner":
       result = "First drink"
   case "IPA":
       result = "I like it"
   case "Hazy IPA":
       result = "Cloudy and cloudy"
   case _:
       result = "I like most beers"
