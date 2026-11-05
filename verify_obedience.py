"""Exact Bayesian obedience checks by enumeration of states and signal types.

Only the focal participant and one opponent need enumeration: congestion is
linear and expectation adds across N-1 opponents. No simulated data are used.
Run: python verify_obedience.py [output-directory]
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
import sys


def bern(bit, accuracy):
    return accuracy if bit else 1 - accuracy


def conditional_gains(a, b, r, p, d, L):
    """Return each labeled own-signal type's gain from A over its opposite."""
    mass = {s: F(0) for s in product((0, 1), repeat=2)}
    gain = mass.copy()
    for theta, hi, hj, ai, aj in product((0, 1), repeat=5):
        joint_a = (1-r)*bern(ai, b)*bern(aj, b)
        if ai == aj:
            joint_a += r*bern(ai, b)
        prob = F(1, 2)*bern(hi, a)*bern(hj, a)*joint_a
        # Correctness bits become actual opportunity labels.
        h, av = (theta if hi else 1-theta), (theta if ai else 1-theta)
        opp_h = theta if hj else 1-theta
        opp_a = theta if aj else 1-theta
        collision = (1-p)*int(av == opp_h) + p*int(av == opp_a)
        value_gain = d*(2*ai-1) - L*(2*collision-1)
        mass[h, av] += prob
        gain[h, av] += prob*value_gain
    return {s: gain[s]/mass[s] for s in mass}


def verify(a, b, r, p, d, L):
    qhh = a*a+(1-a)**2
    qha = a*b+(1-a)*(1-b)
    qaa = b*b+(1-b)**2+2*r*b*(1-b)
    alpha, beta = qha-qhh, qaa-2*qha+qhh
    D = d*(b-a)-L*(alpha+beta*p)
    GA = d*(2*b-1)-L*((1-p)*(2*qha-1)+p*(2*qaa-1))
    GH = d*(2*a-1)-L*((1-p)*(2*qhh-1)+p*(2*qha-1))
    assert GA-GH == 2*D
    values = conditional_gains(a, b, r, p, d, L)
    for (h, av), gain in values.items():
        expected = (GA+GH)/(2*qha) if h == av else D/(1-qha)
        assert gain == expected
        if D == 0:
            assert gain >= 0 if h == av else gain == 0
    if D == 0:
        assert GA == GH == 2*L*r*b*(1-b)*(2*a-1)*p/(b-a)
    return values


if __name__ == '__main__':
    cases = 0
    for a, b in [(F(3,5),F(4,5)), (F(2,3),F(5,6)), (F(11,20),F(9,10))]:
        for r, p in product([F(0),F(1,4),F(1,2),F(1)], [F(1,10),F(2,5),F(4,5)]):
            L = F(99,50)
            alpha = (b-a)*(2*a-1)
            beta = 2*(b-a)**2+2*r*b*(1-b)
            d = L*(alpha+beta*p)/(b-a)
            verify(a,b,r,p,d,L)
            cases += 1
    # The published calibration, independently evaluated by enumeration.
    values = verify(F(3,5),F(4,5),F(1),F(401,990),F(2),F(99,50))
    assert values[0,0] == values[1,1] == F(401,875)
    assert values[0,1] == values[1,0] == 0
    cases += 1
    # Off-equilibrium conditional identities test both strict deviation signs.
    for p in [F(0),F(1,5),F(3,5),F(1)]:
        verify(F(3,5),F(4,5),F(1),p,F(2),F(99,50))
    threshold = (F(2,5)/F(99,50)-F(1,25)-F(2,25))/F(8,25)
    assert threshold == F(203,792)
    result = dict(equilibrium_parameter_cases=cases,
                  equilibrium_signal_types=4*cases,
                  off_equilibrium_signal_types=16,
                  calibration_agreement_gain=str(values[0,0]),
                  calibration_disagreement_gain=str(values[0,1]),
                  commonality_threshold=str(threshold),
                  arithmetic='Python Fraction; exact state/signal enumeration')
    output = Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parent
    output.mkdir(parents=True, exist_ok=True)
    (output/'obedience_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
