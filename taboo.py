import random
import string

# Define the deck of cards
suits = ['H', 'D', 'C', 'S']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

# Taboo words from the provided content
taboo_words = [
    {"word": "Car", "taboo": ["driver", "ride", "transport", "fast", "travel"]},
    {"word": "Duck", "taboo": ["bird", "yellow", "chicken", "\"quack\"", "food"]},
    {"word": "Dragonfly", "taboo": ["Red", "Wings", "Insect", "Fly", "dragon"]},
    {"word": "Snowflake", "taboo": ["cold", "winter", "flower", "snow", "fall"]},
    {"word": "Hungry", "taboo": ["feeling", "eat", "food", "breakfast", "meal"]},
    {"word": "Pillow", "taboo": ["head", "sleep", "soft", "bed", "blanket"]},
    {"word": "Dance", "taboo": ["Shoes", "Romantic", "Music", "Sing", "Town Square"]},
    {"word": "Proud", "taboo": ["feeling", "Accomplish", "Great", "Boast", "Humble"]},
    {"word": "Blanket", "taboo": ["Warm", "Bed", "Pillow", "Soft", "Cold"]},
    {"word": "Snail", "taboo": ["Round", "Slow", "River", "Eat", "Animal"]},
    {"word": "Shanghai", "taboo": ["Modern", "Big", "China", "Expo", "Famous"]},
    {"word": "Soccer", "taboo": ["Ball", "world Cup", "Black", "Sport", "Team"]},
    {"word": "Cheese", "taboo": ["Yellow", "White", "Pizza", "Food", "Italy"]},
    {"word": "Dinosaur", "taboo": ["Big", "Animal", "Extinct", "Long Ago", "Reptile"]},
    {"word": "Japan", "taboo": ["Country", "Asia", "Cherry Blossom", "Sushi", "Tokyo"]},
    {"word": "New York", "taboo": ["City", "America", "Big Apple", "Statue of", "Liberty"]},
    {"word": "Husband", "taboo": ["Wife", "Ring", "Marry", "Man", "Friend"]},
    {"word": "Giraffe", "taboo": ["Tall", "Africa", "Neck", "Long", "Yellow"]},
    {"word": "Michael Jackson", "taboo": ["Dance", "Thriller", "Strange", "Famous", "Singer"]},
    {"word": "Underwear", "taboo": ["Small", "Clothing", "Every Day", "Secret", "Under"]},
    {"word": "Girlfriend", "taboo": ["Boyfriend", "Beautiful", "Flowers", "Date", "Female"]},
    {"word": "Wok", "taboo": ["Cook", "China", "Iron", "Dishes", "Pot"]},
    {"word": "Camera", "taboo": ["Photos", "Pictures", "Snapshot", "Travel", "Memories"]},
    {"word": "Slippers", "taboo": ["Warm", "Feet", "Winter", "House", "Soft"]},
    {"word": "Comb", "taboo": ["Brush", "Hair", "Smooth", "Small", "Beautiful"]},
    {"word": "Glasses", "taboo": ["Eyes", "See", "Contacts", "Wear", "Face"]},
    {"word": "Hamburger", "taboo": ["America", "Beef", "Bread", "McDonalds", "Unhealthy"]},
    {"word": "Polar Bear", "taboo": ["cold", "Winter", "Alaska", "White", "Snow"]},
    {"word": "Penguin", "taboo": ["Bird", "Fly", "Animal", "Black", "White"]},
    {"word": "Popcorn", "taboo": ["Kernel", "Butter", "Sweet", "Microwave", "Snack Food"]},
    {"word": "Speech", "taboo": ["Give", "Speak", "Important", "Audience", "Nervous"]},
    {"word": "Furious", "taboo": ["Angry", "Red Face", "Hurt", "Rage", "Violent"]},
    {"word": "Jealousy", "taboo": ["Envy", "Emotion", "Compare", "Green", "Achieve"]},
    {"word": "Bench", "taboo": ["Sit", "Wooden", "Chair", "Long", "Park"]},
    {"word": "Chicken Leg", "taboo": ["Bird", "Body", "Eat", "Food", "KFC"]},
    {"word": "Toilet", "taboo": ["Washroom", "WC", "Pee", "Poop", "Bathroom"]},
    {"word": "Wish", "taboo": ["Want", "Desire", "Hope", "Dream", "Long For"]},
    {"word": "Exercise", "taboo": ["Run", "Sports", "Healthy", "Daily", "Morning"]},
    {"word": "Crown", "taboo": ["Head", "Gold", "King", "Queen", "Jewels"]},
    {"word": "Princess", "taboo": ["Prince", "Queen", "Daughter", "Royal", "Castle"]},
    {"word": "Internet", "taboo": ["Computer", "Web", "Surf", "Net", "Technology"]},
    {"word": "Ice Cream", "taboo": ["Cold", "Summer", "Sweet", "Snack", "Cone"]},
    {"word": "Jacket", "taboo": ["Coat", "Warm", "Clothes", "Sleeves", "Zipper"]},
    {"word": "Shower", "taboo": ["Rain", "Clean", "Water", "Every Day", "Bath"]},
    {"word": "Wind", "taboo": ["Blow", "Autumn", "Invisible", "Trees", "Kite"]},
    {"word": "Foreigner", "taboo": ["Teacher", "Different", "Outside", "Country", "Travel"]},
    {"word": "Church", "taboo": ["Sing", "Building", "Cross", "God", "Speaker"]},
    {"word": "Police", "taboo": ["Uniform", "Safety", "Peace", "Protect", "Siren"]},
    {"word": "Boots", "taboo": ["Winter", "Shoes", "Warm", "Fashion", "Snow"]},
    {"word": "Soy Sauce", "taboo": ["Chinese", "Liquid", "Brown", "Cooking", "Salty"]},
    {"word": "plane ticket", "taboo": ["Expensive", "Flight", "Travel", "Paper", "Seat"]}
]


def generate_random_word_set():
    """Generate a random word set when we run out of predefined ones."""
    word = ''.join(random.choices(string.ascii_uppercase, k=5))
    taboo = [''.join(random.choices(string.ascii_uppercase, k=4)) for _ in range(5)]
    return {"word": word, "taboo": taboo}

# Create a dictionary to store card-word mappings
card_word_map = {}

# Assign taboo words to cards
cards = [f"{rank}{suit}" for suit in suits for rank in ranks]
random.shuffle(cards)

for card in cards:
    if taboo_words:
        card_word_map[card] = taboo_words.pop(0)
    else:
        card_word_map[card] = generate_random_word_set()

def get_taboo_word(card):
    if card in card_word_map:
        word_set = card_word_map[card]
        return f"Word: {word_set['word']}\nTaboo words: {', '.join(word_set['taboo'])}"
    else:
        return "Card not found."

# Main game loop
while True:
    user_input = input("Enter a card (e.g., 4H) or 'quit' to exit: ").upper()
    if user_input == 'QUIT':
        break
    print(get_taboo_word(user_input))

print("Thanks for playing!")