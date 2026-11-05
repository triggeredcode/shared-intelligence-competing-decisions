"""Synthetic shared-advice adoption study; no external observations or LLM calls.
Run with Python 3, numpy. Writes numerical results beside this script.
"""
from pathlib import Path
import json,csv,math,sys
import numpy as np
ROOT=Path(__file__).resolve().parent
OUT=Path(sys.argv[1]) if len(sys.argv)>1 else ROOT
OUT.mkdir(parents=True,exist_ok=True)
N=100;a=.6;b=.8;d=2.;v0=9.;lam=.02;L=lam*(N-1)
qhh=a*a+(1-a)**2;qha=a*b+(1-a)*(1-b)
alpha=qha-qhh;beta=1-2*qha+qhh;delta=d*(b-a)
pne=(delta/L-alpha)/beta
pso=max(0,min(1,(delta/L-2*alpha)/(2*beta)))
def theory(p):
 q=qhh+2*alpha*p+beta*p*p
 return v0+d*(a+p*(b-a))-L*q
def advantage(p): return delta-L*(alpha+beta*p)
# Independent markets are the units of Monte Carlo uncertainty.
rng=np.random.default_rng(20261105);R=50000
rows=[]
for label,p in [('baseline',0.),('social optimum',pso),('adoption equilibrium',pne),('full adoption',1.)]:
 vals=[];qs=[]
 for _ in range(R//1000):
  adopt=rng.random((1000,N))<p
  private=rng.random((1000,N))<a
  common=rng.random((1000,1))<b
  good=np.where(adopt,common,private)
  k=good.sum(axis=1)
  q=(k*(k-1)+(N-k)*(N-k-1))/(N*(N-1))
  vals.extend(v0+d*k/N-L*q);qs.extend(q)
 vals=np.asarray(vals)
 se=vals.std(ddof=1)/np.sqrt(R)
 row=dict(condition=label,p=float(p),exact=theory(p),mc=float(vals.mean()),se=float(se),q=float(np.mean(qs)))
 row['z_error']=(row['mc']-row['exact'])/se
 rows.append(row)
 assert abs(row['z_error'])<5
# Independent exact enumeration of all signal outcomes and policy assignments, N=4.
import itertools
max_enum_error=0.
for pp in [0.,.17,.5,1.]:
 total=0.
 for ad in itertools.product([0,1],repeat=4):
  pa=np.prod([pp if x else 1-pp for x in ad])
  for hh in itertools.product([0,1],repeat=4):
   ph=np.prod([a if x else 1-a for x in hh])
   for cc in [0,1]:
    pc=b if cc else 1-b
    choices=[cc if ad[i] else hh[i] for i in range(4)]
    pay=[v0+d*choices[i]-lam*sum(choices[i]==choices[j] for j in range(4) if i!=j) for i in range(4)]
    total+=pa*ph*pc*np.mean(pay)
 expected=v0+d*(a+pp*(b-a))-lam*3*(qhh+2*alpha*pp+beta*pp**2)
 max_enum_error=max(max_enum_error,abs(total-expected))
assert max_enum_error<1e-10
# Grid verifies theorem algebra, restrictions and equilibrium indifference.
checks=0
for aa in np.linspace(.51,.9,20):
 for bb in np.linspace(aa+.001,.999,20):
  ah=(bb-aa)*(2*aa-1); bh=1-2*(aa*bb+(1-aa)*(1-bb))+(aa*aa+(1-aa)**2)
  for ll in np.linspace(.1,8,30):
   dd=2*(bb-aa);pp=(dd/ll-ah)/bh
   if 0<pp<1:
    loss=dd*pp-ll*(2*ah*pp+bh*pp*pp)
    assert abs(loss+ll*ah*pp)<1e-10 and loss<0
    checks+=1
assert abs(advantage(pne))<1e-12
# Finite-agent pure adoption equilibria: m adopters.
pure=[]
for m in range(N+1):
 gain_non=delta-lam*((N-m-1)*alpha+m*(1-qha)) if m<N else -1
 gain_ad=delta-lam*((N-m)*alpha+(m-1)*(1-qha)) if m>0 else 1
 if gain_non<=1e-12 and gain_ad>=-1e-12:pure.append(m)
metrics=dict(N=N,a=a,b=b,d=d,v0=v0,lam=lam,L=L,alpha=alpha,beta=beta,pne=pne,pso=pso,loss_at_equilibrium=theory(pne)-theory(0),gain_at_optimum=theory(pso)-theory(0),pure_equilibria_adopter_counts=pure,enumeration_error=max_enum_error,grid_interior_cases=checks,markets_per_condition=R,seed=20261105,rows=rows)
(OUT/'results.json').write_text(json.dumps(metrics,indent=2))
with (OUT/'simulation_results.csv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
print(json.dumps(metrics,indent=2))
# Additional countercase and restricted-optimizer checks.
assert pure == [41]
assert abs((v0+d*b-L*(b*b+(1-b)**2))-9.2536)<1e-12
assert abs((v0+d-L)-9.02)<1e-12
planner_k=N/2+d/(4*lam)
planner_pay=v0+d*planner_k/N-lam*(planner_k*(planner_k-1)+(N-planner_k)*(N-planner_k-1))/N
assert abs(planner_pay-9.27)<1e-12
assert theory(pso)>=max(theory(float(p)) for p in np.linspace(0,1,10001))-1e-10
# Finite-population checks using exact rational arithmetic.
from fractions import Fraction as F
rational_cases=0
for nn in [4,10,100]:
 for aa,bb in [(F(3,5),F(4,5)),(F(2,3),F(5,6)),(F(11,20),F(9,10))]:
  qh=aa**2+(1-aa)**2; qx=aa*bb+(1-aa)*(1-bb)
  al=qx-qh; be=1-2*qx+qh
  for cc in [F(1,100),F(1,50),F(1,5),F(1,1)]:
   dd=2*(bb-aa)
   for m in range(nn+1):
    counts=(nn-m)*(nn-m-1)*qh+2*m*(nn-m)*qx+m*(m-1)
    direct=9+2*aa+dd*F(m,nn)-cc*counts/nn
    base=9+2*aa-cc*(nn-1)*qh
    compact=F(m,nn)*(dd-cc*(2*(nn-1)*al+(m-1)*be))
    assert direct-base==compact
    non=dd-cc*((nn-1)*al+m*be)
    ad=dd-cc*((nn-1)*al+(m-1)*be)
    eq=(m==nn or non<=0) and (m==0 or ad>=0)
    if eq and 0<m<nn and (nn-1)*al>be: assert compact<0
    rational_cases+=1

def fixed_pay(m):
 return v0+d*a+delta*m/N-lam/N*((N-m)*(N-m-1)*qhh+2*m*(N-m)*qha+m*(m-1))
opt_m=max(range(N+1),key=fixed_pay)
assert opt_m==16
for m in range(N+1):
 p=m/N
 assert abs(fixed_pay(m)-theory(p)-lam*beta*p*(1-p))<1e-12
finite=dict(pure_count=pure[0],pure_payoff=fixed_pay(pure[0]),best_fixed_count=opt_m,best_fixed_payoff=fixed_pay(opt_m),exact_rational_cases=rational_cases)
(OUT/'finite_results.json').write_text(json.dumps(finite,indent=2))
with (OUT/'curve.dat').open('w') as f:
 f.write('p change\n')
 for p in np.linspace(0,1,201): f.write(f'{p:.6f} {theory(p)-theory(0):.10f}\n')
with (OUT/'table_rows.tex').open('w') as f:
 labels=['Private only','Optimal independent adoption','Mixed adoption equilibrium','Full common adoption']
 for label,r in zip(labels,rows): f.write(f"{label} & {r['p']:.4f} & {r['exact']:.5f} & {r['mc']:.5f} & {r['se']:.6f} \\\\\n")
print(json.dumps(finite,indent=2))

# Wrap the generated rows in a complete table to avoid alignment-input hooks.
table_path=OUT/'table_rows.tex'
body=table_path.read_text()
table_path.write_text(r"\begin{tabular}{lrrrr}"+'\n'+r"\toprule"+'\n'+r"Regime & $p$ & Exact & Monte Carlo & Standard error\\"+'\n'+r"\midrule"+'\n'+body+r"\bottomrule"+'\n'+r"\end{tabular}"+'\n')
with (OUT/'commonality.dat').open('w') as f:
 f.write('r fixed endogenous pE\n')
 for rr in np.linspace(0,1,201):
  br=2*(b-a)**2+2*rr*b*(1-b)
  pe=float(np.clip((delta/L-alpha)/br,0,1))
  def wr(p):return delta*p-L*(2*alpha*p+br*p*p)
  f.write(f'{rr:.6f} {wr(pne):.10f} {wr(pe):.10f} {pe:.10f}\n')
