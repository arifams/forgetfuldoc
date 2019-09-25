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
    # headers = {
    # 'Accept-Encoding': 'gzip, deflate, sdch',
    # 'Accept-Language': 'en-US,en;q=0.8',
    # 'Upgrade-Insecure-Requests': '1',
    # 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    # 'Cache-Control': 'max-age=0',
    # 'Connection': 'keep-alive',}
    url = request.form['isi_formulir']
    # mimicking headers with passing parameter variable headers
    # req_get_url = requests.get(url, headers=headers)
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
    return render_template("result_form.html", isi_berita = txt_content, judul = title_str, waktu = time, foto = gambar)

if __name__ == '__main__':
    app.run()