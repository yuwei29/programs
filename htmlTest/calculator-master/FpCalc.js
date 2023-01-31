/*
 * @Author: 杰者Jayther
 * @Date: 2021-11-18 17:30:03
 * @LastEditTime: 2021-11-22 08:16:50
 */

//为了修正浮点数运算出现的误差，特写此函数
function FpCalc(ope_stat, ...proc) { //ope_stat体现运算符是什么，1代表加减法，2代表乘法。
    let sum, m_calc, result
    let decl = 0, temp
    for (const num of proc) {
        temp = (("" + num).split("."))[1]?.length || 0
        decl = decl < temp ? temp : decl
    }
    let divide, left, right
    sumQk(ope_stat)()
    for (let num of proc) {
        divide = ("" + num).split(".")
        left = divide[0]; num < 0 ? (right = "-" + divide[1]) : (right = divide[1])
        m_calc()
    }
    return result()

    function sumQk(ope_stat) {  //sum变量的情况
        switch (ope_stat) {
            case 1: return function () { //适用于加减法
                sum = 0
                m_calc = () => { sum += parseInt(left) * 10 ** decl + (parseInt(right) || 0) * 10 ** (decl - (divide[1]?.length || 0)) }
                result = () => sum / (10 ** decl)
            }
            case 2: return function () { //适用于乘法
                sum = 1
                m_calc = () => { sum *= (parseInt(left) * 10 ** decl + (parseInt(right) || 0) * 10 ** (decl - (divide[1]?.length || 0))) }
                result = () => sum / (10 ** (decl * proc.length))
            }
        }
    }
}
