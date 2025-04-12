% Facts
public_transport(bus).
public_transport(train).
public_transport(airplane).
public_transport(ship).

private_transport(bicycle).
private_transport(motorcycle).
private_transport(car).

vehicle(bicycle).
vehicle(motorcycle).
vehicle(car).
vehicle(bus).
vehicle(train).
vehicle(airplane).
vehicle(ship).

motor_vehicle(motorcycle).
motor_vehicle(car).
motor_vehicle(bus).
motor_vehicle(train).
motor_vehicle(airplane).
motor_vehicle(ship).

% Properties
slow(bicycle).
slow(ship).

fast(car).
fast(bus).
fast(train).
fast(airplane).

very_fast(airplane).

eco_friendly(bicycle).
eco_friendly(train).

eco_hostile(car).
eco_hostile(motorcycle).
eco_hostile(ship).

has_petrol_engine(car).
has_petrol_engine(bus).
has_petrol_engine(airplane).

has_diesel_engine(ship).
has_electric_motor(train).

dangerous(car).
dangerous(motorcycle).

safe(X) :- public_transport(X).

% Rules to list answers
print_fast :-
    write('Fast transport means: '), nl,
    fast(X), write(X), nl, fail.
print_fast.

print_eco_friendly :-
    write('Eco-friendly transport means: '), nl,
    eco_friendly(X), write(X), nl, fail.
print_eco_friendly.

print_safe :-
    write('Safe transport means: '), nl,
    safe(X), write(X), nl, fail.
print_safe.

print_has_motor :-
    write('Transport means with a motor: '), nl,
    motor_vehicle(X), write(X), nl, fail.
print_has_motor.

print_airplane_speed :-
    write('Is airplane fast? Yes.'), nl,
    (very_fast(airplane) -> write('Airplane is very fast.'), nl ; true).

print_car_properties :-
    write('Properties of car:'), nl,
    (dangerous(car) -> write('- Dangerous'), nl ; true),
    (fast(car) -> write('- Fast'), nl ; true),
    (has_petrol_engine(car) -> write('- Has petrol engine'), nl ; true),
    (eco_hostile(car) -> write('- Eco-hostile'), nl ; true).

% Initialize all queries
:- initialization(main).
main :-
    print_fast,
    nl,
    print_eco_friendly,
    nl,
    print_safe,
    nl,
    print_has_motor,
    nl,
    print_airplane_speed,
    nl,
    print_car_properties.