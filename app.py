import os
import urllib
from flask import Flask, request
from django.db import connection, models
from django.db.models.expressions import RawSQL

app = Flask(__name__)

@app.route(&quot;/code-execution&quot;)
def code_execution():
code1 = request.args.get(&quot;code1&quot;)
exec(&quot;setname(&#39;%s&#39;)&quot; % code1)
return a

@app.route(&quot;/open-redirect&quot;)
def open_redirect():
redirect_loc = request.args.get(&#39;redirect&#39;)

return redirect(redirect_loc)

@app.route(&quot;/sqli/&lt;username&gt;&quot;)
def show_user(username):
with connection.cursor() as cursor:
cursor.execute(&quot;SELECT * FROM users WHERE username =
&#39;%s&#39;&quot; % username)

if __name__ == &#39;__main__&#39;:
app.run(host=&#39;0.0.0.0&#39;, port=9000)