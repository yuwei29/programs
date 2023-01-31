/*
 * @Author: 杰者Jayther
 * @Date: 2021-08-20 07:06:18
 * @LastEditTime: 2021-11-22 08:26:16
 */
// JavaScript Document
window.onload = function () {
    let screen = document.querySelector(".screen")//计算器屏幕
    let keyboard = document.querySelector(".keyboard")//计算器键盘
    let keys = keyboard.querySelectorAll("button.num")//计算器键盘的数字键
    let ope = document.querySelectorAll(".ope")//计算器键盘的运算键
    let oswitch = document.getElementById("oswitch")//计算器的开关按钮

    /**********************描述计算器状态部分***************************/

    let on_off = false //计算器是否开启
    let result = "" //显示、计算结果
    let calcu = {
        num1: 0, num2: 0, //num1、num2用于储存进行运算的数值
        num_stat: 1, //表示将为哪个运算数赋值
        ope_stat: 0,//用的什么运算符
        xsdian: { is_on: false, length: 0 }, //包含用不用小数点、是小数点后几位的信息
        exec() { //计算函数
            switch (this.ope_stat) {
                case 1: result = FpCalc(1, this.num1, this.num2); break;
                case 2: result = FpCalc(1, this.num1, -this.num2); break;
                case 3: result = FpCalc(2, this.num1, this.num2); break;
                case 4: result = this.num1 / this.num2; break;
            }
            update()
            this.num1 = result
            this.num_stat = 2
            this.ope_stat = 0
            this.xsdian = { is_on: false, length: 0 };
        }
    }
    const update = () => screen.innerHTML = result == Infinity ? "Error" : result  //让显示屏显示或更新计算结果
    const renewXsd = () => calcu.xsdian = { is_on: false, length: 0 } //重置小数点对象状态
    const floatPro = (a, b, decl) => {  //专门处理输入操作数时失去精确度的问题的函数
        let sum = 0, proc = ("" + a).split(".")
        let left = proc[0], right = proc[1] || 0 //由于小数*10**n运算也会失去精度，所以小数部分要分开算
        right += "0".repeat(decl - right.length)
        sum = parseInt(left) * 10 ** decl + parseInt(right) + b //思想：转化为整数相加
        return sum / (10 ** decl)
    }

    /*******************开关键响应事件和计算器功能函数**********************/
    oswitch.addEventListener("click", (e) => {
        function fn1(e) { //针对数字按键
            let n
            switch (e.target.innerHTML) {
                case "1": n = 1; break;
                case "2": n = 2; break;
                case "3": n = 3; break;
                case "4": n = 4; break;
                case "5": n = 5; break;
                case "6": n = 6; break;
                case "7": n = 7; break;
                case "8": n = 8; break;
                case "9": n = 9; break;
                case "0": n = 0; break;
            }
            (calcu.xsdian.is_on) ?
                // result = result + n * 10 ** -(++calcu.xsdian.length) : result = result * 10 + n;
                result = floatPro(result, n, ++calcu.xsdian.length) : result = result * 10 + n;
            (calcu.num_stat == 1) ?
                calcu.num1 = result : calcu.num2 = result
            update()
        }
        function fn2(e) {
            switch (e.target.innerHTML) { //针对运算符按键
                case "+": calcu.ope_stat = 1; update(); result = 0; calcu.num_stat = 2; renewXsd(); break;
                case "-": calcu.ope_stat = 2; update(); result = 0; calcu.num_stat = 2; renewXsd(); break;
                case "×": calcu.ope_stat = 3; update(); result = 0; calcu.num_stat = 2; renewXsd(); break;
                case "÷": calcu.ope_stat = 4; update(); result = 0; calcu.num_stat = 2; renewXsd(); break;
                case "%":
                    result = result * 0.01;
                    (calcu.num_stat == 1) ?
                        calcu.num1 = result : calcu.num2 = result;
                    update(); break;
                case "√":
                    result = Math.sqrt(result);
                    (calcu.num_stat == 1) ?
                        calcu.num1 = result : calcu.num2 = result;
                    update(); break;
                case "=":
                    calcu.exec(); break;
                case "+/-":
                    result = -result;
                    (calcu.num_stat == 1) ?
                        calcu.num1 = result : calcu.num2 = result;
                    update(); break;
                case ".":
                    calcu.xsdian.is_on = true; break;
                case "C":
                    calcu.num1 = calcu.num2 = result = 0; update(); calcu.num_stat = 1; renewXsd(); break;
                case "Bksp":
                    calcu.xsdian.is_on ?
                        result = Number(result.toFixed(--calcu.xsdian.length)) : result = parseInt(result / 10);
                    (calcu.num_stat == 1) ?
                        calcu.num1 = result : calcu.num2 = result;
                    update(); break;
            }
        }
        if (!on_off) {
            // keys.forEach(numk => numk.addEventListener("click", fn1))
            keys.forEach(numk => numk.onclick = fn1)
            // ope.forEach(opek => opek.addEventListener("click", fn2))
            ope.forEach(opek => opek.onclick = fn2)
            result = 0
            update()
            on_off = true
        }
        else {
            // keys.forEach(numk => numk.removeEventListener("click", fn1))
            keys.forEach(numk => numk.onclick = () => { })
            // ope.forEach(opek => opek.removeEventListener("click", fn2))
            ope.forEach(opek => opek.onclick = () => { })
            result = ""
            update()
            calcu.num1 = calcu.num2 = 0  //此三行将计算器的状态还原
            calcu.num_stat = 1; calcu.ope_stat = 0
            renewXsd()
            on_off = false
        }
    })
}
