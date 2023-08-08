import re
import os
palette = {
    'default': {
        'default': '\033[0m',
        'bold': '\033[1m',
        'underline': '\033[4m',
        'nounderline': '\033[24m',
        'reverse': '\033[7m',
        'positive': '\033[27'
    },
    'foreground': {
        'black': '\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'magenta': '\033[35m',
        'cyan': '\033[36m',
        'light_gray': '\033[37m',
        'light_black': '\033[90m',
        'light_red': '\033[91m',
        'light_green': '\033[92m',
        'light_yellow': '\033[93m',
        'light_blue': '\033[94m',
        'light_magenta': '\033[95m',
        'light_cyan': '\033[96m',
        'white': '\033[97m'
    },
    'background': {
        'black': '\033[40m',
        'dark_red': '\033[41m',
        'dark_green': '\033[42m',
        'dark_yellow': '\033[43m',
        'dark_blue': '\033[44m',
        'dark_magenta': '\033[45m',
        'dark_cyan': '\033[46m',
        'dark_white': '\033[47m',
        'bright_black': '\033[100m',
        'bright_red': '\033[101m',
        'bright_green': '\033[102m',
        'bright_yellow': '\033[103m',
        'bright_blue': '\033[104m',
        'bright_magenta': '\033[105m',
        'bright_cyan': '\033[106m',
        'white': '\033[107m'
    }
}

def colour(string: str, *colors: str) -> None:
    colors = list(map(lambda x: x.lower(), colors))
    result = []
    lookahead = re.compile(r'\$[dbf]\$', re.I | re.M)
    matches = lookahead.finditer(string)
    prev_end = 0
    for idx, match in enumerate(matches):
        start, end = match.span()
        result.append(string[prev_end:start])
        pattern = match.group()
        case = 'default' if pattern == '$d$' else ('foreground' if pattern == '$f$' else 'background')
        result.append(palette[case][colors[idx]])
        prev_end = end
    result.append(string[prev_end:])
    colored_string = ''.join(result)
    return os.system('echo ' + colored_string + palette['default']['default'])

print("=" * 100)
colour("Custom API: $f$C$f$o$f$l$f$o$f$u$f$r$f$s$f$.", "Light_red", "yellow", "light_yellow", "light_green", "light_cyan", "light_blue", "light_magenta", "white")
print("=" * 100)
if __name__ == '__main__':
    pass
