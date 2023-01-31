package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

type Tr struct {
	Root     string
	Children []Tr
}
type Pu []string

var pu Pu

func main() {
	var n, m int
	var t0 Tr
	fmt.Scanln(&n)
	pus := make([]Pu, n)
	people := make(map[string]int, 0)
	certain := make(map[string]bool, 0)
	ding := make([]bool, n)
	reader := bufio.NewReader(os.Stdin)
	for i := 0; i < n; i++ {
		strBytes, _, _ := reader.ReadLine()
		s := string(strBytes)
		pu = strings.Fields(s)
		for j := 0; j < len(pu); j++ {
			people[pu[j]] = j
			certain[pu[j]] = false
		}
		//t1.Root = pu[0]
		pus[i] = pu
	}
	//for i:=0
	fmt.Scanln(&m)
	renshu := len(certain)
	dingshu := 0
	for k, v := range people {
		if v == 0 {
			fmt.Println(k)
			t0.Root = k
			certain[k] = true
			dingshu++
			break
		}
	}
	for i := 0; i < n; i++ {
		if t0.Root == pus[i][0] {
			ding[i] = true
			for j := 1; j < len(pus[i]); j++ {
				people[pus[i][j]] = j
				if certain[pus[i][j]] == false {
					certain[pus[i][j]] = true
					dingshu++
				}

			}
		}
	}
	for dingshu < renshu {
		for i := 0; i < n; i++ {
			if ding[i] {
				continue
			}
			if certain[pus[i][0]] {
				for j := 1; j < len(pus[i]); j++ {
					if certain[pus[i][j]] == false {
						people[pus[i][j]] = j + people[pus[i][0]]
						certain[pus[i][j]] = true
						dingshu++
					}
				}
			}

		}
	}
	//fmt.Println(people)
	//fmt.Println(m)
	ans := 0
	for _, v := range people {
		if v == m-1 {
			ans++
		}
	}
	fmt.Println(ans)
	fmt.Println(people)
}
