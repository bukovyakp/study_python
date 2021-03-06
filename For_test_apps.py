# codding: utf-8

"""
Здесь функция testdriver выполняет в цикле серию тестов (модуль te­stapi – не-
кая абстракция в этом примере). Поскольку в обычной ситуа­ции необработан-
ное исключение приводило бы к  завершению самого тестового приложения,
можно обернуть вызовы очередного теста инст­рукцией try, чтобы обеспечить
продолжение процесса тестирования по­сле неудачного завершения любого из
тестов. Здесь, как обычно, пустое предложение except перехватывает любые не-
обработанные исключения, возникшие в ходе выполнения теста, и регистриру-
ет в файле информа­цию об исключении, полученную с помощью функции sys.
exc_info. Предложение else выполняется в  случае отсутствия исключений  –
когда тест завершился благополучно.
"""


import sys
log = open('testlog', 'a')
from testapi import moreTests, runNextTest, testName
def testdriver():
    while moreTests():
        try:
            runNextTest()
        except:
            print('FAILED', testName(), sys.exc_info()[:2], file=log)
        else:
            print('PASSED', testName(), file=log)

testdriver()