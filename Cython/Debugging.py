###############################################
#
#   Odds and ends for debugging
#
###############################################

def print_call_chain(*args):
    import sys
    print(" ".join(map(str, args)))
    f = sys._getframe(1)
    while f:
        name = f.f_code.co_name
        if s := f.f_locals.get('self', None):
            if c := getattr(s, "__class__", None):
                name = f"{c.__name__}.{name}"
        print(f"Called from: {name} {f.f_lineno}")
        f = f.f_back
    print("-" * 70)
