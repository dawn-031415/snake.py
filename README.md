# snakegame.py

A simple and easy-to-play Snake game built with Python and the `turtle` graphics library.

## Description
This is a classic Snake game where you control a snake to eat apples and grow longer. The game features:
- Smooth keyboard controls (W/A/S/D)
- Random apple generation
- Screen edge wrapping (pass through walls)
- Collision detection (game resets on self-bite)
- Built on a custom `gamebase` rendering module

## Features
- **Wall Pass-through**: Moving beyond the screen edge wraps the snake to the opposite side.
- **Growth Mechanism**: The snake grows longer each time it eats a red apple.
- **Auto Reset**: The game automatically resets after 2 seconds when the snake bites itself.

## Controls
Use the following keys to control the snake's direction:
- `w` - Move Up
- `s` - Move Down
- `a` - Move Left
- `d` - Move Right

## Requirements
- Python 3.x
- `turtle` (Built-in standard library)
- `gamebase.py` (Custom module required for the `square()` rendering function)

## How to Run
1. Ensure `snake.py` and `gamebase.py` are in the same directory.
2. Run the script:
