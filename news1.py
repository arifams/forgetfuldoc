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


    # time
    time = soup.find('time')
    if 'washingtonpost.com' in url :
        spans = soup.find_all('span', attrs={'class':'author-timestamp'})
        for span in spans:
            time = str(span)
            time = re.sub('<[^>]+>', '', time)
    elif 'nytimes.com' in url :
        time = str(time)
        time = re.sub('<[^>]+>', '', time)
    elif 'newyorker.com' in url :
        time = soup.find('p', attrs={'class': 'ArticleTimestamp__timestamp___1klks '})
    elif 'nrc.nl' in url :
        time = str(time)
        time = re.sub('<[^>]+>', '', time)

    # pictures extraction
    # gambars = soup.find_all('img')
    if 'nytimes.com' in url :
        # for gambar in gambars :
        #     gambar = gambar['src']
        # gambar = '<img src=\"' + gambar + '\">'
        gambar = soup.find('img', attrs={'class':'css-11cwn6f'})
        # gambar = soup.findAll('srcSet')
    elif 'newyorker.com' in url :
        gambar = soup.find('source')
    else :
        gambar = 'Under construction pictures'

    # caption picture extraction
    if 'nytimes.com' in url :
        caption = soup.find('figcaption')
        caption = str(caption)
    else :
        caption = 'Under construction caption'
    
    # cleanup wapo, nyt, newyorker content
    txt_content = re.sub('<[^>]+>', '', para)
    txt_content = txt_content.replace('.,', '.\n')
    txt_content = txt_content.replace('\n', '<br>')
    txt_content = txt_content.replace('<br>\n<br>\n', '<br>')
    txt_content = txt_content.replace('<br> , ', '<br>')
    txt_content = txt_content.replace(', By', 'By')
    txt_content = txt_content.replace('[Advertisement, Supported by, ', '')
    txt_content = txt_content.replace(', Advertisement]', '')
    txt_content = txt_content.replace(', , , Advertisement]', '')
    txt_content = txt_content.replace('[, ', '')
    txt_content = txt_content.replace(', , ,', '.')
    txt_content = txt_content.replace(', ,', ',')
    # cleanup nrc content
    txt_content = txt_content.replace('[N.B. Het kan zijn dat elementen ontbreken aan deze printversie.', '')
    txt_content = txt_content.replace('Heeft u een tip over dit onderwerp, ziet u een spelfout of feitelijke onjuistheid?', '')
    txt_content = txt_content.replace('We stellen het zeer op prijs als u ons daarover een bericht stuurt.', '')
    txt_content = txt_content.replace('U kunt ons ook anoniem een tip geven.', '')
    txt_content = txt_content.replace(', ]', '')
    return render_template("result_form.html", isi_berita = txt_content, judul = title_str, waktu = time, foto = gambar, judul_foto = caption)

if __name__ == '__main__':
    app.run()