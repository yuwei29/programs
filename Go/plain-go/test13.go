package main

import "fmt" 

type Piece struct {
	X     int
	Y     int
	Color string
	Role  string
	Live  bool
}
type Player struct {
	Pieces [16]Piece
}

func (p *Player) init(color string) {
	for i := 0; i < 16; i++ {
		p.Pieces[i].Color = color
		p.Pieces[i].Live = true
	}
	p.Pieces[0].Role = "jiang"
	p.Pieces[0].X = 0
	p.Pieces[0].Y = -4
	for i := 1; i <= 2; i++ {
		p.Pieces[i].Role = "shi"
		if i == 2 {
			p.Pieces[i].X = 1
		} else {
			p.Pieces[i].X = -1
		}
		p.Pieces[i].Y = -4
	}
	for i := 3; i <= 4; i++ {
		p.Pieces[i].Role = "xiang"
		if i == 4 {
			p.Pieces[i].X = 2
		} else {
			p.Pieces[i].X = -2
		}
		p.Pieces[i].Y = -4
	}
	for i := 5; i <= 6; i++ {
		p.Pieces[i].Role = "ma"
		if i == 6 {
			p.Pieces[i].X = 3
		} else {
			p.Pieces[i].X = -3
		}
		p.Pieces[i].Y = -4
	}
	for i := 7; i <= 8; i++ {
		p.Pieces[i].Role = "ju"
		if i == 8 {
			p.Pieces[i].X = 4
		} else {
			p.Pieces[i].X = -4
		}
		p.Pieces[i].Y = -4
	}
	for i := 9; i <= 10; i++ {
		p.Pieces[i].Role = "pao"
		if i == 10 {
			p.Pieces[i].X = 3
		} else {
			p.Pieces[i].X = -3
		}
		p.Pieces[i].Y = -2
	}
	for i := 11; i < 16; i++ {
		p.Pieces[i].Role = "bing"
		p.Pieces[i].X = 2 * (i - 13)
		p.Pieces[i].Y = -1
	}

	if color == "black" {
		for i := 0; i < 16; i++ {
			p.Pieces[i].X *= -1
			p.Pieces[i].Y = 1 - p.Pieces[i].Y
		}
	}
}
func main() {
  p1:=new(Player)
  p2:=new(Player)
  p1.init("red")
  p2.init("black")
  fmt.Println(p1)
  fmt.Println(p2)
}
