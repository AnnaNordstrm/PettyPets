import time


def sleep_level(trySleep, sleepLevel, deltatime):

    sleep = False

    sleepLevel = sleepLevel - (0.035 * int(deltatime))
    if trySleep:
        if sleepLevel < 50:

            sleep = True
        else:

            sleep = False
    if sleepLevel < 0:

        sleep = True

    if sleep:
        while sleepLevel < 100:
            sleepLevel = sleepLevel + 0.24

    return sleepLevel, sleep

