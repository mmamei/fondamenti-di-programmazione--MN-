
def log_decorator(f):
    from datetime import datetime
    def newf(*x):
        with open('log.txt','a') as logfile:
            # aggiungi l'orario della chiamata
            logfile.write(f'Chiamata a funzione {f.__name__} alle {datetime.now()}\n')
        return f(*x)
    return newf

