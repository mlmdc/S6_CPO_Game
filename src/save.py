import json

import utils.cfg as cfg
import obj.card as card
import obj.stats as stats

# Save function
def save_game():

    data_to_save = {
        'compteur': cfg.compteur,
        'carte_actuelle': cfg.carte_actuelle.to_dict() if cfg.carte_actuelle else None,
        'stats_list': [stats.to_dict() for stats in cfg.stats],
    }

    with open('save_game.json', 'w') as file:
        json.dump(data_to_save, file)

# Load function
def load_game():
    try:
        with open('save_game.json', 'r') as file:
            loaded_data = json.load(file)

            # Load the card using the serialized data
            cfg.carte_actuelle = card.Card.from_dict(loaded_data['carte_actuelle']) if loaded_data['carte_actuelle'] else None

            # Load stats
            loaded_stats = loaded_data.get('stats_list', [])
            cfg.stats = [stats.Stats.from_dict(stats_data) for stats_data in loaded_stats]

            # Update other variables with loaded values
            cfg.compteur = loaded_data['compteur']
            # Update other variables as needed

            print("Game loaded successfully!")
    except FileNotFoundError:
        print("No saved game found.")
