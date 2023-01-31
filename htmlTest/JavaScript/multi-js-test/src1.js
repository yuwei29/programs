var com = com || {}

window.onload = function(){
    var p2 = document.getElementById('2')
    com.init()
    p2.innerHTML = com.result
}

com.init = function(){
    play.start()
}