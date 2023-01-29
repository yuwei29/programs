
extern crate itchy;

fn main(){
let stream = itchy::MessageStream::from_file("D:/personal/programs/any/nasdaq数据分析/12302019.NASDAQ_ITCH50").unwrap();
for msg in stream {
    println!("{:?}", msg.unwrap())
}
}