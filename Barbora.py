#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import csv


# In[2]:


#Barbora - masło - nazwa i waga
page1=requests.get('https://barbora.pl/swieze/t-uszcze/mas-o')
soup = BeautifulSoup(page1.text, 'html.parser')
marka_maslo_barbora = soup.findAll('div', attrs={'class':'b-product--info-icons'}) 
for m1 in marka_maslo_barbora:
    print(m1.text.strip())


# In[3]:


#Barbora - masło - cena
soup = BeautifulSoup(page1.text, 'html.parser')
cena_maslo_barbora = soup.findAll('span', attrs={'class':'b-product-price-current-number'}) 
for c1 in cena_maslo_barbora:
    print(c1.text.strip())


# In[4]:


#Barbora - masło - cena za kg
soup = BeautifulSoup(page1.text, 'html.parser')
cena_kg_maslo_barbora = soup.findAll('div', attrs={'class':'b-product-price--extra'}) 
for ckg1 in cena_kg_maslo_barbora:
    print(ckg1.text.strip())


# In[5]:


#Barbora - mleko - nazwa i waga
page2=requests.get('https://barbora.pl/swieze/mleko/pasteryzowane')
soup = BeautifulSoup(page2.text, 'html.parser')
marka_mleko_barbora = soup.findAll('a', attrs={'class':'b-product-title b-product-title--mobile b-link--product-info'}) 
for m2 in marka_mleko_barbora[:-1]:
    print(m2.text.strip())


# In[6]:


#Barbora - mleko - cena
soup = BeautifulSoup(page2.text, 'html.parser')
cena_mleko_barbora = soup.findAll('span', attrs={'class':'b-product-price-current-number'}) 
for c2 in cena_mleko_barbora:
    print(c2.text.strip())


# In[7]:


#Barbora - mleko - cena za l
soup = BeautifulSoup(page2.text, 'html.parser')
cena_l_mleko_barbora = soup.findAll('div', attrs={'class':'b-product-price--extra'}) 
for cl2 in cena_l_mleko_barbora:
    print(cl2.text.strip())


# In[8]:


#Barbora - kawa rozpuszczalna - nazwa i waga
page3=requests.get('https://barbora.pl/artyku-y-spozywcze/kawa-kakao-i-herbata/kawa-rozpuszczalna-kakao-i-goraca-czekolada')
soup = BeautifulSoup(page3.text, 'html.parser')
marka_kawa_barbora = soup.findAll('a', attrs={'class':'b-product-title b-product-title--mobile b-link--product-info'}) 
for m3 in marka_kawa_barbora[:-5]:
    print(m3.text.strip())


# In[9]:


#Barbora - kawa rozpuszczalna - cena
soup = BeautifulSoup(page3.text, 'html.parser')
cena_kawa_barbora = soup.findAll('span', attrs={'class':'b-product-price-current-number'}) 
for c3 in cena_kawa_barbora:
    print(c3.text.strip())


# In[10]:


#Barbora - kawa rozpuszczalna - cena za kg
soup = BeautifulSoup(page3.text, 'html.parser')
cena_kg_kawa_barbora = soup.findAll('div', attrs={'class':'b-product-price--extra'}) 
for ckg3 in cena_kg_kawa_barbora:
    print(ckg3.text.strip())


# In[11]:


#Barbora - majonez - nazwa i waga
page4=requests.get('https://barbora.pl/wyszukiwanie?q=majonez')
soup = BeautifulSoup(page4.text, 'html.parser') 
marka_majonez_barbora = soup.findAll('a', attrs={'class':'b-product-title b-product-title--mobile b-link--product-info'}) 
for m4 in marka_majonez_barbora[:-1]:
    print(m4.text.strip())


# In[12]:


#Barbora - majonez - cena
soup = BeautifulSoup(page4.text, 'html.parser')
cena_majonez_barbora = soup.findAll('span', attrs={'class':'b-product-price-current-number'}) 
for c4 in cena_majonez_barbora:
    print(c4.text.strip())


# In[13]:


