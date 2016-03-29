# anaCaesar シーザー暗号簡易解析


シーザー暗号を解読したい時に（たぶんほとんどないと思われる・・・）、手っ取り早く文字をずらした結果を表示します。


## 使い方
```sh
python anaCaesar.py <暗号化文字列>
```

* 文字をずらすのはデフォルトでは1～26文字
* anaCaesar()に暗号化文字列を渡せばアルファベットを1～26文字ずつシフト(ずらして)表示します
* 元の文字が小文字であれば小文字、大文字であれば大文字で表示します

例：AZazを1文字ずらすとBAbaとなります  
対象文字が'z'の場合1文字ずらすと'a'、 対象文字が'Z'の場合1文字ずらすと'A'
```
python anaCaesar.py AZaz
1       BAba
2       CBcb
3       DCdc
・・・
24      YXyx
25      ZYzy
26      AZaz
```
## ImportError: No module named \_cursesとなった場合(Windows環境のみ？)

以下のサイトから、「curses-2.2-cp27-none-win32.whl」のファイルをダウンロード  
http://www.lfd.uci.edu/~gohlke/pythonlibs/#curses  
※ファイルは
「The files are provided "as is" without warranty or support of any kind.   
The entire risk as to the quality and performance is with you.」とのこと

pipでインストール
```
pip install curses-2.2-cp27-none-win32.whl
```

#### 参考サイト
Windows でも Python curses を使いたいんですが - quwaharaの日記 : http://quwahara.hatenablog.com/entry/2012/02/23/000639  
Python Extension Packages for Windows - Christoph Gohlke : http://www.lfd.uci.edu/~gohlke/pythonlibs/#curses



## 大文字小文字を区別して文字をずらしたい場合

現時点ではオプション指定の機能はないので、中身を開いて以下の通り修正してください。

* anaCaesar(<暗号化文字列>, False)の第2パラメータに**False**を指定

```python
anaCaesar(sys.argv[1])
↓
anaCaesar(sys.argv[1], False)
```

* 文字をずらす範囲はABCDE....VWXYZabcde....vxxyzの範囲でずらします

例：AZazを1文字ずらすとBAbaとなります  
対象文字が'z'の場合1文字ずらすと'A'、対象文字が'Z'の場合1文字ずらすと'a'
```
python anaCaesar.py AZaz
1       BabA
2       CbcB
3       DcdC
・・・
50      yXYx
51      zYZy
52      AZaz
```
