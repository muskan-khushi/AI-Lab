% Define available colors
color(red).
color(green).
color(blue).
color(yellow).

% Define different relationship (no two countries can have the same color)
different(X, Y) :- X \= Y.

% Define adjacency between countries
adjacent(A, B).
adjacent(A, D).
adjacent(A, E).
adjacent(B, C).
adjacent(B, D).
adjacent(B, E).
adjacent(C, D).
adjacent(C, E).
adjacent(D, E).

% Define map coloring condition
map(A, B, C, D, E) :-
    color(A), color(B), color(C), color(D), color(E),
    different(A, B),
    different(A, D),
    different(A, E),
    different(B, C),
    different(B, D),
    different(B, E),
    different(C, D),
    different(C, E),
    different(D, E).

% Predicate to output a solution
output_solution(A, B, C, D, E) :-
    format('A: ~w, B: ~w, C: ~w, D: ~w, E: ~w~n', [A, B, C, D, E]).

% Main predicate to find and output all solutions without numbering
find_solutions :-
    map(A, B, C, D, E),
    output_solution(A, B, C, D, E),
    fail.  % Force backtracking to find all solutions

% Initialization goal to run the map coloring without solution numbering
:- initialization(find_solutions).