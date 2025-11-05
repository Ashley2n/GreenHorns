from models import Campaign

def campaigns_hc(db):
    campaign1 = Campaign(
        id = 1,
        name = "Italy",
        description = "The land of Italy",
        image_url = "blank",
        difficulty = 1,
        multiplier = 1
    )

    campaign2 = Campaign(
        id = 2,
        name = "Japan",
        description = "The land of Japan",
        image_url = "blank",
        difficulty = 2,
        multiplier = 1.25
    )

    campaign3 = Campaign(
        id = 3,
        name = "France",
        description = "The land of France",
        image_url = "blank",
        difficulty = 3,
        multiplier = 1.50
    )

    campaign4 = Campaign(
        id = 4,
        name = "Mexico",
        description = "The land of Mexico",
        image_url = "blank",
        difficulty = 4,
        multiplier = 1.75
    )

    db.session.add(campaign1)
    db.session.add(campaign2)
    db.session.add(campaign3)
    db.session.add(campaign4)
    db.session.commit()
    return ""