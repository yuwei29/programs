package main

import (
	"gin-test/dto"
	"net/http"

	"github.com/gin-gonic/gin"
)

func main() {
	r := gin.Default()
	//2.绑定路由规则，执行的函数
	r.GET("/", func(context *gin.Context) {
		context.String(http.StatusOK, "Hello 世界!")
	})
	r.POST("/admin", func(c *gin.Context) {
		var data dto.PlayerDto
		c.Bind(&data)
		println("name:", data.Name, "age:", data.Age, "rank:", data.Rank)
	})
	//3.监听端口，默认8080
	r.Run(":8080")
}
