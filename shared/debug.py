from .libraries import colored,timedelta,timer

def formatTime(seconds):
    if seconds < 1e-6:  # If it's less than a microsecond
        return f"{colored(f'{seconds * 1e9:.2f}','magenta')} {colored('ns microsecond','cyan')}"
    elif seconds < 1e-3:  # If it's less than a millisecond
        return f"{colored(f'{seconds * 1e6:.2f}','magenta')} {colored('µs millisecond','cyan')}"
    elif seconds < 1:  # If it's less than a second
        return f"{colored(f'{seconds * 1e3:.2f}','magenta')} {colored('ms second','cyan')}"
    else:
        return str(timedelta(seconds=seconds))
    
def ticktock(func):
    def wrapper(*args, **kwargs):
        start=timer()
        func(*args, **kwargs)
        end=timer()
        print(colored(f'🛰️ Function {func.__name__}()\t','green'),'\t\t: Took ',formatTime(end-start))
    return wrapper