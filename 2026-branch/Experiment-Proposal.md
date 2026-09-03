# Research Question:
Do public LLM models show curiosity?

Hypothesis: LLM models has a high degree of curiosity.

 
## Chapter 1 - Analysis

### Defining Curiosity
Curiosity is "an eager wish to know or learn about something" (Cambridge Dictionary, 2026). This means the motivation is not from to pursue a goal, but rather to make one's understanding complete, or to learn something unnecessary.

### Reflection on 2025's Attempt
In 2025, I attempted an experiment on AI's curiosity, but it is flawed. In that experiment, I made a maze with hidden rules that delays AI models' progress, where they can waste a turn to ask a question. 

However, this directly impact to their set goal (to escape the maze), which makes their motivations for asking question is not due to curiosity, but rather to achieve the goal.

We need to think of a way to separate the "question" (Measurement for curiosity) to its goal in a simulation. From here, I will name the **measurement for curiosity** as **side quest**, and the **goal in the simulation** as **main quest**.

### Essential Conditions
1. Side quest must be separated from the main quest.
2. Side quest does not influence the main quest's progress.
3. AI models should know the side quest is not important for the main quest.

### Software requirement
1. Python - To display and run the simulation.
2. Internet Access - To access AI models.

### Success Criteria
1. AI shows a clear understanding of the simulation's environment.
2. AI understands side quest is unnecessary for main quest.
3. AI understands its main quest.
4. AI understands side quest exists.
5. AI shows motivation for completing or ignoring side quest.

### Limitations
1. The experiment data is qualitative, as motivation for side quest cannot be measured with clear statistics.
   - This can possibly be overcome by using a test. This test would consist of questions regarding the side quest.
   - However, using a test may be biased to the questions. A qualitative measurement should still be considered to reduce bias.
2. Models may not understand the objective of the simulation clearly.
   - This could cause confusion for AI, causing it to act unpredictably. A clear instruction is required for the AI.
 
 
 
## Chapter 2 - Design and Develop (Cycle 1)

### Top Down Design Diagram:
![TD Diagram](gallery/Proposal%20-%20TD%20Diagram.png)
This diagram is shows a breakdown of what must be done to build the experiment. 

### Simulation Board
I am using a grid system, as it is easily implemented with a 2D diagram. Also, grid allow calculations to be performed easily, e.g. calculating distances between entities, or checking collisions. These are functions possibly needed in the future.

Each grid will store a Grid object. This is implemented with OOP, where a class Grid is made.
Attributes it should have:
- Its position (x, y) on the grid system.
- List of entities it contains (the entities standing on it).
- List of items it contains (the items placed on it).

Functions it should have:
- A getter method for its position.
- A getter method and a setter method for the list of entities.
- A getter method and a setter method for the list of items.



## Chapter 3 - Design and Develop (Cycle 1)

## Chapter 4 - Data Result

## Chapter 5 - Data Analysis

## Chapter 6 - Conclusion
