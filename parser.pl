:- ensure_loaded(pokemons).
:- ensure_loaded(moves).
:- ensure_loaded(types).

parse_name(Name, ParsedName) :-
    split_string(Name, "(|)", " ", Parts),
    length(Parts, 5),
    nth0(1, Parts, ParsedName),
    pokemon(ParsedName).

parse_name(Name, ParsedName) :-
    split_string(Name, "(|)", " ", Parts),
    length(Parts, 3),
    nth0(0, Parts, ParsedName),
    pokemon(ParsedName).

parse_name(Name, ParsedName) :-
    split_string(Name, "(|)", " ", Parts),
    length(Parts, 3),
    nth0(1, Parts, ParsedName),
    pokemon(ParsedName).

parse_name(Name, ParsedName) :-
    split_string(Name, "(|)", " ", Parts),
    length(Parts, 1),
    pokemon(Name),
    ParsedName = Name.

list_of_six_elements([_, _, _, _, _, _]).
list_of_four_elements([_, _, _, _]).

% Parse the entire team description
parse_team(TeamString, Output) :-
    % Split the team description by line breaks
    atomic_list_concat(PokemonAtomStrings, '\n\n', TeamString),
    maplist(atom_string, PokemonAtomStrings, RawPokemonStrings),
    % append(PokemonStrings, [_], RawPokemonStrings),
    list_of_six_elements(Output),
    parse_pokemons(RawPokemonStrings, Output).

array_contains_element_with_substring(InputList, Substring, Element) :-
    member(Element, InputList),
    sub_string(Element, _, _, _, Substring).

parse_pokemons([], []). % Base case: empty list, return empty list
parse_pokemons([PokemonString | RestPks], [ParsedPk | ParsedRest]) :-
    %atomic_list_concat(Lines, '\n', PokemonString),
    split_string(PokemonString, "\n", "", Lines),
    parse_name_and_item(Lines, Name, Item),
    %parse_ability_line(Lines, Ability),
    %parse_evs_line(Lines, EVs),
    %parse_ivs_line(Lines, IVs),
    parse_moves(Lines, Moves),
    list_of_four_elements(Moves),
    ParsedPk = pokemon_build(Name, Item, Moves), % , Ability, EVs, NatureStr, IVs
    parse_pokemons(RestPks, ParsedRest).

parse_moves([H|T], Result) :-
    (   string_chars(H, ['-'|RestChars])
    ->  Result = [Move|Rest],
        string_chars(MoveStr, RestChars),
        trim_spaces(MoveStr, Move),
        move(Move),
        parse_moves(T, Rest)
    ;   parse_moves(T, Result)
    ).
parse_moves([], []).

parse_evs_line(Lines, EVs) :-
    array_contains_element_with_substring(Lines, "EVs:", Line),
    split_string(Line, ":", " ", [_, EvsLine]),
    split_string(EvsLine, "/", " ", Parts),
    parse_evs_parts(Parts, EVs).

parse_evs_parts([], []).
parse_evs_parts([Part | Rest], [Stat-Value | EVs]) :-
    trim_spaces(Part, PartTrimmed),
    split_string(PartTrimmed, " ", "", [Value, StatStr]),
    atom_number(Value, ValueNumber),
    atom_string(Stat, StatStr),
    EVs = [Stat-ValueNumber | OtherEVs],
    parse_evs_parts(Rest, OtherEVs).

parse_ability_line(Lines, Ability) :-
    array_contains_element_with_substring(Lines, "Ability:", Line),
    split_string(Line, ":", "", [_, AbilityStr]),
    trim_spaces(AbilityStr, Ability). % ability(AbilityStr)

% Parse the first line (name, item)
parse_name_and_item(Lines, Pokemon, Item) :-
  	% Split by "@" (assuming no nickname before @)
    nth0(0, Lines, Line),
  	split_string(Line, "@", "both", [PokemonPart, ItemPart]),
  	atom_string(PokemonPart, PokemonStr),
    trim_spaces(PokemonStr, PokemonClean),
    parse_name(PokemonClean, Pokemon),
    atom_string(ItemPart, ItemStr),
    trim_spaces(ItemStr, Item). % item(Item).

trim_spaces(Input, Output) :-
    atom_string(Input, InputStr),   % Convert Input to a string if it's an atom
    normalize_space(atom(TrimmedAtom), InputStr), % Trim leading and trailing spaces
    atom_string(TrimmedAtom, Output).
