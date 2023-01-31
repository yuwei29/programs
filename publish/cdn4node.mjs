// const md=require("https://cdn.jsdelivr.net/remarkable/1.7.1/remarkable.min.js")
// import * as md from "https://cdn.jsdelivr.net/remarkable/1.7.1/remarkable.min.js"
import * as md from "./remarkable.min.js"
import * as https from 'https'
// https.get("https://quotes.toscrape.com/", function (error, response, body) {
//         if (!error && response.statusCode == 200) {
//                 var csv = body;
//                 console.log(csv);
//                 // Continue with your processing here.
//         }
// })
let str1 = 'sentence before modification'
console.log(str1);
console.log(Date.now()/1000);
https.get('https://quotes.toscrape.com/', (res) => {
        console.log('statusCode:', res.statusCode);
        console.log('headers:', res.headers);

        res.on('data', (d) => {
                str1 = d;
                console.log(Date.now()/1000);
        });

}).on('error', (e) => {
        console.error(e);
});
// const render = new md.Remarkable();
// const str1 = render.render('# tada!  \
//         [Link text Here](https://link-url-here.org)');
// console.log(str1);
console.log(str1);
console.log(Date.now()/1000);