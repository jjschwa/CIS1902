---
layout: page
title: HW2 - Turtle and Pygame
nav_exclude: true
---

# HW2 - Turtle and Pygame
Due Date: 9:45am on Wednesday, February 25, 2026

As always you get a 24 hour grace period, and can use one late day on this assignment, allowing the last submission to be at 9:25am on Friday, February 27th. If you suspect you will need longer than this, you *must* inform staff prior to the original deadline on 2/25/2026

### Grading

**Note**: HW 2 is fully manually graded

There are 2 components/files. The possible scores on part 1 range from $[14, 16]$ and on part 2 $[20, 26]$. However the cap of points for this homework in total is 38 (out of a base score of 34) so we will be taking $min($your_score$, 38)$


## Part 0 - Downloading the Starter Files

Download the zip file with all necessary base files for both parts of this homework here:

[HW2.zip](../HWs/HW2.zip)

## Part 1 - Turtle Graphics Fractals

In this portion of the homework you will be getting some practice using the turtle graphics library as well as using recursion. 

For question #2, here is an example of what a tree could look like, but we will accept any structure that resembles a recursive tree (eg. more than 2 branches or vertical).

Tree Example
<iframe src="../HW2Tree.png" width="100%" height="600px" style="border: none;">
  This will not load. Please download the image to view it: <a href="../HW2Tree.png">Download image</a>.
</iframe>

### Rubric


## Part 2 - Pygame Mini-Game

For this portion of the homework, we’ve designed a (kinda ugly) base game with simple pieces: four walls, a background, a character you control, and food that spawns one at a time in random places. The mechanics of this game right now are even simpler: the character’s goal is to collect the food to rack up points. Points are displayed outside the walls within the game screen. Each food is worth the same amount of points and the game goes on forever. 

Your job is to design two creative mechanics that alter the way the game works. Some ideas in which you could alter the game include the way the main character interacts with other elements of the game, win/lose conditions, enemies, etc. You really can be as creative as you want. The goal of this homework is to get you familiar with Pygame mechanics as well as think like a game designer, so you should aim to challenge both your game mechanic design and your level of Pygame expertise. Feel free to edit the base game in whatever way you like. If you ever need to start over you can re-download the starter files.

<u>Examples of Acceptable Mechanics</u>

We've chosen to exclude giving any example mechanics because we want you to do the game design on your own. Should you feel stuck or unsure whether your idea will meet the requirements, please post on Ed!

### EXTRA CREDIT:

1. Make the game look pretty.

2. Add a third creative mechanic.

### Rubric


#### Core Game Mechanics (2 × 10 points = 20 points)

<u>Overview</u>

1. You must implement 2 core game mechanics.

2. Max points per mechanic: 10

3. Base total: 20 points

4. Extra Credit: up to 6 points

Maximum possible score: 26 out of 20 points

Each mechanic will be evaluated using the criteria below. Meeting one criteria will award you 10 points. The bare minimum requirement to earn full credit for this homework is to implement __2 different mechanics__.

| Criteria                                                                                    | Points |
| ------------------------------------------------------------------------------------------- | ------ |
| Changes the way the main character interacts with other elements                            | 10      |
| Adds a new character or interactive element that behaves differently from existing elements | 10      |
| Interaction changes based on game state (e.g., Pac-Man after eating a fruit)                | 10      |
| Provides visual feedback based on an event                                                  | 10      |
| Modifies scoring and/or introduces win/lose conditions                                      | 10      |
| **Max possible points over 2 mechanics**                                                                      | **20** |

| Extra Credit Option                           | Points |
| --------------------------------------------- | ------ |
| Game has polished visuals and/or sound design | +2     |
| Adds a third creative mechanic                | +2–4*  |


\* Third mechanic scoring depends on complexity and quality. Final determination is made by graders and may involve peer review.