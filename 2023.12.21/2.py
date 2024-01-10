def deck() -> tuple:
    """Создаёт колоду карт"""
    
    nominals = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    suits = ['черви', 'бубны', 'пики', 'трефы']
    
    for n in suits:
        for j in nominals:
            resume = [j, n]
            resume = tuple(resume)
            
            yield resume


# >>> list(deck())[::13]
# [(2, 'черви'), (2, 'бубны'), (2, 'пики'), (2, 'трефы')]