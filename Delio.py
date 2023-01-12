#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import csv


# In[2]:


#Delio - mleko - nazwa
page1=requests.get('https://delio.com.pl/categories/nabial/mleko-i-zamienniki/mleko?gclid=CjwKCAiAh9qdBhAOEiwAvxIokw6tu2y2VMMR4ILOjqu3wHL4y2pO6UTMP3AK9JqBBtrXdvayX-d5oBoCcsoQAvD_BwE')
soup = BeautifulSoup(page1.text, 'html.parser')
marka_mleko_delio = soup.findAll('p', attrs={'class':'text-sm block font-medium line-clamp-2 lmd:text-base lmd:leading-5'}) 
for m1 in marka_mleko_delio:
    print(m1.text.strip())


# In[3]:


#Delio - mleko - cena
soup = BeautifulSoup(page1.text, 'html.parser')
cena_mleko_delio = soup.findAll('span', attrs={'class':'text-primary-900 text-base'}) 
for c1 in cena_mleko_delio:
    print(c1.text.strip())


# In[4]:


#Delio - mleko - waga
soup = BeautifulSoup(page1.text, 'html.parser')
waga_mleko_delio = soup.findAll('p', attrs={'class':'text-xs text-gray-500 truncate mx-2 xsm:mx-4 pb-1'}) 
for w1 in waga_mleko_delio:
    print(w1.text.strip())


# In[5]:


#Delio - maslo - nazwa
page2=requests.get('https://delio.com.pl/categories/nabial/tluszcze1/masla')
soup = BeautifulSoup(page2.text, 'html.parser')
marka_maslo_delio = soup.findAll('p', attrs={'class':'text-sm block font-medium line-clamp-2 lmd:text-base lmd:leading-5'}) 
for m2 in marka_maslo_delio[:-2]:
    print(m2.text.strip())


# In[6]:


#Delio - maslo - cena
soup = BeautifulSoup(page2.text, 'html.parser')
cena_maslo_delio = soup.findAll('span', attrs={'class':'text-primary-900 text-base'}) 
for c2 in cena_maslo_delio:
    print(c2.text.strip())


# In[7]:


#Delio - maslo - waga
soup = BeautifulSoup(page2.text, 'html.parser')
waga_maslo_delio = soup.findAll('p', attrs={'class':'text-xs text-gray-500 truncate mx-2 xsm:mx-4 pb-1'}) 
for w2 in waga_maslo_delio[:-2]:
    print(w2.text.strip())


# In[8]:


#Delio - kawa rozpuszczalna - nazwa
page3=requests.get('https://delio.com.pl/categories/spizarnia-kawa-i-herbata/kawa-i-kakao/rozpuszczalna')
soup = BeautifulSoup(page3.text, 'html.parser')
marka_kawa_delio = soup.findAll('p', attrs={'class':'text-sm block font-medium line-clamp-2 lmd:text-base lmd:leading-5'}) 
for m3 in marka_kawa_delio:
    print(m3.text.strip())


# In[9]:


#Delio - kawa rozpuszczalna - cena
soup = BeautifulSoup(page3.text, 'html.parser')
cena_kawa_delio = soup.findAll('span', attrs={'class':'text-primary-900 text-base'}) 
for c3 in cena_kawa_delio:
    print(c3.text.strip())


# In[10]:


#Delio - kawa rozpuszczalna - waga
soup = BeautifulSoup(page3.text, 'html.parser')
waga_kawa_delio = soup.findAll('p', attrs={'class':'text-xs text-gray-500 truncate mx-2 xsm:mx-4 pb-1'}) 
for w3 in waga_kawa_delio:
    print(w3.text.strip())


# In[11]:


#Delio - majonez - nazwa
page4=requests.get('https://delio.com.pl/categories/spizarnia-kawa-i-herbata/przyprawysosy-fixy/majonezy-i-dressingi')
soup = BeautifulSoup(page4.text, 'html.parser')
marka_majonez_delio = soup.findAll('p', attrs={'class':'text-sm block font-medium line-clamp-2 lmd:text-base lmd:leading-5'}) 
for m4 in marka_majonez_delio[:-2]:
    print(m4.text.strip())


# In[12]:


