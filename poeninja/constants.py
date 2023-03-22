from utils import get_current_league

current_league = get_current_league()
links = [
    f"https://poe.ninja/api/data/currencyoverview?league={current_league}&type=Currency&language=en",
    f"https://poe.ninja/api/data/currencyoverview?league={current_league}&type=Fragment&language=en",
    f"https://poe.ninja/api/data/itemoverview?league={current_league}&type=DivinationCard&language=en",
    f"https://poe.ninja/api/data/itemoverview?league={current_league}&type=Artifact&language=en",
    f"https://poe.ninja/api/data/itemoverview?league={current_league}&type=Oil&language=en",
    f"https://poe.ninja/api/data/itemoverview?league={current_league}&type=Incubator&language=en",
    f"https://poe.ninja/api/data/itemoverview?league={current_league}&type=UniqueWeapon&language=en",
    f"https://poe.ninja/api/data/itemoverview?league={current_league}&type=UniqueArmour&language=en",
    f"https://poe.ninja/api/data/itemoverview?league={current_league}&type=UniqueAccessory&language=en",
    f"https://poe.ninja/api/data/itemoverview?league={current_league}&type=UniqueFlask&language=en",
    f"https://poe.ninja/api/data/itemoverview?league={current_league}&type=UniqueJewel&language=en",
    f"https://poe.ninja/api/data/itemoverview?league={current_league}&type=SkillGem&language=en",
    f"https://poe.ninja/api/data/itemoverview?league={current_league}&type=ClusterJewel&language=en",
    f"https://poe.ninja/api/data/itemoverview?league={current_league}&type=Map&language=en",
    f"https://poe.ninja/api/data/itemoverview?league={current_league}&type=BlightedMap&language=en",
    f"https://poe.ninja/api/data/itemoverview?league={current_league}&type=BlightRavagedMap&language=en",
    f"https://poe.ninja/api/data/itemoverview?league={current_league}&type=UniqueMap&language=en",
    f"https://poe.ninja/api/data/itemoverview?league={current_league}&type=DeliriumOrb&language=en",
    f"https://poe.ninja/api/data/itemoverview?league={current_league}&type=Invitation&language=en",
    f"https://poe.ninja/api/data/itemoverview?league={current_league}&type=Scarab&language=en",
    f"https://poe.ninja/api/data/itemoverview?league={current_league}&type=BaseType&language=en",
    f"https://poe.ninja/api/data/itemoverview?league={current_league}&type=Fossil&language=en",
    f"https://poe.ninja/api/data/itemoverview?league={current_league}&type=Resonator&language=en",
    f"https://poe.ninja/api/data/itemoverview?league={current_league}&type=Beast&language=en",
    f"https://poe.ninja/api/data/itemoverview?league={current_league}&type=Essence&language=en",
    f"https://poe.ninja/api/data/itemoverview?league={current_league}&type=Vial&language=en"
]
