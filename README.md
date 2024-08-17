# NFA-to-DFA
**A Python script that converts a Non-deterministic Finite Automaton (NFA) to a Deterministic Finite Automaton (DFA) and checks string acceptance.**
Here’s a summarized and efficient version of your README for the "Introduction to the Theory of Computation" course project:

---

# Introduction to the Theory of Computation Project

## Overview

This project involves the conversion of a Non-deterministic Finite Automaton (NFA) to a Deterministic Finite Automaton (DFA) and checking string acceptance by the DFA. It demonstrates key concepts in automata theory including epsilon-closure and DFA state transitions.

## Functionality

1. **NFA to DFA Conversion**:
   - **Input**: Defines states, alphabet symbols, accepting states, transitions, and strings to be checked.
   - **Process**: Computes epsilon-closure, converts NFA transitions to DFA transitions, and maps NFA states to DFA states.
   - **Output**: Prints DFA transitions and whether each input string is accepted.

2. **String Acceptance**:
   - **Check**: Simulates the DFA to determine if given strings are accepted or rejected based on the DFA's transitions.

## Components

### Functions

- **accepting_states_contain(states, accepting_states)**: Checks if any state in `states` is an accepting state.

### Main Script

- **Input**:
  - Number of states, alphabet symbols, accepting states, transitions, and strings.
  - Reads alphabet, start state, accepting states, and transitions.
- **Epsilon-Closure**: Computes the epsilon-closure of the start state to handle epsilon transitions.
- **DFA Conversion**: Converts NFA to DFA using a breadth-first search approach.
- **Output**:
  - Displays DFA transitions.
  - Checks and reports acceptance for each input string.

### Example

1. **Input Data**:
   - States: `0, 1, 2`
   - Alphabet: `a, b`
   - Accepting State: `2`
   - Transitions: `0 --a--> 0, 1`; `1 --b--> 2`
   - Start State: `0`
2. **Execution**:
   - Converts the NFA to DFA.
   - Outputs DFA transitions.
   - Checks and reports string acceptance.

### Usage

1. **Run the Script**:
   - Execute the script in a Python environment.
   - Provide inputs as prompted (number of states, alphabet, transitions, etc.).

2. **Example Execution**:
   ```bash
   python nfa_to_dfa.py
   ```

3. **Input Format**:
   - Follow the prompts to input the number of states, symbols, accepting states, transitions, and strings.