#Delio - majonez - cena
soup = BeautifulSoup(page4.text, 'html.parser')
cena_majonez_delio = soup.findAll('span', attrs={'class':'text-primary-900 text-base'}) 
for c4 in cena_majonez_delio:
    print(c4.text.strip())


# In[13]:


#Delio - majonez - waga
soup = BeautifulSoup(page4.text, 'html.parser')
waga_majonez_delio = soup.findAll('p', attrs={'class':'text-xs text-gray-500 truncate mx-2 xsm:mx-4 pb-1'}) 
for w4 in waga_majonez_delio[:-2]:
    print(w4.text.strip())


# In[14]:


#Delio - olej - nazwa
page5=requests.get('https://delio.com.pl/categories/spizarnia-kawa-i-herbata/olej-oliwa-ocet/olej')
soup = BeautifulSoup(page5.text, 'html.parser')
marka_olej_delio = soup.findAll('p', attrs={'class':'text-sm block font-medium line-clamp-2 lmd:text-base lmd:leading-5'}) 
for m5 in marka_olej_delio:
    print(m5.text.strip())


# In[15]:


#Delio - olej - cena
soup = BeautifulSoup(page5.text, 'html.parser')
cena_olej_delio = soup.findAll('span', attrs={'class':'text-primary-900 text-base'}) 
for c5 in cena_olej_delio:
    print(c5.text.strip())


# In[16]:


#Delio - olej - waga
soup = BeautifulSoup(page5.text, 'html.parser')
waga_olej_delio = soup.findAll('p', attrs={'class':'text-xs text-gray-500 truncate mx-2 xsm:mx-4 pb-1'}) 
for w5 in waga_olej_delio:
    print(w5.text.strip())


# In[17]:


#Delio - woda niegazowana - nazwa
page6=requests.get('https://delio.com.pl/categories/woda-i-napoje/woda/niegazowana')
soup = BeautifulSoup(page6.text, 'html.parser')
marka_woda_delio = soup.findAll('p', attrs={'class':'text-sm block font-medium line-clamp-2 lmd:text-base lmd:leading-5'}) 
for m6 in marka_woda_delio[:-4]:
    print(m6.text.strip())


# In[18]:


#Delio - woda niegazowana - cena
soup = BeautifulSoup(page6.text, 'html.parser')
cena_woda_delio = soup.findAll('span', attrs={'class':'text-primary-900 text-base'}) 
for c6 in cena_woda_delio:
    print(c6.text.strip())


# In[19]:


#Delio - woda niegazowana - waga
soup = BeautifulSoup(page6.text, 'html.parser')
waga_woda_delio = soup.findAll('p', attrs={'class':'text-xs text-gray-500 truncate mx-2 xsm:mx-4 pb-1'}) 
for w6 in waga_woda_delio[:-4]:
    print(w6.text.strip())


# In[20]:


#Delio - cukier - nazwa
page7=requests.get('https://delio.com.pl/categories/spizarnia-kawa-i-herbata/przyprawysosy-fixy/cukier-i-slodziki')
soup = BeautifulSoup(page7.text, 'html.parser')
marka_cukier_delio = soup.findAll('p', attrs={'class':'text-sm block font-medium line-clamp-2 lmd:text-base lmd:leading-5'}) 
for m7 in marka_woda_delio[:-1]:
    print(m7.text.strip())


# In[21]:


#Delio - cukier - cena
soup = BeautifulSoup(page7.text, 'html.parser')
cena_cukier_delio = soup.findAll('span', attrs={'class':'text-primary-900 text-base'}) 
for c7 in cena_cukier_delio:
    print(c7.text.strip())


# In[22]:


#Delio - cukier - waga
soup = BeautifulSoup(page7.text, 'html.parser')
waga_cukier_delio = soup.findAll('p', attrs={'class':'text-xs text-gray-500 truncate mx-2 xsm:mx-4 pb-1'}) 
for w7 in waga_cukier_delio[-1]:
    print(w7.text.strip())


# In[23]:


with open("marka_mleko_delio.csv","w") as csv_file:
    writer=csv.writer(csv_file)
    for m1 in marka_mleko_delio:
         writer.writerow([m1.text.strip()])


# In[24]:


