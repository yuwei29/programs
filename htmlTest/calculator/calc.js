window.onload = function () {
    let calc = document.getElementById('calc')
    let screen = document.querySelector('.screen')
    let result = '0'
    let tmp = 0
    let toCalc = false
    let opt = ''
    let update = ()=>screen.innerHTML = result == Infinity? 'Error' : result
    calc.addEventListener('click', (e) => {
        if(e.target.id==''){
            if(toCalc){
                if(result.length==0) result = e.target.innerHTML
                else result+=e.target.innerHTML
            }
            else if(result!='0'||e.target.innerHTML=='.') result+=e.target.innerHTML
            else result = e.target.innerHTML
            update()
        }
        switch(e.target.id){
            case 'toggle':
                result = -result
                update()
                break
            case 'daoshu':
                result = 1/result
                update()
                break
            case 'square':
                result = result*result
                update()
                break
            case 'sqrt':
                result = Math.sqrt(result)
                update()
                break
            case 'backspace':
                result = String(result)
                if(result.length<=1) result = '0'
                else result = result.slice(0,-1)
                update()
                break
            case 'clear':
                result = '0'
                update()
                break
            case 'divide':
            case 'times':
            case 'plus':
            case 'minus':
                tmp = Number(result)
                result = ''
                toCalc = true
                opt = e.target.id
                break
            case 'equals':
                result = Number(result)
                switch(opt){
                    case 'divide':
                        result = tmp/result
                        break
                    case 'times':
                        result = tmp*result
                        break
                    case 'plus':
                        result = tmp+result
                        break
                    case 'minus':
                        result = tmp-result
                        break
                }
                toCalc = false
                update()
                break
            
        }

    })
}