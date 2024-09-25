class TuringMachine:
    def __init__(self, tape, transition_function, start_state, accept_state, reject_state):
        self.tape = list(tape)
        self.head = 0  # Tape head starts at the first position
        self.state = start_state
        self.transition_function = transition_function
        self.accept_state = accept_state
        self.reject_state = reject_state

    def step(self):
        if self.head >= len(self.tape):
            self.tape.append('_')

        symbol = self.tape[self.head]

        action = self.transition_function.get((self.state, symbol))

        if action:
            new_state, write_symbol, direction = action

            print(f"=> HEAD: {self.head}, STATE: {self.state}, SYMBOL: {symbol}")

            self.tape[self.head] = write_symbol

            self.state = new_state

            if direction == 'R':
                self.head += 1
            elif direction == 'L' and self.head > 0:
                print(f" -> Moving Left")
                self.head -= 1

            print(f"  ACTION : Head: {self.head}, State: {self.state}\n")
        else:
            self.state = self.reject_state

    def run(self):
        print(f"Tape: {''.join(self.tape).replace('_', '')}\n")
        while self.state != self.accept_state and self.state != self.reject_state:
            self.step()

        return self.state == self.accept_state


# Definisikan fungsi transisi sesuai dengan deskripsi
transition_function = {
    ('q0', '1'): ('q1', '1', 'R'), 
    ('q0', '0'): ('q2', '0', 'R'),  

    ('q1', '1'): ('q0', '1', 'R'), 
    ('q1', '0'): ('q3', '0', 'R'),

    ('q3', '1'): ('q2', '1', 'R'),
    ('q3', '0'): ('q1', '0', 'R'),

    ('q2', '1'): ('q3', '1', 'R'),  
    ('q2', '0'): ('q0', '0', 'R'), 

    # -- State akhir -- #a
    # di terima || q_accept
    ('q0', '_'): ('q_accept', '_', 'R'), 

    # di tolak || q_reject
    ('q1', '_'): ('q_reject', '_', 'R'), 
    ('q2', '_'): ('q_reject', '_', 'R'),  
    ('q3', '_'): ('q_reject', '_', 'R'), 
}

# -- Main Program -- #
print("=============================================")
print("||                                         ||")
print("||               MESIN TURING              ||")
print("||                                         ||")
print("=============================================")

# input tape
print("Masukkan tape yang ingin diuji:")
print("Contoh input tape: 10100")
valueInput = input() 
tape = valueInput + "_" 
start_state = 'q0'
accept_state = 'q_accept'
reject_state = 'q_reject'

tm = TuringMachine(tape, transition_function, start_state, accept_state, reject_state)

# Jalankan mesin
if tm.run():
    print(f"Jadi '{tape.replace('_', '')}' DITERIMA (jumlah 0 genap).")
else:
    print(f"Jadi '{tape.replace('_', '')}' DITOLAK (jumlah 0 ganjil).")