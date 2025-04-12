% ------------------------
% Facts: Basic Entities
% ------------------------

% Furniture items present in the room
furniture(desk).
furniture(chair).
furniture(bed).
furniture(bookshelf).
furniture(wardrobe).

% Door and windows in the room
door(door).
window(window1).
window(window2).

% Walls of the room
wall(wall1).
wall(wall2).
wall(wall3).
wall(wall4).

% Corners of the room
corner(corner1).
corner(corner2).
corner(corner3).
corner(corner4).

% ------------------------
% Facts: Object Locations
% ------------------------

% Location of each furniture item
location(desk, wall4).
location(chair, center).
location(bed, wall3).
location(bookshelf, wall2).
location(wardrobe, wall4).

% Location of windows and door
location(window1, wall3).
location(window2, wall4).
location(door, wall1).

% Example item located in a corner
location(lamp, corner1).

% ------------------------
% Rules: Queries
% ------------------------

% Retrieve all furniture items in the room
all_furniture(List) :- findall(X, furniture(X), List).

% Count the number of windows in the room
count_windows(Count) :- findall(X, window(X), List), length(List, Count).

% Count the number of doors in the room
count_doors(Count) :- findall(X, door(X), List), length(List, Count).

% Count the number of furniture items
count_furniture(Count) :- findall(X, furniture(X), List), length(List, Count).

% Get the location of a specific item
where_is(Item, Place) :- location(Item, Place).

% Determine what is to the left of an item (example logic)
left_of(Item, Other) :- location(Item, wall4), location(Other, wall1).

% Determine what is to the right of an item (example logic)
right_of(Item, Other) :- location(Item, wall4), location(Other, wall2).

% List all items located on a specific wall
at_wall(Wall, Items) :- findall(X, location(X, Wall), Items).

% Determine on which wall a window is located
at_window(Window, Wall) :- location(Window, Wall), window(Window).

% Determine what item is located at a specific corner
at_corner(Corner, Item) :- location(Item, Corner), corner(Corner).

% ------------------------
% Initialization: Auto Execution
% ------------------------

% This predicate runs when the program is loaded
:- initialization(main).

main :-
    % Print all furniture items
    all_furniture(FList),
    write('Furniture: '), write(FList), nl,

    % Print number of windows, doors, and furniture
    count_windows(WCount),
    count_doors(DCount),
    count_furniture(FCount),
    write('Number of Windows: '), write(WCount), nl,
    write('Number of Doors: '), write(DCount), nl,
    write('Number of Furniture: '), write(FCount), nl,

    % Display location of the chair
    where_is(chair, P),
    write('Chair is at: '), write(P), nl,

    % Display what's to the left and right of the desk (if available)
    (left_of(desk, L) -> write('Left of desk is: '), write(L), nl ; write('No item to the left of desk'), nl),
    (right_of(desk, R) -> write('Right of desk is: '), write(R), nl ; write('No item to the right of desk'), nl),

    % Display what is at wall2
    at_wall(wall2, WallItems),
    write('At wall2: '), write(WallItems), nl,

    % Display which wall window1 is on
    at_window(window1, W),
    write('Window1 is at wall: '), write(W), nl,

    % Display what is at corner1
    at_corner(corner1, CItem),
    write('At corner1: '), write(CItem), nl.