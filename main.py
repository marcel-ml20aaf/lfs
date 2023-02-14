LFSL = 0
LFSR = 0

def on_forever():
    global LFSL, LFSR
    LFSL = maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT)
    LFSR = maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT)
    if LFSR == 1 and LFSL == 1:
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 60)
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 60)
        basic.pause(100)
    elif False and False:
        pass
    elif False and False:
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 0)
    else:
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 0)
basic.forever(on_forever)