with open("cena_mleko_delio.csv","w") as csv_file:
    writer=csv.writer(csv_file)
    for c1 in cena_mleko_delio:
         writer.writerow([c1.text.strip()])


# In[25]:


with open("waga_mleko_delio.csv","w") as csv_file:
    writer=csv.writer(csv_file)
    for w1 in waga_mleko_delio:
         writer.writerow([w1.text.strip()])


# In[26]:


with open("marka_maslo_delio.csv","w") as csv_file:
    writer=csv.writer(csv_file)
    for m2 in marka_maslo_delio[:-2]:
         writer.writerow([m2.text.strip()])


# In[27]:


with open("cena_maslo_delio.csv","w") as csv_file:
    writer=csv.writer(csv_file)
    for c2 in cena_maslo_delio:
         writer.writerow([c2.text.strip()])


# In[28]:


with open("waga_maslo_delio.csv","w") as csv_file:
    writer=csv.writer(csv_file)
    for w2 in waga_maslo_delio[:-2]:
         writer.writerow([w2.text.strip()])


# In[29]:


with open("marka_kawa_delio.csv","w") as csv_file:
    writer=csv.writer(csv_file)
    for m3 in marka_kawa_delio:
         writer.writerow([m3.text.strip()])


# In[30]:


with open("cena_kawa_delio.csv","w") as csv_file:
    writer=csv.writer(csv_file)
    for c3 in cena_kawa_delio:
         writer.writerow([c3.text.strip()])


# In[31]:


with open("waga_kawa_delio.csv","w") as csv_file:
    writer=csv.writer(csv_file)
    for w3 in waga_kawa_delio:
         writer.writerow([w3.text.strip()])


# In[32]:


with open("marka_majonez_delio.csv","w") as csv_file:
    writer=csv.writer(csv_file)
    for m4 in marka_majonez_delio:
        writer.writerow([m4.text.strip()])


# In[33]:


with open("cena_majonez_delio.csv","w") as csv_file:
    writer=csv.writer(csv_file)
    for c4 in cena_majonez_delio:
         writer.writerow([c4.text.strip()])


# In[34]:


with open("waga_majonez_delio.csv","w") as csv_file:
    writer=csv.writer(csv_file)
    for w4 in waga_majonez_delio:
         writer.writerow([w4.text.strip()])


# In[35]:


with open("marka_olej_delio.csv","w") as csv_file:
    writer=csv.writer(csv_file)
    for m5 in marka_olej_delio:
         writer.writerow([m5.text.strip()])


# In[36]:


with open("cena_olej_delio.csv","w") as csv_file:
    writer=csv.writer(csv_file)
    for c5 in cena_olej_delio:
         writer.writerow([c5.text.strip()])


# In[37]:


with open("waga_olej_delio.csv","w") as csv_file:
    writer=csv.writer(csv_file)
    for w5 in waga_olej_delio:
         writer.writerow([w5.text.strip()])


# In[38]:


with open("marka_woda_delio.csv","w") as csv_file:
    writer=csv.writer(csv_file)
    for m6 in marka_woda_delio[:-4]:
         writer.writerow([m6.text.strip()])


# In[39]:


with open("cena_woda_delio.csv","w") as csv_file:
    writer=csv.writer(csv_file)
    for c6 in cena_woda_delio:
         writer.writerow([c6.text.strip()])


# In[40]:


with open("waga_woda_delio.csv","w") as csv_file:
    writer=csv.writer(csv_file)
    for w6 in waga_woda_delio[:-4]:
         writer.writerow([w6.text.strip()])


# In[41]:


with open("marka_cukier_delio.csv","w") as csv_file:
    writer=csv.writer(csv_file)
    for m7 in marka_cukier_delio[:-1]:
         writer.writerow([m7.text.strip()])


# In[42]:


with open("cena_cukier_delio.csv","w") as csv_file:
    writer=csv.writer(csv_file)
    for c7 in cena_cukier_delio:
         writer.writerow([c7.text.strip()])


# In[43]:


with open("waga_cukier_delio.csv","w") as csv_file:
    writer=csv.writer(csv_file)
    for w7 in waga_cukier_delio[:-1]:
         writer.writerow([w7.text.strip()])


# In[ ]:




