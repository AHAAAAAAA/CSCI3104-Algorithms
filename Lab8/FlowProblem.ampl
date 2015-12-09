# william mortl
# solution to flow problem in CSCI 3104 lecture

# requires glpsol and glpk
# to run: glpsol --math FlowProblem.ampl

# flow variables
var to;
var le;
var sp;
var ca;
var ol;

# objective
minimize objVal: 21*to + 17*le + 370*sp + 345*ca + 883*ol;

# initial flow limitations
c1:  0.85*to + 1.63*le + 12.79*sp + 8.38*ca         >= 15;
c2:  0.33*to + 0.20*le + 1.58*sp + 1.39*ca + 100*ol >=  2;
c3:  0.33*to + 0.20*le + 1.58*sp + 1.39*ca + 100*ol <= 6;
c4:  4.65*to + 2.37*le + 73.68*sp + 80.7*ca         >= 4;
c5:  9.00*to + 8.00*le + 7.00*sp + 506.4*ca         <= 100;
c6:  le + sp                                        <= to + ca + ol;
c7:  to                                             >= 0;
c8:  le                                             >= 0;
c9:  sp                                             >= 0;
c10: ca                                             >= 0;
c11: ol                                             >= 0;

# solve and show
solve;
display objVal, to, le, sp, ca, ol;
end;
