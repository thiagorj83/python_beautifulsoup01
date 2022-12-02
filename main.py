from getdata import get_deal_rules


get_drules=get_deal_rules()


def main():
    url="https://www.novadax.com.br/regras-de-negociacao"
    get_deal_rules.get_rules(url)
    drules=get_drules.get_rules(url)
    print(drules)
    
if __name__=='__main__':

    main()