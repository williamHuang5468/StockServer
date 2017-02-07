# Password

## [Salt](http://plainpass.com/2012/06/best-practicing-for-password-protection.html)


隨機加料式雜湊法

    Hash ( 隨機數字 + 明碼 ) # 加料的數字以隨機方式取得。

### Todo 

- [x] Hash 明碼，然後可以驗證
- [x] Hash 固定數字 + 明碼，然後可以驗證
- [x] Hash 隨機數字 + 明碼，然後可以驗證

> 我不需要還原密碼，只要把使用者的輸入抓進來運算，比對結果就可以了。

import hashlib
import uuid

def create_salt():
    return uuid.uuid4().hex

def hash(word, salt):
    return (hashlib.md5((word + salt).encode()).hexdigest())

def check(hash_password, user_password, salt):
    return hash_password == md5(user_password + salt)
