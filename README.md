# about                                                   
chatwork apiのPython用wrapperクラスです。

## 使い方
1. pipからインストール可能です
```
pip install cwthon
```

2. 環境変数CW_TOKENに、ChatWork用APIトークンを格納して下さい。
※現在は1環境につき1つのトークンのみ対応しています。

```
export CW_TOKEN=<Your ChatWork Api Token>
```

3. コードでの使い方
```Python
from cwthon import chatwork

#コンタクト情報をDict形式で取得する。
#キー：account_id、バリュー：各コンタクトの情報　という形式になっています。
chatwork.contactDict

#account_idをキーに、一意に紐づくコンタクト情報を取得する
chatwork.getContactInfo()

#ルーム情報をDict形式で取得する。
#キー：room_id、バリュー：各ルームの情報　という形式になっています。
chatwork.roomDict

#account_idをキーに、一意に紐づくコンタクト情報を取得する
chatwork.getRoomInfo()


#リクエスト送信用インスタンスを生成
cwReq = chatwork.cwReq()

#account_idを指定してメッセージを送る場合
target_account_id = "10xxx231"
msg_account_id    = "test message for account"
cwReq.sendMsgToAccount(account_id=target_account_id, msg=msg_account_id)

#room_idを指定してメッセージを送る場合
target_room_id = "232xxxx093"
msg_room_id    = "test message for room"
cwReq.sendMsgToAccount(room_id=target_room_id, msg=msg_room_id)

#sendMsg~メソッドは、戻り値としてAPIのレスポンス情報がか格納されたcwReqインスタンスを返す
cwReq = cwReq.sendMsgToAccount(room_id=target_room_id, msg=msg_room_id)
res = cwReq.res

#cwGrammerクラスからは、チャットワーク用の文法をEnum形式で取得可能です
from chatwork_prop import cwGrammar
class cwGrammar(Enum) :
    TO = '[To:{account_id}]'
    QUOTE_TIME = '[qt][qtmeta aid={account_id} time={timestamp}]{body}[/qt]'
    QUOTE = '[qt][qtmeta aid={account_id}]{body}[/qt]'
    INFO = '[info]{body}[/info]'
    INFO_TITLE = '[info][title]{title}[/title]{body}[/info]'
    RULE = '[hr]'
    PICON = '[picon:{account_id}]'
    PICON_NAME = '[piconname:{account_id}]'
```

## 今後実装予定の機能
- cwResクラスのwrapper化
   - 残リクエスト数等を簡単に取得できるように変更する。
