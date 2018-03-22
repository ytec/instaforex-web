from .model import AccountType, Language, AccountCurrency, TraderType

class data_forms():
        client = Client('http://client-api.instaforex.com/soapservices/OpenAccount.svc?wsdl')

    AccountTypeSAOP = client.factory.create('AccountType')
    for s in AccountTypeSOAP:
        AccountType(
                    name = s[0],
                    value = s[1])
        AccountType.save()

    LanguageSOAP = client.factory.create('Language')
    for s in LanguageSOAP:
        Language(
                    name = s[0],
                    value = s[1])
        Language.save()

    AccountCurrencySOAP = client.factory.create('AccountCurrency')
    for s in AccountCurrencySOAP:
        AccountCurrency(
                    name = s[0],
                    value = s[1])
        AccountCurrency.save()
    #TraderTypeSOAP = client.factory.create('TraderType')
    for s in TraderTypeSOAP:
        TraderType(
                    name = s[0],
                    value = s[1])
        TraderType.save()
