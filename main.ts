let LFSL = 0
let LFSR = 0
basic.forever(function on_forever() {
    
    LFSL = maqueen.readPatrol(maqueen.Patrol.PatrolLeft)
    LFSR = maqueen.readPatrol(maqueen.Patrol.PatrolRight)
    if (LFSR == 1 && LFSL == 1) {
        maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, 60)
        maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, 60)
        basic.pause(100)
    } else if (false && false) {
        
    } else if (false && false) {
        maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, 0)
    } else {
        maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, 0)
    }
    
})
