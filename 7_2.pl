% Initial state
state(robot(at_door, on_floor), ramp(at_window), stopcock(open)).

% Goal state (FIXED)
goal_state(state(robot(in_corner, on_ramp), ramp(in_corner), stopcock(closed))).

% Actions
action(
    state(robot(at_door, on_floor), ramp(at_window), stopcock(open)),
    walk_to_window,
    state(robot(at_window, on_floor), ramp(at_window), stopcock(open))
).

action(
    state(robot(at_window, on_floor), ramp(at_window), stopcock(open)),
    push_ramp_to_corner,
    state(robot(at_window, on_floor), ramp(in_corner), stopcock(open))
).

action(
    state(robot(at_window, on_floor), ramp(in_corner), stopcock(open)),
    walk_to_corner,
    state(robot(in_corner, on_floor), ramp(in_corner), stopcock(open))
).

action(
    state(robot(in_corner, on_floor), ramp(in_corner), stopcock(open)),
    step_on_ramp,
    state(robot(in_corner, on_ramp), ramp(in_corner), stopcock(open))
).

action(
    state(robot(in_corner, on_ramp), ramp(in_corner), stopcock(open)),
    shut_stopcock,
    state(robot(in_corner, on_ramp), ramp(in_corner), stopcock(closed))
).

% Plan execution
run :-
    Initial = state(robot(at_door, on_floor), ramp(at_window), stopcock(open)),
    step(Initial).

step(State) :-
    goal_state(State),
    write('Goal reached!'), nl.

step(State) :-
    action(State, Action, Next),
    write('Action: '), write(Action), nl,
    step(Next).

% Start automatically in online compiler
:- initialization(run).