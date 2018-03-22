from suds.client import Client

class form_not_if_data():

    def Real():
        client = Client('http://client-api.instaforex.com/soapservices/OpenAccount.svc?wsdl')
        Dicc_AccountType = []
        Dicc_Language = []
        Dicc_AccountCurrency = []
        Dicc_TraderType = []

        AccountType = client.factory.create('AccountType')

        for s in AccountType:
            name' : s[0],
                  'value' : s[1]}
            Dicc_AccountType.append(d)

        Language = client.factory.create('Language')

        for a in Language:
            h = {'name' : a[0],
                'value' : a[1]}
            Dicc_Language.append(h)

        AccountCurrency = client.factory.create('AccountCurrency')

        for q in AccountCurrency:
            f = {'name' : q[0],
                'value' : q[1]}
            Dicc_AccountCurrency.append(f)

        #TraderType = client.factory.create('TraderType')

        #for z in TraderType:
        #    e = {'name' : z[0],
        #        'value' : z[1]}
        #    Dicc_TraderType.append(e)

        FormName = 'Real'

        Dicc_name = { 'name' : FormName,
                      'AccountType' : Dicc_AccountType,
                      'Language' : Dicc_Language,
                      'AccountCurrency' : Dicc_AccountCurrency,
        #              'TraderType' : Dicc_TraderType,
                    }

        return Dicc_name
    def Demo():
        client = Client('http://client-api.instaforex.com/soapservices/OpenAccount.svc?wsdl')
        Dicc_AccountType = []
        Dicc_Language = []
        Dicc_AccountCurrency = []
        Dicc_TraderType = []

        AccountType = client.factory.create('AccountType')

        for s in AccountType:
            d = {'name' : s[0],
                'value' : s[1]}
            Dicc_AccountType.append(d)

        Language = client.factory.create('Language')

        for a in Language:
            h = {'name' : a[0],
                'value' : a[1]}
            Dicc_Language.append(h)

        AccountCurrency = client.factory.create('AccountCurrency')

        for q in AccountCurrency:
            f = {'name' : q[0],
                'value' : q[1]}
            Dicc_AccountCurrency.append(f)

        TraderType = client.factory.create('TraderType')

        for z in TraderType:
            e = {'name' : z[0],
                'value' : z[1]}
            Dicc_TraderType.append(e)
        FormName = 'Demo'
        Dicc_name = { 'name' : FormName,
                      'AccountType' : Dicc_AccountType,
                      'Language' : Dicc_Language,
                      'AccountCurrency' : Dicc_AccountCurrency,
                      'TraderType' : Dicc_TraderType,
                    }
        return Dicc_name
