from pycsound import PyCsound
import random


cs = PyCsound()
cs.options = "-o dac"
cs.header = {"sr": 44100, "nchnls": 2, "0dbfs": 1}

cs.orc = """

instr 1
a1 = poscil(p4 * expseg:k(.001, .01, 1, p3 - .01, .001), p5)
outs(a1, a1)
endin

instr 2
a1 = poscil(p4 * expseg:k(.001, .01, 1, p3 - .01, .001), p5 + poscil(expseg:k(.001, .01, 1, p3 - .01, .001) * p4 * p5 + 10, p5 + 10))
outs(a1, a1)
endin

instr 3
a1 = poscil(p4 * expseg:k(.001, .01, 1, p3 - .01, .001), p5 + poscil(expseg:k(.001, .01, 1, p3 - .01, .001) * p4 * p5 + 10, p5 + 10))
outs(a1, a1)
endin


"""


atk1, dur1 = 0, 0
for i in range(10):
    atk1 += random.uniform(0, 3)
    dur1 = random.uniform(0, 5)
    score1 = cs.add_to_score(statement="i", params=[1, atk1, dur1, 0.5, 110*(i+1)])

atk2, dur2 = 0, 0
for j in range(15):
    atk2 += random.uniform(0, 6)
    dur2 = random.uniform(0, 1)
    score2 = cs.add_to_score(statement="i", params=[2, atk2, dur2, 0.5, 90*(j+1)])

atk3, dur3 = 0, 0
for x in range(7):
    atk3 += random.uniform(0, 12)
    dur3 = random.uniform(0, 3)
    score2 = cs.add_to_score(statement="i", params=[3, atk3, dur3, 0.5, 69*(x+1)])


cs.add_to_score(statement="f", params=[1, 0, 4096, 10, 1])
cs.add_to_score(statement="t", params=[0, 240])

numbers = [i for i in range(100)]
cs.create_data_table(table_number=2, data=numbers)

cs.compile()

cs.save_csound_file(mode="csd")
# cs.plot_performance()

# cs.run()