"""A Christmas Carol for the Grade 7 Reader: VenvLearning's introduction, then Dickens's complete text (christmas_carol.txt),
split into the sections the Grade 7 ELA lessons read in Units 1–2. Each section opens with Words to Know."""
import os

HERE = os.path.dirname(os.path.abspath(__file__))

INTRO = {
    "title": "Introduction",
    "words": [("Victorian", "Belonging to the reign of Queen Victoria (1837–1901)."), ("workhouse", "A grim public building where very poor people lived and worked in exchange for food and a bed."),
              ("debtors' prison", "A prison for people who could not pay what they owed."), ("stave", "A verse of a song; Dickens calls each chapter of his “carol” a stave.")],
    "paras": [
        "In the autumn of 1843, Charles Dickens was thirty-one years old, famous, and worried about money. His newest novel was selling poorly, and he had a growing family to support. He was also angry. That year he had read a government report about children working long hours in mines and factories, and he had visited a “ragged school,” a free school for the poorest children of London. He wanted to strike a blow for them. He decided not to write a pamphlet but a story, and he wrote it in about six weeks.",
        "The story was <i>A Christmas Carol</i>. It went on sale on December 19, 1843, and the first six thousand copies sold out by Christmas Eve. It has never been out of print since.",
        "Dickens knew poverty from the inside. When he was twelve, his father was sent to a debtors' prison, and young Charles was taken out of school to work ten-hour days in a factory, pasting labels onto pots of boot polish. He never forgot the shame and hunger of those months, and he never forgot that a child's whole future can depend on whether anyone cares what happens to him.",
        "Victorian London was the largest and richest city in the world, and also one of the poorest. Factories and trade made some people very wealthy, while many families lived crowded into single rooms, burning what coal they could afford. People who could not support themselves might be sent to a workhouse, where families were separated and the food was kept deliberately meager so that no one would want to stay. Many comfortable people believed that the poor had only themselves to blame.",
        "Ebenezer Scrooge believes exactly that. He is a rich, lonely, tight-fisted businessman who thinks that prisons and workhouses are all the help the poor deserve, and that Christmas is “humbug,” or nonsense. On Christmas Eve he is visited by the ghost of his dead business partner, Jacob Marley, and then by three Spirits, who show him his past, his present, and a possible future. The question of the story is whether a person like Scrooge can change.",
        "Dickens called his book a <i>carol</i>, a joyful song sung at Christmas, and he divided it into five <b>staves</b>, or verses, instead of chapters. He wrote it to be read aloud, and he later performed it on stage himself, playing every character. As you read, listen to the voices: Dickens's narrator talks to you directly, jokes, and exaggerates, and every character has a way of speaking all his or her own.",
        "This is the complete text of the story, as Dickens published it in 1843. Some words and customs are old-fashioned, so each section begins with Words to Know. Read slowly, read aloud when you can, and keep your lesson's question in mind.",
    ],
    "cast": [("Ebenezer Scrooge", "a rich, miserly London businessman"), ("Jacob Marley", "Scrooge's business partner, dead seven years"),
             ("Bob Cratchit", "Scrooge's clerk"), ("Mrs. Cratchit, Martha, Belinda, Peter, and Tiny Tim", "Bob's family"),
             ("Fred", "Scrooge's cheerful nephew"), ("Fan", "Scrooge's little sister, Fred's mother"), ("Mr. Fezziwig", "the kindly merchant Scrooge worked for as a young man"),
             ("Belle", "the young woman Scrooge once planned to marry"), ("The Ghost of Christmas Past", "a strange, glowing figure, both childlike and old"),
             ("The Ghost of Christmas Present", "a jolly giant robed in green"), ("The Ghost of Christmas Yet to Come", "a silent, hooded phantom")],
}

SECTIONS = [
    {"key": "stave-1a", "name": "Stave One (first section)", "stave": "STAVE ONE", "title": "Marley's Ghost",
     "words": [("covetous", "Greedy; eager to get more money or things."), ("solitary", "Alone; without companions."), ("humbug", "Nonsense; something false or foolish."),
               ("morose", "Gloomy and bad-tempered."), ("destitute", "Without money, food, or a home."), ("surplus", "Extra; more than is needed."),
               ("counting-house", "A merchant's office where accounts were kept.")]},
    {"key": "stave-1b", "name": "Stave One (second section)", "stave": "STAVE ONE, CONTINUED", "title": "Marley's Ghost",
     "words": [("apparition", "A ghost or ghostlike figure."), ("incredulous", "Unable or unwilling to believe something."), ("spectre", "A ghost (British spelling)."),
               ("fetter", "A chain or shackle for the ankles."), ("ponderous", "Very heavy and slow-moving."), ("penance", "Suffering accepted to make up for wrongdoing."),
               ("benevolence", "Kindness; the wish to do good for others.")]},
    {"key": "stave-2", "name": "Stave Two", "stave": "STAVE TWO", "title": "The First of the Three Spirits",
     "words": [("recollection", "A memory."), ("apprentice", "A young person learning a trade by working for a skilled master."), ("jovial", "Cheerful and friendly."),
               ("idol", "Something loved or worshipped too much."), ("dowerless", "Without a dowry, the money or property a bride once brought to a marriage."),
               ("relentless", "Never stopping or letting up."), ("melancholy", "Sad and thoughtful.")]},
    {"key": "stave-3a", "name": "Stave Three (first section)", "stave": "STAVE THREE", "title": "The Second of the Three Spirits",
     "words": [("poulterer", "A seller of chickens, geese, and turkeys."), ("threadbare", "Worn so thin the threads show."), ("brazier", "A metal stand that holds burning coals."),
               ("odious", "Hateful; disgusting."), ("pawn", "To leave something with a lender in exchange for a loan."), ("plump", "Pleasantly round and full.")]},
    {"key": "stave-3b", "name": "Stave Three (second section)", "stave": "STAVE THREE, CONTINUED", "title": "The Second of the Three Spirits",
     "words": [("forfeits", "A party game in which players pay small, silly penalties."), ("blind man's buff", "A game in which a blindfolded player tries to catch the others."),
               ("wretched", "Very unhappy or unfortunate."), ("meagre", "Small in amount; not enough (British spelling of meager)."), ("earnest", "Serious and sincere."),
               ("Ignorance and Want", "Lack of education and lack of food, money, and care, shown as two starving children.")]},
    {"key": "stave-4", "name": "Stave Four", "stave": "STAVE FOUR", "title": "The Last of the Spirits",
     "words": [("shrouded", "Wrapped or covered, as a body is wrapped for burial."), ("solemn", "Serious and grave."), ("spectral", "Ghostly."),
               ("obscure", "Hidden or hard to see."), ("plunder", "Stolen goods."), ("intercede", "To plead on someone else's behalf."), ("neglected", "Not cared for.")]},
    {"key": "stave-5", "name": "Stave Five", "stave": "STAVE FIVE", "title": "The End of It",
     "words": [("transported", "Overwhelmed with joy."), ("Hallo", "An old spelling of hello, often shouted."), ("gruel", "A thin, watery porridge."),
               ("earnest", "Serious and sincere."), ("idle", "Lazy; not working.")]},
]


def load():
    """Fill each section's paras from christmas_carol.txt."""
    cur = None
    by_key = {s["key"]: s for s in SECTIONS}
    for s in SECTIONS: s["paras"] = []
    for line in open(os.path.join(HERE, "christmas_carol.txt"), encoding="utf-8").read().split("\n")[3:]:
        if line.startswith("@@ "): cur = by_key[line[3:].strip()]; continue
        if line.strip() and cur: cur["paras"].append(line)
    return SECTIONS
