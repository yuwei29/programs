/*
 * @Author: 杰者Jayther
 * @Date: 2021-11-12 21:35:15
 * @LastEditTime: 2021-11-21 21:14:52
 */
let calc = document.querySelector(".calc");//整个计算器
let theme = document.querySelector(".theme");
let screen = document.querySelector(".screen");
let all_btn = calc.querySelectorAll("button");

let flag = true
let gStyle =
    `background: rgba(255, 255, 255, 0.10);
        backdrop-filter: blur(5px);
        border-top: 1.5px solid rgba(255, 255, 255, 0.44);
        border-left: 1.5px solid rgba(255, 255, 255, 0.44);`,
    cStyle =
        `background: linear-gradient(90deg, #7e7e7e, #b8b8b8);
        background-size: 40% 100%;
        animation: shine 3s linear infinite;
        box-shadow: 25px 25px 60px rgba(3, 3, 3, 0.50);`

theme.style.cssText = gStyle
theme.addEventListener("click", () => {
    if (flag) {
        theme.style.cssText = cStyle
        calc.style.cssText = gStyle
        all_btn.forEach(btn => btn.classList.add("affected"))
        screen.style.backgroundColor = "rgb(213 213 213 / 10%)"
        theme.innerHTML = "有色模式"
        flag = false
    }
    else {
        theme.style.cssText = gStyle
        calc.style.cssText = ""
        all_btn.forEach(btn => btn.classList.remove("affected"))
        screen.style.backgroundColor = "rgb(89, 91, 109)"
        theme.innerHTML = "空灵玻璃"
        flag = true
    }
})

