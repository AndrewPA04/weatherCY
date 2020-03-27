import requests
import bs4
import tkinter

window = tkinter.Tk()
window.title('Nicosia Weather App')
window.geometry("900x600")
window.resizable(False,False) #could work with window.resizable(0,0)
window.config(bg = "yellow")


label = tkinter.Label(height = 5,width = 50,bg = 'green')
label.place(x = 310,y = 300)
label.config(font = 66)

heading = tkinter.Label(width = 50,height = 5,bg = 'red')
heading.place(x = 250,y = 150)
heading.config(font = 66,text = 'This tracks Nicosias weather')

def Track():
    response = requests.get('https://www.cyprus-weather.org/')
    content = response.content
    soup = bs4.BeautifulSoup(content,'html.parser')
    nowContainer = soup.find_all(class_='cwLocationBox b0')
    TomorrowWeather = soup.find_all(class_ = 'cwLocationBox b2')
    highTemp = TomorrowWeather[0].find_all(class_='hi')
    lowTemp = TomorrowWeather[0].find_all(class_='lo')
    temperature = nowContainer[0].find_all('b')
    highTempString = str(highTemp[0].text.strip())
    lowTempString = str(lowTemp[0].text.strip())
    temperatureString = str(temperature[0].text.strip())
    CheckCold = int(highTempString.replace('°',''))
    temperature_sentence = 'The current temperature is '+temperatureString+'\n The highest temperature for tomorrow will be '+ highTempString+'\n The lowest temperature for tomorrow will be '+lowTempString
    if CheckCold<22:
        label.config(text = f'{temperature_sentence} \n Tomorrow it is going to be cold,Dress well!')
    else:
        label.config(text = f'{temperature_sentence} \n Tomorrow it is going to be hot')


button = tkinter.Button(width = 25,height = 5,text = 'Track Weather',command = Track,bg = 'blue',font= 44,fg = 'red')
button.place(x = 100,y = 300)

window.mainloop()
