#!/usr/bin/env python3
import random
import os
import hashlib
from datetime import datetime

# Poem templates and components for variety
POEM_STYLES = [
    "haiku",
    "limerick", 
    "sonnet",
    "free_verse",
    "couplet"
]

THEMES = [
    "nature", "technology", "love", "time", "dreams",
    "ocean", "mountains", "stars", "city", "seasons",
    "code", "art", "music", "journey", "wisdom"
]

NATURE_WORDS = {
    "nouns": ["moon", "sun", "tree", "river", "mountain", "ocean", "star", "cloud", "rain", "snow", "flower", "bird", "wind", "leaf", "forest"],
    "verbs": ["flows", "shines", "dances", "whispers", "blooms", "soars", "drifts", "glows", "falls", "rises", "sings", "breathes", "grows", "moves", "rests"],
    "adjectives": ["gentle", "golden", "silver", "ancient", "eternal", "silent", "peaceful", "wild", "serene", "mystic", "luminous", "infinite", "tranquil", "vibrant", "sacred"]
}

TECH_WORDS = {
    "nouns": ["code", "algorithm", "data", "pixel", "byte", "circuit", "network", "signal", "memory", "processor", "binary", "function", "variable", "loop", "array"],
    "verbs": ["compiles", "processes", "iterates", "executes", "streams", "connects", "transmits", "calculates", "renders", "encodes", "decodes", "optimizes", "debugs", "deploys", "runs"],
    "adjectives": ["digital", "virtual", "binary", "recursive", "parallel", "quantum", "encrypted", "modular", "dynamic", "static", "async", "responsive", "scalable", "distributed", "atomic"]
}

def generate_seed():
    """Generate a unique seed based on current timestamp and random value"""
    timestamp = datetime.now().isoformat()
    random_val = random.random()
    seed_string = f"{timestamp}-{random_val}"
    return hashlib.md5(seed_string.encode()).hexdigest()[:8]

def generate_haiku(theme, seed):
    """Generate a haiku (5-7-5 syllable pattern)"""
    random.seed(seed)
    words = NATURE_WORDS if theme in ["nature", "seasons", "ocean", "mountains"] else TECH_WORDS
    
    lines = []
    # Line 1 (5 syllables)
    adj = random.choice(words["adjectives"])
    noun = random.choice(words["nouns"])
    lines.append(f"{adj.capitalize()} {noun}")
    
    # Line 2 (7 syllables)
    verb = random.choice(words["verbs"])
    adv = random.choice(["softly", "gently", "quickly", "slowly", "brightly"])
    prep = random.choice(["through the", "in the", "with the", "by the"])
    noun2 = random.choice(words["nouns"])
    lines.append(f"{verb} {adv} {prep} {noun2}")
    
    # Line 3 (5 syllables)
    noun3 = random.choice(words["nouns"])
    verb2 = random.choice(words["verbs"])
    lines.append(f"{noun3} {verb2} away")
    
    return "\n".join(lines)

def generate_limerick(theme, seed):
    """Generate a limerick (AABBA rhyme scheme)"""
    random.seed(seed)
    
    subjects = ["programmer", "developer", "artist", "dreamer", "wanderer", "explorer", "writer", "builder"]
    places = ["GitHub", "forest", "valley", "city", "cloud", "server", "garden", "mountain"]
    actions = ["coded", "wandered", "created", "discovered", "imagined", "designed", "explored", "built"]
    
    subject = random.choice(subjects)
    place = random.choice(places)
    action = random.choice(actions)
    
    lines = [
        f"There once was a {subject} from {place}",
        f"Who {action} at incredible pace",
        f"With skill and with grace",
        f"They conquered the space",
        f"And left quite a marvelous trace"
    ]
    
    return "\n".join(lines)

