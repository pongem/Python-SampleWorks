

from mod_SET_Helper import *


helper = SETFetch()
setdata = SetData()

print ( setdata.arrAllSets[0] )

print ( setdata.isStockInSet("cpf") )

print ( helper.fetchCurrentStockInfo("CPF") )