from flask import Flask, request, render_template
import re
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('my_form.html')

@app.route('/', methods=['POST'])
def my_form_post() :
    url = request.form['isi_formulir']
    req_get_url = requests.get(url)
    txt = req_get_url.text
    
    soup = BeautifulSoup(txt, 'lxml')
    
    title = soup.find('title')
    title_str = str(title.string)
    
    paragraph = soup.find_all('p')
    para = str(paragraph)
    
    time = soup.find('time')
    time = str(time)
    time = re.sub('<[^>]+>', '', time)

    gambars = soup.find_all('img')
    for gambar in gambars :
        gambar = gambar['src']
    
    txt_content = re.sub('<[^>]+>', '', para)
    txt_content = txt_content.replace('.,', '.\n')
    txt_content = txt_content.replace('\n', '<br>')
    txt_content = txt_content.replace('<br>\n<br>\n', '<br>')
    txt_content = txt_content.replace('<br> , ', '<br>')
    txt_content = txt_content.replace('[Advertisement, Supported by, ', '')
    txt_content = txt_content.replace(', Advertisement]', '')
    txt_content = txt_content.replace(', , , Advertisement]', '')
    txt_content = txt_content.replace('[, ', '')
    txt_content = txt_content.replace(', , ,', '.')
    txt_content = txt_content.replace(', ,', ',')
    return render_template("result_form.html", isi_berita = txt_content, judul = title_str, waktu = time, foto = gambar)

if __name__ == '__main__':
    app.run()