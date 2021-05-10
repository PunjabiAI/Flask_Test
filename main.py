from flask import Flask, render_template, request

app = Flask(__name__)

# @app.route('/file')
@app.route('/file/',methods = ['GET'])
def results():
    file_name = request.args.get('file_name', None)
    start_line = request.args.get('start_line', None)
    end_line = request.args.get('end_line', None)
    print(file_name)
    print(start_line)
    print(end_line)
    if file_name != None:
        print('=========')
        # f = open(str(file_name),"r",encoding="utf8")
        # with open(file_name, 'rb') as f:
        file_data = open(file_name, encoding="utf-8", errors='ignore').readlines()
        result=[]
        for i in file_data:
            content = i.encode()
            content = content.decode()
            result.append(content)
            # result.append('\n')


    else:

        file_data = open("file1.txt", errors='ignore').readlines()
        result =file_data
    if start_line != None and end_line != None:
        result = result[int(start_line):int(end_line)]
    else:
        result = result
    return render_template("result.html",result = result,)

if __name__ == '__main__':
   app.run(debug=True,port=2001)