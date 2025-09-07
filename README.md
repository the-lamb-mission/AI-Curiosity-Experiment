# AI-Curiosity-Experiment

##AI Experiment project - Ian Lam, 6th Sep 2025

I am investigating the weakness of narrow AI. There are many weaknesses in current AI model, and I decided to investigate its ability to show human traits, specifically curiosity.

Curiosity is greatly linked to how human learns about the world. As AI reaches a limit to its improvement after overfitting, I can foresee how curiosity solves it. As AI agents actively approaches different scenarios, overfitting no longer applies to AI.
In this experiment, I will measure AI agents' performances within a boardgame that involves curiosity.

What game can measure curiosity?

A game that requires gathering information actively.

However, if the game's objective is to gather as the main goal, then AI agents will attempt to gather information. Hence, the game should have scouting data as an option which is not necessarily a condition to win and see if these agents decide to actively search for it.
I decide to give AI a boardgame, where all rules are hidden. They can only learn about it with their own actions. This is a single player boardgame to prevent each AI agent's performance being affected by other agents.


##The boardgame settings:
###Public Rules:

The game is on a board with 10 x 10 grid.

AI agent starts on the bottom-left of the board.

The win condition is to reach the top-right destination of the board.

Each AI agent can move to its adjacent grid (vertical and horizontal, but not diagonal) by one grid or ask a question about the rules (the game master will answer yes or no).

There are hidden rules.

AI agents must complete the game in 70 rounds.
###Hidden Rules:

The boxes are labelled 1 to 100, with 1 starting at bottom-left, counting from right to left on a row, then continues left to right on the above row.

If agent step on any odd prime number, the agent moves down by a row if possible.

If agent step on any multiple of 11, the destination moves to left by one if possible and broadcast to the agent.

If agent step on any 




