
from datetime import date, datetime
from flask import Flask, request
from flask_restful import Resource, Api
import script

app = Flask(__name__)

api = Api(app)

QQ2203_list = [1668384328,121046785,414951321,1357031377,2060359190,2274878949,2465508751,2857976554,3316194733,471005298,905783999,1258243959,1521453135,1535321782,1612890466,1773301934,2135523213,2170351257,2376383602,2717971532,2741547963,2767789935,2849822473,2859863647,2964319856,2968950336,2979245421,3099756105,3208769953,3314227204,3323298037,3345967904,3358646384,3434774366]
G1id=923558852
G2id=895733915

fL=str("0")
Ti1=str("19:00")
Ti2=str("19:01")

class AcceptMes(Resource):

    
    
    def post(self):
        # 这里对消息进行分发，暂时先设置一个简单的分发
        
        _ = request.json
        if _.get("message_type") == "private":  # 说明有好友发送信息过来
            uid = _["sender"]["user_id"]  # 获取发信息的好友qq号
            message = _["raw_message"]  # 获取发送过来的消息
            script.handle_private(uid, message)
        
        s=str(datetime.now())
        global fL,Ti1,Ti2,G1id
            
        if(s[11:16]==Ti2):
            fL=str("0")
            
        if fL==str("1"):
            return

        if(fL==str("0") and s[11:16]==Ti1):
            fL=str("1")
                
        if fL==str("0"):
            return 
            
        for i in QQ2203_list:
                # script.send(i,f"请检查核酸是否填表")
            script.send_private(i,f"请检查核酸是否填表",G1id)    
        return 
        
    


api.add_resource(AcceptMes, "/", endpoint="index")
if __name__ == '__main__':
    app.run("0.0.0.0", "5701")  # 注意，这里的端口要和配置文件中的保持一致