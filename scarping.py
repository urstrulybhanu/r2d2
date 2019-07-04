import bs4

from urllib.request import urlopen as uReq
import pandas as pd 

from bs4 import BeautifulSoup as soup
starsList=[]
movieName=[]
runTimePro=[]
ratingPro=[]
genrePro=[]
starsPro=[]
se=[]
    

o=1
while(True):
    print(o)
    if o>1700:
        break 
    
    my_url="https://www.imdb.com/search/title/?genres=horror&start="+str(o)+"&explore=title_type&ref_=adv_nxt"
    o=o+50

    uClient=uReq(my_url)



    page_html=uClient.read()


    uClient.close()


    page_soup=soup(page_html,"html.parser")


    #containers=page_soup.find_all("div",{"class":"Stars:"})


    #contain=containers[0]
    
    s=page_soup.find_all("div",{"class":"lister-item-content"})
    for i in s:
        try:
            movieName.append(i.h3.a.text)
            
        except:
            movieName.append("NA")
        try:
            ratingPro.append(i.div.div.strong.text)
        except:
            ratingPro.append(-1)
        try:    
            runtime=[j.text for j in i.findAll('span', {'class': 'runtime'})]
            runTimePro.append(runtime[0])
        except:
            runTimeA.append(-1)
        try:    
            genre=[j.text for j in i.findAll('span', {'class': 'genre'})]
            genrePro.append(genre[-1])
            print(genreA)
        except:
            genrePro.append("NA")
        try:
            stars=[j.text for j in i.findAll('p', {'class': ''})]
            se.append(stars)
            for ele in se:
                for ele2 in ele:
                    
                    ele2.strip()
                    #print(ele2)
                    StarsPro.append(ele2)
            
               # print(ele)
               #print(stars[-1])
        except:
            starsPro.append("NA")
    
    """try: 
        s=page_soup.find_all("div",{"class":"lister-item mode-advanced"})
        for i in s:
            print(i.h3.a.text)
            print(i.div.div.strong)
            runtime=[j.text for j in i.findAll('span', {'class': 'runtime'})]
            print(runtime[0])
            genre=[j.text for j in i.findAll('span', {'class': 'genre'})]
            print(genre)
            stars=[j.text for j in i.findAll('p', {'class': ''})]
            print(stars)    
    except:
        pass
    """
   
#print(starsList)
d={"MovieName":movieName,"Rating":ratingPro,"Genre":genrePro,"runtime":runTimePro,"stars":starsPro}
print(len(movieName),len(ratingPro),len(genrePro),len(runTimePro),len(starsPro))
df=pd.DataFrame(d)
print(df.head())
print(df.shape)

df.to_csv("MoviesData.csv")

            
            
            
            
    
    
