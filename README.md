a script to automate sending stupid emails to the government
primarily in order to clog up their snitch email.
This idea here is to fill the DEIAtruth@opm.gov snitch hotline with bogus emails so that they are
less effective in reaching and acting on any potential "real" emails.

v1.0 January 23rd 2025
It's a little sloppy, but it works.


The only variables you need to change are the "email_username", "app_password", "send_limit", and send_randomized. Otherwise, it should just run.

email_username: the username/email address of the sending email.

app_password: the password used to log into the sending email. regular password usually doesn't work.

send_limit: how many emails get sent. If send_randomized is False, rounds down to the nearest whole number divisible by the number of pre-selected names.

send_randomized: A true/false option to turn on a mode that randomizes "target" information to be a combination of common first and last names, with
randomized locations, ages, and federal departments.

This script offers two scenarios: targeted emails, with "real" people (i.e. Doland Trumpf, Melon Husk), and
randomized emails, which generates a bogus email with fake names, ages, and locations as a red herring.
The randomized emails are not intended to be real people, but fakes names, like "John Doe" to further
clog the system of fascist bureaucracy. It might be better to leave this mode as "false," unless
you feel like really throwing as many names at the wall as possible.

it requires a valid email address, but if you're using gmail, you can't log in with your regular password.
you have to set up an app password, which requires 2fa, which requires a phone number,
but you can get around this by using the google authenticator app instead. Once you generate
an app passowrd, use that instead.

The first emails sent are always real names of whoever is in the pre_random_list
Feel free to customize the individual aspects of this list, or the names in the randomized list below that.

Not comfortable sending a misleading gibberish witch hunt email with randomized personal information
that could, in theory, be a real person?
Change "send_randomized" to "False" to turn this feature off! Now it just sends targeted emails
against specific people in power, from the "pre_random_dict" list. The script will iterate
through the list of pre-selected names until it reaches your send limit.
