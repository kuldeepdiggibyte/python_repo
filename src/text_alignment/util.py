import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')


def text_alignment():
    thickness = int(input())  # This must be an odd number
    c = 'H'
    ans = ''

    # Top Cone
    for i in range(thickness):
        logging.info((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))
        temp = (c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1)
        ans += temp+"\n"

    # Top Pillars
    for i in range(thickness + 1):
        logging.info((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))
        temp = (c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6)
        ans += temp+"\n"

    # Middle Belt
    for i in range((thickness + 1) // 2):
        logging.info((c * thickness * 5).center(thickness * 6))
        temp = (c * thickness * 5).center(thickness * 6)
        ans += temp+"\n"

        # Bottom Pillars
    for i in range(thickness + 1):
        logging.info((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))
        temp = (c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6)
        ans += temp+"\n"

        # Bottom Cone
    for i in range(thickness):
        logging.info(((c * (thickness - i - 1)).rjust(thickness) + c + (c * (thickness - i - 1)).ljust(thickness)).rjust(
            thickness * 6))
        temp = ((c * (thickness - i - 1)).rjust(thickness) + c + (c * (thickness - i - 1)).ljust(thickness)).rjust(
            thickness * 6)
        ans += temp+"\n"

    return ans