#Barbora - majonez - cena za kg
soup = BeautifulSoup(page4.text, 'html.parser')
cena_l_majonez_barbora = soup.findAll('div', attrs={'class':'b-product-price--extra'}) 
for cl4 in cena_l_majonez_barbora:
    print(cl4.text.strip())


# In[14]:


#Barbora - olej rzepakowy - nazwa i waga
page5=requests.get('https://barbora.pl/artyku-y-spozywcze/oleje-i-octy/olej-rzepakowy')
soup = BeautifulSoup(page5.text, 'html.parser') 
marka_olej_barbora = soup.findAll('a', attrs={'class':'b-product-title b-product-title--mobile b-link--product-info'}) 
for m5 in marka_olej_barbora:
    print(m5.text.strip())


# In[15]:


#Barbora - olej rzepakowy - cena
soup = BeautifulSoup(page5.text, 'html.parser')
cena_olej_barbora = soup.findAll('span', attrs={'class':'b-product-price-current-number'}) 
for c5 in cena_olej_barbora:
    print(c5.text.strip())


# In[16]:


#Barbora - olej rzepakowy - cena za l
soup = BeautifulSoup(page5.text, 'html.parser')
cena_l_olej_barbora = soup.findAll('div', attrs={'class':'b-product-price--extra'}) 
for ckg5 in cena_l_olej_barbora:
    print(ckg5.text.strip())


# In[17]:


#Barbora - woda niegazowana - nazwa i waga
page6=requests.get('https://barbora.pl/napoje/woda/woda-niegazowana')
soup = BeautifulSoup(page6.text, 'html.parser') 
marka_woda_barbora = soup.findAll('a', attrs={'class':'b-product-title b-product-title--mobile b-link--product-info'}) 
for m6 in marka_woda_barbora[:-24]:
    print(m6.text.strip())


# In[18]:


#Barbora - woda niegazowana - cena
soup = BeautifulSoup(page6.text, 'html.parser')
cena_woda_barbora = soup.findAll('span', attrs={'class':'b-product-price-current-number'}) 
for c6 in cena_woda_barbora:
    print(c6.text.strip())


# In[19]:


#Barbora - woda niegazowana - cena za l
soup = BeautifulSoup(page6.text, 'html.parser')
cena_l_woda_barbora = soup.findAll('div', attrs={'class':'b-product-price--extra'}) 
for cl6 in cena_l_woda_barbora:
    print(cl6.text.strip())


# In[20]:


#Barbora - cukier - nazwa i waga
page7=requests.get('https://barbora.pl/artyku-y-spozywcze/cukier-i-sol/cukier')
soup = BeautifulSoup(page7.text, 'html.parser') 
marka_cukier_barbora = soup.findAll('a', attrs={'class':'b-product-title b-product-title--mobile b-link--product-info'}) 
for m7 in marka_cukier_barbora[:-3]:
    print(m7.text.strip())


# In[21]:


#Barbora - cukier - cena
soup = BeautifulSoup(page7.text, 'html.parser')
cena_cukier_barbora = soup.findAll('span', attrs={'class':'b-product-price-current-number'}) 
for c7 in cena_cukier_barbora:
    print(c7.text.strip())


# In[22]:


#Barbora - cukier - cena za kg
soup = BeautifulSoup(page7.text, 'html.parser')
cena_kg_cukier_barbora = soup.findAll('div', attrs={'class':'b-product-price--extra'}) 
for ckg7 in cena_kg_cukier_barbora:
    print(ckg7.text.strip())


# In[23]:


with open("marka_maslo_barbora.csv","w") as csv_file:
    writer=csv.writer(csv_file)
    for m1 in marka_maslo_barbora:
         writer.writerow([m1.text.strip()])


# In[24]:


with open("cena_maslo_barbora.csv","w") as csv_file:
    writer=csv.writer(csv_file)
    for c1 in cena_maslo_barbora:
         writer.writerow([c1.text.strip()])


# In[25]:


with open("cena_kg_maslo_barbora.csv","w") as csv_file:
    writer=csv.writer(csv_file)
    for ckg1 in cena_kg_maslo_barbora:
         writer.writerow([ckg1.text.strip()])


