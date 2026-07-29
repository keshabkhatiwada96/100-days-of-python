# random quote generator

import random
quotes = [
    "The optimist thinks this is the best of all possible worlds. The pessimist fears it is true. — J. Robert Oppenheimer",
    "If the radiance of a thousand suns were to burst at once into the sky, that would be like the splendor of the mighty one. — J. Robert Oppenheimer",
    "Now I am become Death, the destroyer of worlds. — J. Robert Oppenheimer",
    "The deep things in science are not found because they are useful; they are found because it was possible to find them. — J. Robert Oppenheimer",
    "Failure is simply the opportunity to begin again, this time more intelligently. — Henry Ford",
    "Whether you think you can, or you think you can't—you're right. — Henry Ford",
    "Anyone who stops learning is old, whether at twenty or eighty. — Henry Ford",
    "Quality means doing it right when no one is looking. — Henry Ford",
    "The best way to predict the future is to invent it. — Alan Kay",
    "Talk is cheap. Show me the code. — Linus Torvalds",
    "Programs must be written for people to read, and only incidentally for machines to execute. — Harold Abelson",
    "Simplicity is the ultimate sophistication. — Leonardo da Vinci",
    "Measuring programming progress by lines of code is like measuring aircraft building progress by weight. — Bill Gates",
    "The computer was born to solve problems that did not exist before. — Bill Gates",
    "Two things are infinite: the universe and human stupidity; and I'm not sure about the universe. — Albert Einstein",
    "Science is a way of thinking much more than it is a body of knowledge. — Carl Sagan",
    "Somewhere, something incredible is waiting to be known. — Carl Sagan",
    "In politics, if you want anything said, ask a man; if you want anything done, ask a woman. — Margaret Thatcher",
    "The only thing we have to fear is fear itself. — Franklin D. Roosevelt",
    "If you want to test a man's character, give him power. — Abraham Lincoln"
    "END OF SOMETHING IS NOT END OF LIFE. - Keshab Khatiwada"
]
input("press ENTER to generate a random quote...")
quote = random.choice(quotes)
print("\nQuotes for Today:\n")
print(quote)