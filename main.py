import concurrent.futures
import time
import webbrowser


def do_something(seconds):
    print(f'Sleeping {seconds} second(s...)')
    time.sleep(seconds)
    return 'Done Sleeping...'


def follow_twitch(seconds):
    print(f'Opening Twitch within chrome in {seconds} second(s)...')
    twitch = "https://www.twitch.tv/yourdestinyis"
    webbrowser.register('chrome',
                        None,
                        webbrowser.BackgroundBrowser(
                            "C:\Program Files\Google\Chrome\Application/chrome.exe"))
    webbrowser.get('chrome').open_new(twitch)
    return 'Successfully opened chrome, & opened Twitch tab'

def follow_youtube(seconds):
    print(f'Opening youtube inside chrome as a tab in {seconds} second(s)...')
    youtube = "https://www.youtube.com/channel/UC7gypqZF6y3cl437Smt3IVw"
    webbrowser.register('chrome',
                        None,
                        webbrowser.BackgroundBrowser(
                            "C:\Program Files\Google\Chrome\Application/chrome.exe"))
    webbrowser.get('chrome').open_new(youtube)
    return 'Successfully opened chrome, & opened Youtube tab....'

def follow_twitter(seconds):
    print(f'Opening Twitter inside chrome as a tab in {seconds} second(s)...')
    twitter = "https://twitter.com/AylissaHeart"
    webbrowser.register('chrome',
                        None,
                        webbrowser.BackgroundBrowser(
                            "C:\Program Files\Google\Chrome\Application/chrome.exe"))
    webbrowser.get('chrome').open_new(twitter)
    return 'Successfully opened chrome, & opened Twitter tab....'


with concurrent.futures.ThreadPoolExecutor() as executor:
    f1 = executor.submit(do_something, 1)
    print(f1.result())
    f2 = executor.submit(follow_twitch, 1)
    print(f2.result())
    f3 = executor.submit(follow_youtube, 1)
    print(f3.result())
    f4 = executor.submit(follow_twitter, 1)
    print(f4.result())
# list comprehension idea for running multiple loops of the same function
# secs = [5, 4, 3, 2, 1]
# results = [executor.submit(do_something, sec) for sec in secs]
# for f in concurrent.futures.as_completed(results):
# print(f.result())
# submit function returns FUTURE object

# how to map (will run function with all values asyncronous, returns results in order it was started) follow this
#   secs = [5, 4, 3, 2, 1]
#   results = executor.map(do_something, secs)
#    for result in results:
#       print(result)


# older version.
# threads = []

# this _ is a throw away variable, the range is how many times you wish to run said target function
# args is for the number of seconds you wish for that function to take or any other paramater you passed in

# for _ in range(1):
#   t = threading.Thread(target=start_chrome, args=[2.5])
#   t.start()
#    threads.append(t)

# for thread in threads:
#    thread.join()

finish = time.perf_counter()

print(f'Finished in {round(finish, 2)} second(s)')