def generate_couplet(theme, seed):
    """Generate a rhyming couplet"""
    random.seed(seed)
    words = NATURE_WORDS if theme in ["nature", "seasons", "ocean", "mountains"] else TECH_WORDS
    
    rhyme_pairs = [
        ("night", "light"), ("day", "way"), ("code", "road"),
        ("dream", "stream"), ("heart", "start"), ("mind", "find"),
        ("time", "rhyme"), ("soul", "goal"), ("tree", "free")
    ]
    
    pair = random.choice(rhyme_pairs)
    verb1 = random.choice(words["verbs"])
    verb2 = random.choice(words["verbs"])
    adj = random.choice(words["adjectives"])
    
    lines = [
        f"The {adj} {random.choice(words['nouns'])} {verb1} through the {pair[0]}",
        f"While {random.choice(words['nouns'])} {verb2} toward the {pair[1]}"
    ]
    
    return "\n".join(lines)

def generate_free_verse(theme, seed):
    """Generate a free verse poem"""
    random.seed(seed)
    words = NATURE_WORDS if theme in ["nature", "seasons", "ocean", "mountains"] else TECH_WORDS
    
    num_lines = random.randint(4, 8)
    lines = []
    
    for i in range(num_lines):
        structure = random.choice([
            f"{random.choice(words['adjectives']).capitalize()} {random.choice(words['nouns'])}",
            f"{random.choice(words['verbs']).capitalize()} {random.choice(['like', 'as', 'with'])} {random.choice(words['nouns'])}",
            f"The {random.choice(words['nouns'])} {random.choice(words['verbs'])}",
            f"{random.choice(['In', 'Through', 'Beyond', 'Within'])} the {random.choice(words['adjectives'])} {random.choice(words['nouns'])}",
            f"{random.choice(words['nouns']).capitalize()}, {random.choice(words['nouns'])}, {random.choice(words['nouns'])}"
        ])
        lines.append(structure)
    
    return "\n".join(lines)

def generate_sonnet(theme, seed):
    """Generate a simplified sonnet (14 lines)"""
    random.seed(seed)
    words = NATURE_WORDS if theme in ["nature", "seasons", "ocean", "mountains"] else TECH_WORDS
    
    lines = []
    for i in range(14):
        if i % 2 == 0:
            line = f"The {random.choice(words['adjectives'])} {random.choice(words['nouns'])} {random.choice(words['verbs'])} {random.choice(['above', 'below', 'within', 'beyond'])}"
        else:
            line = f"While {random.choice(words['nouns'])} {random.choice(words['verbs'])} {random.choice(['softly', 'gently', 'boldly', 'freely'])}"
        lines.append(line)
    
    return "\n".join(lines)

def generate_poem():
    """Main function to generate a poem"""
    seed = generate_seed()
    random.seed(seed)
    
    style = random.choice(POEM_STYLES)
    theme = random.choice(THEMES)
    
    # Generate poem based on style
    if style == "haiku":
        poem_content = generate_haiku(theme, seed)
    elif style == "limerick":
        poem_content = generate_limerick(theme, seed)
    elif style == "couplet":
        poem_content = generate_couplet(theme, seed)
    elif style == "free_verse":
        poem_content = generate_free_verse(theme, seed)
    else:  # sonnet
        poem_content = generate_sonnet(theme, seed)
    
    # Create metadata
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")
    title_words = ["whisper", "echo", "dream", "song", "dance", "tale", "verse", "melody", "rhythm", "harmony"]
    title_adj = ["morning", "evening", "midnight", "dawn", "twilight", "golden", "silver", "crystal", "velvet", "cosmic"]
    
    title = f"{random.choice(title_adj).capitalize()} {random.choice(title_words).capitalize()}"
    
    # Format the complete poem file
    poem_file_content = f"""# {title}

*Generated on {timestamp}*  
*Style: {style.replace('_', ' ').title()}*  
*Theme: {theme.title()}*  
*Seed: {seed}*

---

{poem_content}

---

*This poem was automatically generated by GitHub Actions*
"""
    
    # Create poems directory if it doesn't exist
    os.makedirs("poems", exist_ok=True)
    
    # Save poem with timestamp-based filename
    filename_timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"poems/{filename_timestamp}_{title.lower().replace(' ', '_')}.md"
    
    with open(filename, "w") as f:
        f.write(poem_file_content)
    
    print(f"Generated poem: {title}")
    print(f"Saved to: {filename}")
    print(f"Seed: {seed}")

if __name__ == "__main__":
    generate_poem()