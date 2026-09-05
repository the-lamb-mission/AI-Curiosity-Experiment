# Research Question:
Do public LLM models show curiosity?

Hypothesis: LLM models has a high degree of curiosity.

<br/><br/> 
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
 
 
<br/><br/>
## Chapter 2 - Design (Cycle 1)

### Top Down Design Diagram:
![TD Diagram](gallery/Proposal%20-%20TD%20Diagram.png)
This diagram is shows a breakdown of what must be done to build the experiment. 

### Describing the Simulation
The simulation will be ran on a simulation board. The simulation will be round-based, which is simple to design, as it does not require a constant connection. Each round the entity can do one action, e.g. moving, or interacting with items and other entity on the board. **The goal for AI agents is to reach a certain item.**

### Simulation Board
I am using a grid system, as it is easily implemented with a 2D diagram. Also, grid allow calculations to be performed easily, e.g. calculating distances between entities, or checking collisions. These are functions possibly needed in the future.

Each grid will store a Grid object. This is implemented with OOP, where a class Grid is made.

#### Grid Class:
Attribute(s):
- Its position (x, y) on the grid system.
- Type, as grid may have different type, wall, water, land...
- List of entities it contains (the entities standing on it).
- List of items it contains (the items placed on it).

Function(s):
- A getter method for its position.
- A getter method and a setter method for the list of entities.
- A getter method and a setter method for the list of items.

Next, I will create an abstract class for entities, such that a contract between different entities is enforced. This also makes it easier for me to design the interaction between the grid system and the entities.

#### Entity Class:
Attribute(s):
- Its ID.
- Health.
- Its position (x, y) on the grid system.

Function(s):
- Movement - How it moves per round.
- Attack - How it attacks.
- FindDistance - Gets another Entity and find the distance between them.

There is two main type of distance calculation, Manhattan distance and Euclidean distance. Manhattan distance would be used as it suits more for grid system, where it is equivalent to number of grids needed to be traversed for two entities to meet.

### Display System
I am writing the display system in Python, as I am experienced in it. PyGame is a good library for the display system, as it can has built-in Sprite, which allows designing entities and grids easily.

#### Displaying Board:
The board is displayed in layers. All grids and entities will have their own sprite. Grids near the agents will be rendered.

Change to Grid Class' attribute (s):
+ Sprite Object - describes how the grid should be displayed.

Change to Grid Class' function (s):
+ render - render the grid onto the screen.

Change to Entity Class' attribute (s):
+ Sprite Object - describes how the entity should be displayed.

Change to Entity Class' function (s):
+ render - render the entity onto the screen.

#### Display Start Sequence:
1. Create a window.
2. Create a Canvas (PyGame Surface object).
3. Repeat rendering the grid system by:
4. Request all entities to finish their actions.
5. Update Grid System after all entities' actions.
6. Repeat until an end condition is satisfied (Either AI agent reached its goal or stopped by human moderator).

<br/><br/>
## Chapter 2.5 - Develop (Cycle 1)


<br/><br/>
## Chapter 3 - Design (Cycle 2)
<br/><br/>
## Chapter 4 - Data Result
<br/><br/>
## Chapter 5 - Data Analysis
<br/><br/>
## Chapter 6 - Conclusion
