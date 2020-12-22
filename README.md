# pipでgithub上のライブラリをインストールする

[この記事](https://qiita.com/syakoo/items/deddeb91e2a0313a45f7)を参考に
githubのrepositoryにあるpythonスクリプトをインストールする。

基本は、
```shell
pip install git+https://github.com/<account>/<repository>
```

を叩くだけ。ブランチで切ったほうをインストールするには、
```shell
pip install git+https://github.com/<account>/<repository>@<branch>
```

とすればよい。
