MAX_STARS = 30
WIDTH = 80


def print_result(number):
    stars_count = int
    if number == 0:
        pass
    #     stars_count = MAX_STARS
    else:
        stars_count = round(MAX_STARS / number)
        if stars_count > MAX_STARS:
            stars_count = MAX_STARS

    number_field_width = WIDTH - 2 * stars_count
    stars = '*' * stars_count
    fmt = '{0}{1:^' + str(number_field_width) + '}{0}'

    print(fmt.format(stars, number))
