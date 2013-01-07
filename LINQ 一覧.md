|演算子|説明|
|:--|:-------------|
|Where|述語関数に基づく制限演算子|
|Select/SelectMany|選択関数に基づくプロジェクション演算子|
|Take/SkipTakeWhile/SkipWhile|位置決め関数または述語関数に基づくパーティション分割演算子|
|Join/GroupJoin|キー選択関数に基づく結合演算子|
|Concat|連結演算子|
|OrderBy/ThenBy/OrderByDescending/ThenByDescending|省略可能なキー選択関数と比較関数に基づいて昇順または降順に並べ替える並べ替え演算子|
|Reverse|シーケンスの順序を反転する並べ替え演算子|
|GroupBy|省略可能なキー選択関数と比較関数に基づくグループ化演算子|
|Distinct|重複を削除するセット演算子|
|Union/Intersect|和集合または積集合を返すセット演算子|
|Except|差集合を返すセット演算子|
|AsEnumerable|IEnumerable<T> への変換演算子|
|ToArray/ToList|配列または List<T> への変換演算子|
|ToDictionary/ToLookup|キー選択関数に基づく Dictionary<K,T> または Lookup<K,T> (多重辞書) への変換演算子|
|OfType/Cast|フィルタ選択に基づく IEnumerable<T> への変換演算子または型引数への変換|
|SequenceEqual|対になった要素の等値性をチェックする等価演算子|
|First/FirstOrDefault/Last/LastOrDefault/Single/SingleOrDefault|省略可能な述語関数に基づいて初期要素、最終要素、または唯一の要素を返す要素演算子|
|ElementAt/ElementAtOrDefault|位置に基づいて要素を返す要素演算子|
|DefaultIfEmpty|空のシーケンスを既定値の単一シーケンスに置き換える要素演算子|
|Range|範囲内の数を返す生成演算子|
|Repeat|特定の値の複数の出現を返す生成演算子|
|Empty|空のシーケンスを返す生成演算子|
|All/Any|述語関数の実存的または普遍的充足度をチェックする限定子|
|Contains|特定の要素の存在をチェックする限定子|
|Count/LongCount|省略可能な述語関数に基づいて要素を数える集計演算子|
|Sum/Min/Max/Average|省略可能な選択関数に基づく集計演算子|
|Aggregate|累積関数および省略可能なシードを基に複数の値を集積する集計演算子|
