from flask import Flask, render_template, jsonify
from database import load_jobs_from_db, load_jobs_from_db_json



app = Flask(__name__)

@app.route("/")
def hello_jovian():
  jobs_list = load_jobs_from_db()
  return render_template('home.html', 
                         jobs=jobs_list, 
                         company_name='Jovian')


@app.route("/api/jobs")
def list_jobs():
  jobs_list = load_jobs_from_db_json()
  return(jobs_list)



if __name__ == "__main__":
  print("I'm inside the if now")
  app.run(host='0.0.0.0', debug=True)
