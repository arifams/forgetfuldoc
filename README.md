# forgetfuldoc app

<h3>Read information behind the screen.</h3>

<p>
<h5>Development (mac)</h5>
<br>
<strong>Activate the environment</strong>
<br>
`. venv/bin/activate` 
<br>
<strong>running flask</strong>
<br>
`export FLASK_APP=news1.py`
<br>
`export FLASK_ENV=development` (if it's for development)
<br>
`python3 -m flask run`
<br>
`flask run` 
</ul>
<ul>
<strong>Freezing the dependencies</strong>
<br>
`pip freeze`
</p>

<p>
<strong>Create text about dependencies information</strong>
<br>
`pip freeze > requirements.txt`
<strong>Create Procfile with Vi</strong>
<br>
`vi Procfile`
<br>
'web: guncorn app:app' (<i>inside the vi editor</i>)
<br>
'web: guncorn app:app' 
</p>

<p>
<h5>Using</h5>
<br>
<strong>Go to <a href="https://forgetfuldoc.herokuapp.com/">this url</a> </strong>
<br>
https://forgetfuldoc.herokuapp.com/
<br>
</p>