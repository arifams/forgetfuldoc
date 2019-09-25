# theirnews app

<h3>Read information behind the screen.</h3>

<p>
<h5>Development (mac)</h5>
<li>
<ul><strong>Activate the environment</strong>
<br>
`. venv/bin/activate` 
</ul>
<ul><strong>running flask</strong>
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
</ul>>
<ul>
<strong>Create text about dependencies information</strong>
<br>
`pip freeze > requirements.txt`
</ul>
<ul>
<strong>Create Procfile with Vi</strong>
<br>
`vi Procfile`
</ul>
<ul>
'web: guncorn app:app' (<i>inside the vi editor</i>)
<br>
'web: guncorn app:app' 
</ul>
</li>
</p>

<p>
<h5>Using</h5>
<li>
	<ul>
		<strong>Go to <a href="https://forgetfuldoc.herokuapp.com/">this url</a> </strong>
	</ul>
	<ul>
		`https://forgetfuldoc.herokuapp.com/`
	</ul>
	<ul>
		<strong>Paste the URL needed to get the screened content</strong>
	</ul>
</li>
</p>