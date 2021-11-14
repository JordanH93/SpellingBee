Jordan Hennessy
R00109148

Pattern: Singleton Pattern
Location: app.server.connections.Connection
Reasoning:

I implemented this class as a singleton to ensure we don't have multiple instances manipulating data at
the same time causing data inconsistencies. If there were for example two instances of Connection then when we are
using multi-threading with multiple users we could have a scenario where we are trying to read and write the same value
at once which will lead to problems. The plan is to eventually use DB persistence in the future for this class which
can easily be refactored to include a db connection too.

Pattern: Factory Pattern
Location: app.server.spelling_bee_factory.ISpellingBee
Reasoning:

I implemented this class as a factory class to give the player the option to have different types of games. With the
factory pattern the types of games are only instantiated when the player chooses the game type. For now the difference
between games is that the length of the randomly chosen pangram. I plan to expand upon this in the next assignment with
adding score multipliers ect..