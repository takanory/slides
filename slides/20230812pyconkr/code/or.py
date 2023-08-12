match beer_style:  # "IPA" / "Session IPA"
    case "Pilsner":
        result = "First drink"
    case "IPA" | "Session IPA":
        result = "I like it"
    case "Hazy IPA":
        result = "Cloudy and cloudy"
    case _:
        result = "I like most beers"
