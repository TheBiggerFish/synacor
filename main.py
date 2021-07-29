from machine import Machine

machine = Machine()
machine.load_program('challenge.bin')
machine.execute(0)