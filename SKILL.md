如果需要下载视频，使用如下命令，`XXX` 为用户希望下载的视频
yt-dlp XXX

如果需要从 AINews 的 RSS 中按关键词获取新闻，使用如下命令，`XXX` 为用户希望检索的关键词。先从 `https://news.smol.ai/rss.xml` 获取 RSS，再按标题进行不区分大小写匹配，每条仅输出标题、时间和链接；如果没有命中结果，则输出“未找到相关资讯”。
KW="XXX"; export KW; curl -sL -A "Mozilla/5.0" "https://news.smol.ai/rss.xml" | perl -0ne 'BEGIN{$kw=lc($ENV{KW}//""); $n=0} while (m#<item>.*<title>(.*?)</title>.*?<link>(.*?)</link>.*?<pubDate>(.*?)</pubDate>.*?</item>#sg) { ($t,$l,$p)=($1,$2,$3); next if index(lc($t), $kw) < 0; print "标题: $t\n时间: $p\n链接: $l\n\n"; last if ++$n >= 2 } END { print "未找到相关资讯\n" if !$n }'