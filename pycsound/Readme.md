## PyCsound  

A package to run Csound from python.

```python
cs = PyCsound()
cs.option = "-o dac"
cs.header = {"sr": 44100, "kr": 44100, "nchnls": 2, "0dbfs": 1}

cs.orc = """

instr 1
a1 = poscil(p4 * expseg:k(.001, .01, 1, p3 - .01, .001), p5)
outs(a1, a1)
endin

"""

atk, dur = 0, 0
for i in range(10):
    atk += random.uniform(0, 3)
    dur = random.uniform(0, 5)
    score = cs.add_score_statement(statement="i", params=[1, atk, dur, 0.5, 110 * (i + 1)])

cs.add_score_statement(statement="f", params=[1, 0, 4096, 10, 1])
cs.add_score_statement(statement="t", params=[0, 240])

cs.compile()
cs.run()

```

It is also possible to run csound file: .orc, .sco

```python

cs.orc = "path_to_file.orc"
cs.sco = "path_to_file.sco"

```

or

```python

cs.run("path_to_file.orc", "path_to_file.sco")

```

or


```python

cs.run("path_to_file.csd")

```

For save generated file:

```python

cs.save_csound_file(mode="csd", name="file_generated.csd", path="path_to_save_the_file_generated")

```


