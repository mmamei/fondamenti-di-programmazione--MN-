
LOG_LEVEL = 2             # 0=ERROR, 1=INFO, 2=DEBUG (ma usato in modo incoerente)

def debug(msg):
    if LOG_LEVEL >= 2:
        print("[DEBUG]", msg)

def info(msg):
    if LOG_LEVEL >= 1:
        print("[INFO]", msg)

def error(msg):
    print("[ERROR]", msg)