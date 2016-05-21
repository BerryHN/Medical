init -100 python:

    def re_check(regexp):
        import re
        reg = re.compile(regexp)
        return lambda str: reg.match(str)

    def less_check(val):
        return lambda str: int(str) < val

    def greater_check(val):
        return lambda str: int(str) > val

    def all_of_checks_inner(checks,str):
        for check in checks:
            if not check(str):
                return False
        return True
    def all_of_checks(checks):
        return lambda str: all_of_checks_inner(checks,str)
