# Gomoku AI Project

## Overview
This repository contains a project on **Gomoku (Five in a Row)**, a strategic board game often used to explore Artificial Intelligence (AI) techniques.  
The project includes a playable version of Gomoku in Python, as well as documentation and analysis resources related to the game and its AI implementations.


## Files

### 1. `gomoku.py`
- Python implementation of the **Gomoku board game** on a 15×15 grid.  
- Implements basic rules of Gomoku, including victory conditions (five stones in a row horizontally, vertically, or diagonally).  
- Supports:
  - Human vs AI gameplay
  - Special rule **Long Pro variant**, which balances the advantage of the first player (Black).
  - Player input and text-based board display in the console.
- Includes placeholders for **Minimax and Alpha-Beta pruning** functions to extend the AI decision-making.

### 2. `gomoku_analysis.pdf`
- A research-based **analysis of Gomoku strategies and AI approaches**.  
- Key contents:
  - Game patterns (victories, attacks, threats)
  - Classical AI approaches (Minimax, Alpha-Beta pruning)
  - Advanced methods such as **Monte Carlo Tree Search** and **Deep Learning**
  - Discussion of "Wine", a strong AI Gomoku player from the Gomocup tournament
- This document serves as a **theoretical foundation** to better understand how to design and improve an AI player for Gomoku.

### 3. `IA-Affrontement_entre_IA.pdf`
- A **project assignment document (in French)** describing the rules, requirements, and objectives of implementing a Gomoku AI:
  - Game rules and Long Pro variant  
  - Requirements for the AI (must use **Minimax with Alpha-Beta pruning**)  
  - AI should be able to play against a human within a **5-second response time**  
  - Gameplay displayed in a text-based format  
  - Final evaluation based on the AI’s correct functionality and ability to play multiple games without errors  
- Also includes instructions for hosting and testing on **Google Colab**.

---

## Getting Started

### Requirements
Only Python 3.x needed.

### How to Play
1. Run the Python script:
   ```bash
   python gomoku.py
   ```
2. Choose your color:  
   - **B** for Black (goes first, forced to start at H7 in Long Pro variant)  
   - **W** for White
3. Enter moves in the format:  
   ```
   A0  (row A, column 0)
   H7  (row H, column 7)
   ```
4. The game ends when:
   - A player places **five stones in a row**
   - Or the board is full (draw).

---
## References
- [Gomoku analysis paper (arXiv)](http://arxiv.org/abs/2111.01016v1) – theoretical foundation for AI design.
- Assignment guidelines in `IA-Affrontement_entre_IA.pdf`.
