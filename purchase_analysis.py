# -*- coding: utf-8 -*-

def purchase_analysis(stock_market=None, day_purchase=0, sale_day=0):
    len_ = len(stock_market)    
    day_purchase -= 1
    sale_day -= 1                                 
    
    if not day_purchase < sale_day:
        print('Dia de compra deve ser maior que dia de venda!')
        return 0

    if not 0 <= day_purchase < len_:
        print('Dia de compra fora de faixa!')
        return 0

    if not 0 <= sale_day < len_:
        print('Dia de venda fora de faixa!')
        return 0
    
    result = stock_market[sale_day] - stock_market[day_purchase]
    
    return result if result > 0 else 0


print(purchase_analysis(
        stock_market=[7, 1, 5, 3, 6, 4], day_purchase=2, sale_day=4))    

print(purchase_analysis(
        stock_market=[7, 6, 4, 3, 1], day_purchase=2, sale_day=5))    
    