tpl = (True, True, True, False)


def all_true(tpl):
    return True if all(tpl) else False


print(all_true(tpl))