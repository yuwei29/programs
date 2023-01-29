import * as t2 from './t2.mjs'
export const f1 = x=>x+11
const f2=x=>x+12
export const f3 = x=>f2(x)+t2.f1(x)