from automata.pda.dpda import DPDA

my_transitions = {
    '1-2': '/A',
    '1-3': '/B',
    '1-4': 'A/',
    '1-5': 'B/',
    '2-4': 'B/',
    '2-5': '/A',
    '2-6': 'A/',
    '3-4': '/B',
    '6-6': '/B'
}
stack_symbols = {'A', 'B', ''}


def translate_transitions(dict_to_trans, s_symbols) -> dict:
    created_dict = {}
    for key in dict_to_trans.keys():

        # Determine Add order
        if dict_to_trans[key][0] == '/':
            a = key[0]
            b = key[2]
            index = 1
        else:
            a = key[2]
            b = key[0]
            index = 0

        if key[0] != key[2]:
            # Add Transitions
            if f'q{a}' not in created_dict.keys():
                created_dict[f'q{a}'] = {}
            if f'q{b}' not in created_dict.keys():
                created_dict[f'q{b}'] = {}

            created_dict[f'q{a}'][b] = {}
            # Read: ε, Push: Symbol
            for symbol in s_symbols:
                created_dict[f'q{a}'][b][symbol] = (f'q{b}', (dict_to_trans[key][index], symbol))

            # Read: Symbol, Push: ε
            created_dict[f'q{b}'][a] = {f'{dict_to_trans[key][index]}': (f'q{a}', '')}

        else:
            # Add Transitions
            if f'q{a}' not in created_dict.keys():
                created_dict[f'q{a}'] = {}

            # Read: ε, Push: Symbol
            created_dict[f'q{a}']['('] = {}
            for symbol in s_symbols:
                created_dict[f'q{a}']['('][symbol] = (f'q{a}', (dict_to_trans[key][index], symbol))

            # Read: Symbol, Push: ε
            created_dict[f'q{a}'][')'] = {f'{dict_to_trans[key][index]}': (f'q{a}', '')}
    return created_dict


maze = DPDA(
    states={'q1', 'q2', 'q3', 'q4', 'q5', 'q6'},
    input_symbols={'1', '2', '3', '4', '5', '6', '(', ')'},
    stack_symbols=stack_symbols,
    transitions=translate_transitions(my_transitions, stack_symbols),
    initial_state='q1',
    initial_stack_symbol='',
    final_states={'q2'},
    acceptance_mode='both'
)


def main() -> None:
    path = '34126(21524126(21524126(2152'
    print('Path Accepted') if maze.accepts_input(path) else print('Path Error')

    for maze_out in maze.read_input_stepwise(path):
        print(f'Input: {maze_out[1] :<{len(path)}}, State: {maze_out[0] :<3}, Stack: {maze_out[2][0][1::]}')
