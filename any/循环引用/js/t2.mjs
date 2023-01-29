import * as t1 from './t1.mjs'

export const f1=x=>x+21
const f2 = x=>t1.f3(x)+22
export const f3=x=>f2(x)+23