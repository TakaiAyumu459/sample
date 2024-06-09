-- @block
-- サンプル用のデータベースを作成する

CREATE DATABASE sample;

-- @block
-- サンプル用のデータベースを削除する
-- CREATEとDROPを同じブロックに記述すると複文になり、
-- トランザクションが内で実行されるためエラーになってしまう。
-- 単文なら実行できる

DROP DATABASE IF EXISTS sample;

