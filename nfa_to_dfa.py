def accepting_states_contain(states, accepting_states):
    for state in states:
        if state in accepting_states:
            return True
    return False

# # q, s, a, m, n = map(int, input().split())
q = int(input("Enter the number of states: "))
s = int(input("Enter the number of alphabet symbols: "))
a = int(input("Enter the number of accepting states: "))
m = int(input("Enter the number of transitions: "))
n = int(input("Enter the number of strings to check: "))

# Read alphabet symbols
alphabet = input().split()

# Read starting state
start_state = int(input())

# Read accepting states
accepting_states = set(map(int, input().split()))

# Read transitions
nfa = {}
for _ in range(m):
    from_state, symbol, to_states = input().split()
    from_state = int(from_state)
    to_states = set(map(int, to_states.split(',')))
    transitions = nfa.setdefault(from_state, {})
    if symbol == '$':
        transitions.setdefault("epsilon", set()).update(to_states)
    else:
        transitions.setdefault(symbol, set()).update(to_states)

# Compute epsilon-closure of starting state
start_states = set()
queue = [start_state]
while queue:
    cur_state = queue.pop(0)
    start_states.add(cur_state)
    transitions = nfa.get(cur_state, {})
    epsilon_states = transitions.get("epsilon", set())
    for state in epsilon_states:
        if state not in start_states:
            queue.append(state)

# Convert NFA to DFA
dfa = {}
states_map = {frozenset(start_states): start_state}
queue = [frozenset(start_states)]
while queue:
    cur_states = queue.pop(0)
    for symbol in alphabet:
        next_states = set()
        for state in cur_states:
            transitions = nfa.get(state, {})
            to_states = transitions.get(symbol, set())
            epsilon_states = transitions.get("epsilon", set())
            for state in to_states:
                next_states.add(state)
            for state in epsilon_states:
                if state not in next_states:
                    next_states.add(state)
        if next_states:
            next_states = frozenset(next_states)
            transitions = dfa.setdefault(cur_states, {})
            transitions[symbol] = next_states
            if next_states not in dfa:
                new_state = max(states_map.values(), default=0) + 1
                states_map[next_states] = new_state
                queue.append(next_states)

# Output DFA
print("DFA transitions:")
for from_states, transitions in dfa.items():
    for symbol, to_states in transitions.items():
        from_state = states_map[from_states]
        to_state = states_map[to_states]
        print(f"{from_state} --{symbol}--> {to_state}", end='')
        if to_states & accepting_states:
            print(" (accepting)")
        else:
            print()

# Check strings
print("Checking strings:")
for i in range(n):
    string = input(f"Enter string #{i+1}: ")
    cur_states = frozenset(start_states)
    for symbol in string:
        if symbol not in alphabet:
            print(f"Error: symbol '{symbol}' not in alphabet")
            break
        next_states = dfa[cur_states].get(symbol, frozenset())
        if not next_states:
            print(f"Error: no transition for symbol '{symbol}' from state {cur_states}")
            break
        cur_states = next_states
    else:
        if cur_states & accepting_states:
            print("Yes")
        else:
            print("No")
