#定义要爬取的url
$url='https://movie.douban.com/'
#定义保存的文件名
$fileName="hotMovieComments.json"

#定义空数组，存放爬取到的信息
$dataList=@()

#用Invoke-WebRequest爬取网页内容
$webContent =Invoke-WebRequest -Uri $url

#爬取页面内的热门电影的信息
$movieList = $webContent.ParsedHtml.getElementsByClassName("item") | Where-Object {$_.classname -like "item*"}

#遍历每个热门电影
foreach($movie in $movieList){
    #定义电影名字、id、热门短评和评论人昵称
    $movieName= $movie.InnerText
    $movieId=$movie.href -replace '.*\/',''
    $hotMoviewComments = $movie.getElementsByClassName("comment") | Where-Object {$_.classname -like "comment*"}
    $hotMoviewCommentTxt = $hotMoviewComments.InnerText
    $commentUserName=$movie.getElementsByClassName("name") | Where-Object {$_.classname -like "name*"}

    #循环获取每部电影的3条热评
    for($i=0;$i -lt 3;$i++){

        #定义热评：评论内容、作者昵称
        $comment=$hotMoviewCommentTxt[$i]
        $userName=$commentUserName[$i]
        #创建一个对象，用来封装爬取到的信息。
        $obj=[PSCustomObject]@{
            MovieName=$movieName
            MovieId=$movieId
            Comment=$comment
            UserName=$userName
        }
        #将爬取到的热评添加到数组
        $dataList += $obj
    }
}

#将抓取到的信息转换为json格式，并保存到文件中
$dataList | ConvertTo-Json | Out-File $fileName