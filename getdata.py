import pandas as pd
from bs4 import BeautifulSoup
import urllib
import re



class get_deal_rules:

    def get_rules(self,url):

        html = urllib.request.urlopen(url).read()

        soup = BeautifulSoup(html, 'html.parser')

        df = pd.DataFrame(columns=['Par', 'Quantidade mínima da ordem', 'Movimentação mínima do preço', 'Valor total mínimo da ordem'])

        # Collecting Ddata
        for row in soup.tbody.find_all('tr'):    
            # Find all data for each column
            columns = row.find_all('td')
            
            if(columns != []):
                Par = columns[0].text.strip()
                QMO= columns[1].text.strip()
                MMP= columns[2].text.strip()
                VTMO= columns[3].text.strip()

                df = df.append({'Par': Par,  'Quantidade mínima da ordem': QMO, 'Movimentação mínima do preço': MMP, 'Valor total mínimo da ordem': VTMO}, ignore_index=True)
        for i in range(0,len(df)):
            df['Par'][i]=df['Par'][i].replace('/BRL','_BRL')
            x=0
            x=df.iloc[i][1].split()
            df.iloc[i][1]=x[0]
            df.iloc[i][1]=df.iloc[i][1].replace(',','.')
            if (df.iloc[i][1].count('.')) > 1:
                df.iloc[i][1]=df.iloc[i][1].replace('.','')
            df.iloc[i][1]=float(df.iloc[i][1])
            
            df.iloc[i][2]=re.sub('[A-Z]*','',df.iloc[i][2]).strip()
            df.iloc[i][2]=df.iloc[i][2].replace(',','.')
            df.iloc[i][2]=float(df.iloc[i][2])
            
            df.iloc[i][3]=re.sub('[A-Z]*','',df.iloc[i][3]).strip()
            df.iloc[i][3]=float(df.iloc[i][3])

        return df  


