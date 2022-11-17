#https://www.codewars.com/users/724thomas2/completed_solutions

class Automaton(object):

    def __init__(self):
        self.states = ["q1","q2","q3"]

    def read_commands(self, commands):
        cur=self.states[0]
        for i in commands:
            if i=="1":
                if cur=="q1":
                    cur="q2"
                elif cur=="q3":
                    cur="q3"
            elif i=="0":
                if cur=="q2":
                    cur="q3"
                elif cur=="q3":
                    cur="q2"
        return cur=="q2"
        # Return True if we end in our accept state, False otherwise

my_automaton = Automaton()

# Do anything necessary to set up your automaton's states, q1, q2, and q3.