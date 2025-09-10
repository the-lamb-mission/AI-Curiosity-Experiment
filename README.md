# AI-Curiosity-Experiment

## AI Experiment project - Ian Lam, 6th Sep 2025

I am investigating the weakness of narrow AI. There are many weaknesses in current AI model, and I decided to investigate its ability to show human traits, specifically curiosity.

Curiosity is greatly linked to how human learns about the world. As AI reaches a limit to its improvement after overfitting, I can foresee how curiosity solves it. As AI agents actively approaches different scenarios, overfitting no longer applies to AI.
In this experiment, I will measure AI agents' (specifically referring to **LLMs Chatbot**) performances within a boardgame that involves curiosity.

What game can measure curiosity?

A game that requires gathering information actively.

However, if the game's objective is to gather as the main goal, then AI agents do not gathers information out of curiosity, but rather motivated by achieving the objective. Hence, the game should have scouting data as an option which is not necessarily a condition to win and see if these agents decide to actively search for it.
I decide to give AI a boardgame, where all rules are hidden. They can only learn about it with their own actions. This is a single player boardgame to prevent each AI agent's performance being affected by other agents.


## The boardgame settings:

### Public Rules:

1. The game is on a board with 10 x 10 grid.

2. AI agent starts on the bottom-left of the board.

3. The win condition is to reach the top-right destination of the board.

4. Each AI agent can move to its adjacent grid (vertical and horizontal, but not diagonal) by one grid or ask a question about the rules (the game master will answer yes or no).

5. There are hidden rules.

6. AI agents must complete the game in 70 rounds, or else the game ends.

7. The least rounds used, the better it is.

### Hidden Rules:

1. The hidden rules have different level of priorities, where they are done in the order they are ranked.

2. The boxes are labelled 0 to 99, with 0 starting at bottom-left, counting in ascending order from left to right on a row until its end, then move up to next row (also left to right).

3. If agent steps on any odd prime number, the agent moves down by a row if possible.

4. If agent steps on any multiple of 11, the destination moves to left by one if possible and broadcast to the agent.

5. If agent was initially placed on a multiple of 6, and if they attempt to move up, it will not be permitted and their round would be wasted.

6. If agent steps on any multiple of 4 (except 4), they will be moved to the last multiple of 4, for example, when they step on 32, they will move to 28.



## Method for Measuring Curiosity

In order to measure how curious the AI agents are, there are three observations to be made, the total rounds needed before each agent reaches the destination, 
the percentages of rounds used for questioning hidden rules, and a reflection from AI agents after the game of how much hidden rules they have found.

### Observation 1 - The Total Rounds Needed

This is a quantitative measurement to show how effective AI agents are at handling this boardgame. The quicker they are, the better the performances.

### Observation 2 - The Percentages of Questioning Rounds

This is a quantitative measurement that shows the degree of curiosity an agent is at. Higher percentages may indicate that the related AI models were designed with an adventurous trait embedded. By using such Observation 2 with Observation 1, we may investigate if the degree of curiosity has an impact to the performance in this scenario.

### Observation 3 - The Reflections

This is a qualitative assessment that shows how competent different AI agents are at collecting data. By using Observation 3 with Observation 1, we could conclude whether competence in data collection would impact the efficiency of AI agents reaching their destinations (similar to linking Observation 2 with Observation 1). Observation 3 can make a better judgement than observation 2 in some cases, such as when the AI agents have already fully grasped all hidden rules in a single question, then Observation 2 no longer correlates to the degree of curiosity an agent is at.