# In[26]:


with open("marka_mleko_barbora.csv","w") as csv_file:
    writer=csv.writer(csv_file)
    for m2 in marka_mleko_barbora[:-1]:
         writer.writerow([m2.text.strip()])


# In[27]:


with open("cena_mleko_barbora.csv","w") as csv_file:
    writer=csv.writer(csv_file)
    for c2 in cena_mleko_barbora:
         writer.writerow([c2.text.strip()])


# In[28]:


with open("cena_l_mleko_barbora.csv","w") as csv_file:
    writer=csv.writer(csv_file)
    for cl2 in cena_l_mleko_barbora:
         writer.writerow([cl2.text.strip()])


# In[29]:


with open("marka_kawa_barbora.csv","w") as csv_file:
    writer=csv.writer(csv_file)
    for m3 in marka_kawa_barbora[:-5]:
         writer.writerow([m3.text.strip()])


# In[30]:


with open("cena_kawa_barbora.csv","w") as csv_file:
    writer=csv.writer(csv_file)
    for c3 in cena_kawa_barbora:
         writer.writerow([c3.text.strip()])


# In[31]:


with open("cena_kg_kawa_barbora.csv","w") as csv_file:
    writer=csv.writer(csv_file)
    for ckg3 in cena_kg_kawa_barbora:
         writer.writerow([ckg3.text.strip()])


# In[32]:


with open("marka_majonez_barbora.csv","w") as csv_file:
    writer=csv.writer(csv_file)
    for m4 in marka_majonez_barbora[:-1]:
         writer.writerow([m4.text.strip()])


# In[33]:


with open("cena_majonez_barbora.csv","w") as csv_file:
    writer=csv.writer(csv_file)
    for c4 in cena_majonez_barbora:
         writer.writerow([c4.text.strip()])


# In[34]:


with open("cena_l_majonez_barbora.csv","w") as csv_file:
    writer=csv.writer(csv_file)
    for cl4 in cena_l_majonez_barbora:
         writer.writerow([cl4.text.strip()])


# In[35]:


with open("marka_olej_barbora.csv","w") as csv_file:
    writer=csv.writer(csv_file)
    for m5 in marka_olej_barbora:
         writer.writerow([m5.text.strip()])


# In[36]:


with open("cena_olej_barbora.csv","w") as csv_file:
    writer=csv.writer(csv_file)
    for c5 in cena_olej_barbora:
         writer.writerow([c5.text.strip()])


# In[37]:


with open("cena_l_olej_barbora.csv","w") as csv_file:
    writer=csv.writer(csv_file)
    for ckg5 in cena_l_olej_barbora:
         writer.writerow([ckg5.text.strip()])


# In[38]:


with open("marka_woda_barbora.csv","w") as csv_file:
    writer=csv.writer(csv_file)
    for m6 in marka_woda_barbora[:-24]:
         writer.writerow([m6.text.strip()])


# In[39]:


with open("cena_woda_barbora.csv","w") as csv_file:
    writer=csv.writer(csv_file)
    for c6 in cena_woda_barbora:
         writer.writerow([c6.text.strip()])


# In[40]:


with open("cena_l_woda_barbora.csv","w") as csv_file:
    writer=csv.writer(csv_file)
    for cl6 in cena_l_woda_barbora:
         writer.writerow([cl6.text.strip()])


# In[41]:


with open("marka_cukier_barbora.csv","w") as csv_file:
    writer=csv.writer(csv_file)
    for m7 in marka_cukier_barbora[:-3]:
         writer.writerow([m7.text.strip()])


# In[42]:


with open("cena_cukier_barbora.csv","w") as csv_file:
    writer=csv.writer(csv_file)
    for c7 in cena_cukier_barbora:
         writer.writerow([c7.text.strip()])


# In[43]:


with open("cena_kg_cukier_barbora.csv","w") as csv_file:
    writer=csv.writer(csv_file)
    for ckg7 in cena_kg_cukier_barbora:
         writer.writerow([ckg7.text.strip()])

